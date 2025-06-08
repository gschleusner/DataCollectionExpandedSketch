# Data Collection Expanded Sketch

A StrangeMatter component-based data collection system that enables structured information requests and responses with full traceability.

## Overview

This application demonstrates a complete workflow where users can create information requests, deliver them to assigned individuals, and capture responses using the StrangeMatter schema. All questions, responses, and connected information are preserved and linked together.

## Features

### 🎯 Core Functionality
- **Two-Phase Workflow**: Request creation and response collection
- **StrangeMatter Integration**: Uses HOK StrangeMatter component templates
- **Voice-to-Text**: Speech recognition for efficient data entry
- **Database Storage**: SQLite for local development, PostgreSQL for deployment
- **Modern UI**: Beautiful, responsive web interface

### 📊 StrangeMatter Schema
- Follows `hok.projectdata.request.dynamic.json` template for requests
- Uses `hok.projectdata.dynamic.json` template for responses  
- Maintains full component relationships via `Using` field
- Preserves all metadata including timestamps, GUIDs, and hashes

## Quick Start

### Prerequisites
- Python 3.8+
- pip

### Installation

1. **Clone and setup**:
```bash
git clone <your-repo-url>
cd DataCollectionExpandedSketch
pip install -r requirements.txt
```

2. **Start the server**:
```bash
python run_server.py
```

3. **Open your browser**:
Navigate to [http://localhost:8000](http://localhost:8000)

## User Workflows

### Workflow 1: Creating a Request

1. Navigate to the home page and click **"Create Data Request"**
2. Fill out the form:
   - **Assigned To**: Email of the person who should answer
   - **Instructions**: Detailed guidance for completing the request
   - **Task Description**: Brief summary of what's needed
   - **Questions**: Add one or more questions with types (text, number, date, choice)
3. Submit the request - it's saved as a StrangeMatter component

### Workflow 2: Answering Requests

1. Navigate to **"Answer Requests"** from the home page
2. Select a person from the dropdown to see their assigned requests
3. Click on a specific request to view details and questions
4. For each question:
   - Type your answer directly, OR
   - Click the 🎤 microphone icon to use voice input
5. Submit your response - it's linked to the original request via StrangeMatter schema

## Technical Architecture

### Backend (FastAPI)
- **Database**: SQLAlchemy with SQLite (development) / PostgreSQL (production)
- **Models**: StrangeMatter component schema mapped to relational database
- **API Endpoints**: RESTful API for CRUD operations
- **Templates**: Jinja2 for server-side rendering

### Frontend
- **Framework**: Vanilla JavaScript with Bootstrap 5
- **Voice Recognition**: Web Speech API (Chrome/Edge support)
- **Responsive Design**: Mobile-friendly interface
- **Real-time Updates**: Dynamic content loading

### Database Schema

The `StrangeMatterComponent` model includes:
- StrangeMatter standard fields (ComponentType, GUIDs, timestamps)
- Relationship tracking (`Using` field links responses to requests)
- JSON payload storage for questions and answers
- Indexing for efficient querying by assigned person

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main application interface |
| `/create-request` | GET | Request creation form |
| `/answer-requests` | GET | Response interface |
| `/api/requests` | POST | Create new request |
| `/api/requests/{person}` | GET | Get requests for person |
| `/api/request/{id}` | GET | Get specific request details |
| `/api/responses` | POST | Submit response |
| `/api/assigned-people` | GET | List people with requests |

## StrangeMatter Integration

### Request Components
```json
{
  "ComponentType": "https://github.com/HOKGroup/hok_strangematter_components/DataCollectionComponents/hok.projectdata.request.dynamic.json",
  "Function": ["AGM:ENT:SELF"],
  "ComponentClassification": {"Value": "hok.projectdata.request.dynamic"},
  "Payload": {
    "instructions": "...",
    "taskDescription": "...",
    "questions": [...]
  }
}
```

### Response Components
```json
{
  "ComponentType": "https://github.com/HOKGroup/hok_strangematter_components/DataCollectionComponents/hok.projectdata.dynamic.json",
  "Function": ["Response"],
  "Using": ["<request_entity_guid>"],
  "ComponentClassification": {"Value": "hok.projectdata.dynamic"},
  "Payload": {
    "question_1": {"question": "...", "answer": "...", "type": "text"}
  }
}
```

## Deployment

### Development
```bash
python run_server.py
```

### Production (Dokku)
```bash
# Build and deploy
git push dokku main

# Set environment variables
dokku config:set myapp DATABASE_URL=postgresql://...
```

## Browser Compatibility

- **Voice Recognition**: Chrome, Edge, Safari (WebKit)
- **General Interface**: All modern browsers
- **Responsive Design**: Mobile and desktop optimized

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is part of the HOK StrangeMatter ecosystem. See the main repository for licensing information.

---

**Built with**: FastAPI, SQLAlchemy, Bootstrap 5, and the HOK StrangeMatter Components framework. 