import json

def normalize_report(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)

    audits = extract_raw_audits(data)

    cleaned = []

    for val in audits:
        score = val.get("score")

        # skip if score is None
        if score is None:
            continue

        # skip good items
        if score >= 0.9:
            continue

        cleaned.append({
            "title": val.get("title", "Unknown Issue"),
            "description": val.get("description", ""),
            "score": score,
            "severity": get_severity(score)
        })

    return cleaned


def extract_raw_audits(data):
    audits = []

    # Lighthouse / PageSpeed
    if isinstance(data, dict):
        if "lighthouseResult" in data:
            raw = data["lighthouseResult"].get("audits", {})
        else:
            raw = data.get("audits", {})

        for key, val in raw.items():
            if isinstance(val, dict):
                audits.append(val)

    # List-based reports
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, dict):
                audits.extend(extract_raw_audits(item))

    return audits


def get_severity(score):
    if score < 0.5:
        return "High"
    elif score < 0.8:
        return "Medium"
    else:
        return "Low"