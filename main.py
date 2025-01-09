# Copyright 2024
# Directory: fastapi-gcp-pro/main.py

from fastapi import FastAPI
from datetime import datetime
import requests
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="FastAPI GCP Pro")

# Define allowed origins for CORS
origins = [
    "http://localhost:3000",
    "http://localhost:3001",
    "https://launch-an-app.vercel.app"
]

# Add CORS middleware to the application
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,  # Allow credentials (cookies, authorization headers)
    allow_methods=["*"],    # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],    # Allow all headers
)


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