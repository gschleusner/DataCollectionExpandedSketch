from fastapi import FastAPI, HTTPException, Depends, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import json
import uuid
from datetime import datetime
import hashlib

from database import SessionLocal, engine, Base
from models import StrangeMatterComponent
from schemas import ComponentCreate, ComponentResponse
from utils import create_component_from_template, generate_unique_ids

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Data Collection Expanded Sketch", version="1.0.0")

# Mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Root endpoint - shows main task selection
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Request creation UI
@app.get("/create-request", response_class=HTMLResponse)
async def create_request_form(request: Request):
    return templates.TemplateResponse("create_request.html", {"request": request})

# Response/Answer UI - shows assigned requests
@app.get("/answer-requests", response_class=HTMLResponse)
async def answer_requests_form(request: Request):
    return templates.TemplateResponse("answer_requests.html", {"request": request})

# API endpoint to create a new request
@app.post("/api/requests")
async def create_request(
    assigned_to: str = Form(...),
    description: str = Form(...),
    task_description: str = Form(...),
    questions: str = Form(...),  # JSON string of questions
    db: Session = Depends(get_db)
):
    try:
        # Parse questions from JSON string
        questions_data = json.loads(questions)
        
        # Create component using template
        component_data = create_component_from_template(
            template_type="request",
            assigned_to=assigned_to,
            description=description,
            task_description=task_description,
            questions=questions_data
        )
        
        # Save to database
        db_component = StrangeMatterComponent(**component_data)
        db.add(db_component)
        db.commit()
        db.refresh(db_component)
        
        return {"success": True, "component_id": db_component.id, "entity_guid": db_component.entity_guid}
    
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid questions format")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# API endpoint to get requests assigned to a specific person
@app.get("/api/requests/{assigned_to}")
async def get_requests_for_person(assigned_to: str, db: Session = Depends(get_db)):
    requests = db.query(StrangeMatterComponent).filter(
        StrangeMatterComponent.assigned_to_identifier == assigned_to,
        StrangeMatterComponent.function.contains("AGM:ENT:SELF")
    ).all()
    
    return [
        {
            "id": req.id,
            "entity_guid": req.entity_guid,
            "name": req.name,
            "description": req.description,
            "task_description": req.task_description,
            "payload": json.loads(req.payload) if req.payload else {},
            "date_created": req.date_created.isoformat()
        }
        for req in requests
    ]

# API endpoint to get a specific request details
@app.get("/api/request/{request_id}")
async def get_request_details(request_id: int, db: Session = Depends(get_db)):
    request = db.query(StrangeMatterComponent).filter(StrangeMatterComponent.id == request_id).first()
    if not request:
        raise HTTPException(status_code=404, detail="Request not found")
    
    return {
        "id": request.id,
        "entity_guid": request.entity_guid,
        "name": request.name,
        "description": request.description,
        "task_description": request.task_description,
        "payload": json.loads(request.payload) if request.payload else {},
        "date_created": request.date_created.isoformat()
    }

# API endpoint to submit response to a request
@app.post("/api/responses")
async def submit_response(
    request_id: int = Form(...),
    author_identifier: str = Form(...),
    answers: str = Form(...),  # JSON string of answers
    db: Session = Depends(get_db)
):
    try:
        # Get original request
        original_request = db.query(StrangeMatterComponent).filter(StrangeMatterComponent.id == request_id).first()
        if not original_request:
            raise HTTPException(status_code=404, detail="Original request not found")
        
        # Parse answers from JSON string
        answers_data = json.loads(answers)
        
        # Create response component using template
        component_data = create_component_from_template(
            template_type="response",
            author_identifier=author_identifier,
            answers=answers_data,
            using_entity_id=original_request.entity_guid
        )
        
        # Save to database
        db_component = StrangeMatterComponent(**component_data)
        db.add(db_component)
        db.commit()
        db.refresh(db_component)
        
        return {"success": True, "component_id": db_component.id, "entity_guid": db_component.entity_guid}
    
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid answers format")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# API endpoint to get all people with assigned requests (for dropdown population)
@app.get("/api/assigned-people")
async def get_assigned_people(db: Session = Depends(get_db)):
    people = db.query(StrangeMatterComponent.assigned_to_identifier).filter(
        StrangeMatterComponent.assigned_to_identifier.isnot(None)
    ).distinct().all()
    
    return [person[0] for person in people if person[0]]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 