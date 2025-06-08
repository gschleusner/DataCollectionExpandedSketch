from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from datetime import datetime

class ComponentBase(BaseModel):
    component_type: str
    author_identifier: Optional[str] = None
    assigned_to_identifier: Optional[str] = None
    context: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    task_description: Optional[str] = None

class ComponentCreate(ComponentBase):
    payload: Dict[Any, Any]

class ComponentResponse(ComponentBase):
    id: int
    entity_guid: str
    component_guid: str
    component_version_guid: str
    date_created: datetime
    last_modified: datetime
    payload: Optional[Dict[Any, Any]] = None
    
    class Config:
        from_attributes = True

class RequestCreate(BaseModel):
    assigned_to: str
    description: str
    task_description: str
    questions: List[Dict[str, str]]

class ResponseCreate(BaseModel):
    request_id: int
    author_identifier: str
    answers: Dict[str, Any] 