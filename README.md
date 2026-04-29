# SaaS Speed Optimization AI Agent

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
- Groq LLM (LLaMA 3.1)
- dotenv (for environment variables)

---

##  Project Structure
ai_audit/
│── main.py # Main pipeline
│── parser.py # Data normalization
│── utils.py # Chunking logic
│── assistant.py # (Optional helper logic)
│── prompts.py # Prompt templates
│── storage.py # Data storage (if used)
│── report.json # Sample input
│── history.json # Logs/history
│── .env # API keys

##  Setup Instructions

### 1. Clone / Extract Project

cd 07_Saas_SpeedOptimization/ai_audit


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