import json
from parser import normalize_report
from utils import chunk_data

from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
import os

# Load env
load_dotenv()


def run_pipeline(file_path):
    print("API KEY LOADED:", os.getenv("GROQ_API_KEY") is not None)

    # Step 1: Load + Clean Data
    data = normalize_report(file_path)
    print("Cleaned audits:", len(data))

    # Step 2: Initialize LLM
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0
    )

    # Step 3: Prompt Template
    prompt = PromptTemplate(
        input_variables=["issues"],
        template="""
You are a senior performance engineer.

Given these website performance issues:
{issues}

Generate actionable optimization recommendations.

STRICT RULES:
- Return ONLY valid JSON
- No explanation, no extra text
- Keep responses concise

Return format:
[
  {{
    "title": "...",
    "why": "...",
    "impact": "Low|Medium|High",
    "complexity": "Low|Medium|High",
    "notes": "..."
  }}
]
"""
    )

    chain = prompt | llm | StrOutputParser()

    # Step 4: Chunking
    chunks = list(chunk_data(data, size=4))
    print("Total chunks:", len(chunks))

    # Step 5: LLM Processing
    results = []

    for i, chunk in enumerate(chunks):
        print(f"\nProcessing chunk {i+1}/{len(chunks)}")

        try:
            res = chain.invoke({
                "issues": json.dumps(chunk, indent=2)
            })
            results.append(res)

        except Exception as e:
            print("Error:", e)

    # Step 6: Merge + Clean Output
    def safe_parse(json_str):
        try:
            return json.loads(json_str)
        except:
            return []

    all_recommendations = []

    for r in results:
        parsed = safe_parse(r)
        all_recommendations.extend(parsed)

    # Step 7: Deduplicate
    unique = {}

    for item in all_recommendations:
        title = item.get("title")
        if title and title not in unique:
            unique[title] = item

    final_list = list(unique.values())

    # Step 8: Priority Scoring
    def get_priority(impact, complexity):
        score_map = {"High": 3, "Medium": 2, "Low": 1}
        return score_map.get(impact, 1) * 2 - score_map.get(complexity, 1)

    for item in final_list:
        item["priority_score"] = get_priority(
            item.get("impact"),
            item.get("complexity")
        )

    # Step 9: Sort
    final_list.sort(key=lambda x: x["priority_score"], reverse=True)

    return final_list