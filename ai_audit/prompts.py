from langchain.prompts import PromptTemplate

EXTRACTION_PROMPT = PromptTemplate(
    input_variables=["data"],
    template="""
You are a performance expert.

Analyze the following audit issues:
{data}

Extract actionable optimization recommendations.

Return JSON list:
[
  {{
    "title": "...",
    "why": "...",
    "complexity": "Low|Medium|High",
    "impact": "Low|Medium|High",
    "notes": "..."
  }}
]
"""
)

FINAL_PROMPT = PromptTemplate(
    input_variables=["all_recommendations"],
    template="""
You are a senior performance engineer.

Given these recommendations:
{all_recommendations}

1. Remove duplicates
2. Merge similar items
3. Prioritize based on impact vs effort

Return final JSON:
[
  {{
    "title": "...",
    "why": "...",
    "complexity": "...",
    "impact": "...",
    "priority": 1-10,
    "notes": "..."
  }}
]
"""
)