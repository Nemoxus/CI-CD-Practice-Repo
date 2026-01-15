from fastapi import FastAPI
from app.logic import assess_risk
from app.models import InputData

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(data: InputData):
    risk = assess_risk(data.age, data.cholesterol)
    return {"risk": risk}
