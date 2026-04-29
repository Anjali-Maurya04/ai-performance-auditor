import json
import os

# Save
def save_to_history(result):
    file = "history.json"

    if os.path.exists(file):
        with open(file, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(result)

    with open(file, "w") as f:
        json.dump(data, f, indent=2)

    print("Saved to history ✅")


# View
def view_history():
    try:
        with open("history.json", "r") as f:
            data = json.load(f)

        print(f"\nTotal past audits: {len(data)}")

        for i, audit in enumerate(data):
            print(f"\nAudit {i+1}: {len(audit)} recommendations")

    except:
        print("No history found")


# Compare
def compare_audits():
    try:
        with open("history.json", "r") as f:
            data = json.load(f)

        if len(data) < 2:
            print("Not enough data to compare")
            return

        last = data[-1]
        prev = data[-2]

        last_titles = set([i["title"] for i in last])
        prev_titles = set([i["title"] for i in prev])

        print("\n=== Comparison ===")

        print("\nNew Issues:")
        for item in last_titles - prev_titles:
            print("-", item)

        print("\nResolved Issues:")
        for item in prev_titles - last_titles:
            print("-", item)

    except:
        print("Error reading history")