# SunoSeek - Voice Job Assistant (Placeholder Prototype)

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class VoiceQuery(BaseModel):
    user_id: str
    language: str
    text: str

# Mock job database
jobs = [
    {"role": "Tailor", "location": "Hyderabad", "salary": "₹12,000", "summary": "Silai ka kaam, full time"},
    {"role": "Driver", "location": "Mumbai", "salary": "₹18,000", "summary": "Ghar ka driver, 8 ghante"},
]

@app.post("/voice_query")
def handle_voice(q: VoiceQuery):
    # Simple mock job matching
    matches = [job for job in jobs if q.text.lower() in job["role"].lower()]
    if matches:
        return {"response": matches}
    return {"response": "No matching jobs found."}
