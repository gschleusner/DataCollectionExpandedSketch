#!/usr/bin/env python3
"""
Data Collection Expanded Sketch Server
Run this script to start the FastAPI server
"""

import uvicorn
import sys
import os

# Add app directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

if __name__ == "__main__":
    print("🚀 Starting Data Collection Expanded Sketch Server...")
    print("📊 StrangeMatter Component-Based Data Collection System")
    print("🌐 Server will be available at: http://localhost:8000")
    print("📝 Create requests at: http://localhost:8000/create-request")
    print("🎤 Answer requests at: http://localhost:8000/answer-requests")
    print("-" * 60)
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        app_dir="app"
    ) 