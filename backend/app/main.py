from fastapi import FastAPI
from datetime import datetime
import os

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "AI SOC Lab Backend Running",
        "timestamp": str(datetime.utcnow())
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.get("/logs/test")
def test_log():
    return {
        "event": "test_log",
        "severity": "info",
        "timestamp": str(datetime.utcnow())
    }
