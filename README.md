# Enterprise RLHF Data Annotation & Quality Pipeline

A Python-based enterprise data platform for orchestrating Human-in-the-Loop (HITL) annotations, quality control, and Direct Preference Optimization (DPO) dataset generation for LLMs.

## Core Architecture
1. **Data Ingestion & Sanitization (`pipeline.py`):** Automated PII masking and schema validation.
2. **Quality Assurance Engine (`metrics.py`):** Calculates Inter-Annotator Agreement (IAA) ratios to filter out noisy annotator ratings.
3. **API & Dataset Exporter (`app.py`):** REST API built with FastAPI to ingest worker votes and export formatted preference pairs for LLM fine-tuning.

## Tech Stack
- **Backend:** Python 3.10+, FastAPI, Pydantic
- **Data Engineering:** NumPy, JSON Schema Parsing, Regex Sanitization

## Quickstart
```bash
pip install fastapi uvicorn numpy
uvicorn app:app --reload
