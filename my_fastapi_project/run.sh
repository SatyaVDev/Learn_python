#!/bin/bash

# Check if PORT is set in the environment
PORT=${PORT:-8000}

# Run the FastAPI app using Uvicorn
uvicorn app.main:app --reload --port $PORT
