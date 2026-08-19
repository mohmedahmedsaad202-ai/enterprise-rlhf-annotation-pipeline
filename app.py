from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import json

app = FastAPI(title="Enterprise RLHF Annotation Platform API")

# In-memory database simulation
db = []

class AnnotationPayload(BaseModel):
    task_id: int
    annotator_id: str
    preferred_response: str  # "Response A" or "Response B"
    hallucination_detected: bool
    quality_score: int  # 1 to 5

@app.post("/annotate/")
def submit_annotation(payload: AnnotationPayload):
    if payload.quality_score < 1 or payload.quality_score > 5:
        raise HTTPException(status_code=400, detail="Quality score must be between 1 and 5.")
    
    db.append(payload.dict())
    return {"status": "SUCCESS", "recorded_entries": len(db)}

@app.get("/export/rlhf-dataset/")
def export_dataset():
    """Exports dataset structured for Direct Preference Optimization (DPO) training."""
    exported_data = [
        {
            "task_id": entry["task_id"],
            "chosen": entry["preferred_response"],
            "rejected": "Response B" if entry["preferred_response"] == "Response A" else "Response A",
            "flagged_hallucination": entry["hallucination_detected"]
        }
        for entry in db
    ]
    return {"dataset_type": "DPO_Pairs", "count": len(exported_data), "data": exported_data}
