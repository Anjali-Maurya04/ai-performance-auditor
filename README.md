# AI Audit assisstant

This project is an AI-powered performance audit assistant that analyzes website performance reports and generates actionable optimization recommendations using LLMs.

## What It Does

- Parses website audit reports
- Cleans and structures performance issues
- Uses an LLM (Groq + LLaMA 3.1) to generate optimization suggestions
- Deduplicates and prioritizes recommendations
- Outputs a sorted list of improvements based on impact and complexity

---

## Tech Stack

- Python
- LangChain
- Groq LLM 
- dotenv (for environment variables)

---

##  Setup Instructions

### 1. Clone / Extract Project
git clone <your-repo-url>
cd ai_audit


##  Create Virtual Environment

- python3 -m venv venv
- source venv/bin/activate   # Mac/Linux

##  Install Dependencies 

- pip install -r requirements.txt


##  Add Environment Variables

GROQ_API_KEY=your_api_key_here

## How to run

from main import run_pipeline

result = run_pipeline("report.json")

print(result)

## Pipeline Flow
- Load audit report
- Normalize data (parser.py)
- Chunk issues (utils.py)
- Send chunks to LLM
- Parse JSON responses
- Deduplicate recommendations
- Sort results
