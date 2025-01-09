# Copyright 2024
# Directory: fastapi-gcp-pro/main.py

from fastapi import FastAPI
from datetime import datetime
import requests

app = FastAPI(title="FastAPI GCP Pro")

@app.get("/")
async def root():
    """Root endpoint returning a welcome message."""
    return {"message": "Welcome to FastAPI GCP Pro"}

@app.get("/greet/{name}")
async def greet(name: str):
    """
    Greet endpoint that returns a personalized greeting.
    
    Args:
        name (str): Name of the person to greet
    """
    return {"message": f"Hello, {name}! I think you are great!"}

@app.get("/weather")
async def fetch_weather_today():
    """Fetch current weather data from a mock API."""
    # Note: In a real application, you would use an actual weather API
    # This is a mock response
    mock_weather = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "temperature": 22,
        "condition": "Sunny",
        "location": "Sample City"
    }
    return mock_weather 