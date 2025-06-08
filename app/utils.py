import uuid
import json
import hashlib
from datetime import datetime
from typing import Dict, Any, List

def generate_unique_ids():
    """Generate unique GUIDs for StrangeMatter components"""
    return {
        "entity_guid": str(uuid.uuid4()),
        "component_guid": str(uuid.uuid4()),
        "component_version_guid": str(uuid.uuid4())
    }

def calculate_md5_hash(data: str) -> str:
    """Calculate MD5 hash of payload data"""
    return hashlib.md5(data.encode()).hexdigest()

def create_component_from_template(template_type: str, **kwargs) -> Dict[str, Any]:
    """Create a StrangeMatter component based on the template type"""
    
    # Generate unique identifiers
    ids = generate_unique_ids()
    current_time = datetime.now().isoformat()
    
    if template_type == "request":
        # Create request component
        assigned_to = kwargs.get("assigned_to")
        description = kwargs.get("description")
        task_description = kwargs.get("task_description")
        questions = kwargs.get("questions", [])
        
        # Create payload
        payload_data = {
            "instructions": description,
            "taskDescription": task_description,
            "questions": questions
        }
        
        payload_json = json.dumps(payload_data)
        payload_hash = calculate_md5_hash(payload_json)
        
        return {
            "component_type": "https://github.com/HOKGroup/hok_strangematter_components/DataCollectionComponents/hok.projectdata.request.dynamic.json",
            "component_hash": "",
            "author_identifier": kwargs.get("author_identifier", "system@datacollection.app"),
            "assigned_to_identifier": assigned_to,
            "context": ".../hok/?projectname=DataCollection&projectnumber=DEMO",
            "used_as_a": "Instance",
            "using": [],
            "function": ["AGM:ENT:SELF"],
            "component_classification_value": "hok.projectdata.request.dynamic",
            "component_classification_uri": "",
            "entity_guid": ids["entity_guid"],
            "component_guid": ids["component_guid"],
            "component_version_guid": ids["component_version_guid"],
            "date_created": datetime.now(),
            "last_modified": datetime.now(),
            "name": f"Data Request - {task_description[:50]}...",
            "description": description,
            "task_description": task_description,
            "hash_definition": "MD5",
            "payload_hash": payload_hash,
            "payload_data_type": "json",
            "payload_schema": {
                "$schema": "http://json-schema.org/draft-07/schema#",
                "type": "object",
                "properties": {
                    "instructions": {"type": "string"},
                    "taskDescription": {"type": "string"},
                    "questions": {"type": "array"}
                }
            },
            "payload": payload_json
        }
    
    elif template_type == "response":
        # Create response component
        author_identifier = kwargs.get("author_identifier")
        answers = kwargs.get("answers", {})
        using_entity_id = kwargs.get("using_entity_id")
        
        payload_json = json.dumps(answers)
        payload_hash = calculate_md5_hash(payload_json)
        
        return {
            "component_type": "https://github.com/HOKGroup/hok_strangematter_components/DataCollectionComponents/hok.projectdata.dynamic.json",
            "component_hash": "",
            "author_identifier": author_identifier,
            "assigned_to_identifier": None,
            "context": ".../hok/?projectname=DataCollection&projectnumber=DEMO",
            "used_as_a": "Instance",
            "using": [using_entity_id] if using_entity_id else [],
            "function": ["Response"],
            "component_classification_value": "hok.projectdata.dynamic",
            "component_classification_uri": "",
            "entity_guid": ids["entity_guid"],
            "component_guid": ids["component_guid"],
            "component_version_guid": ids["component_version_guid"],
            "date_created": datetime.now(),
            "last_modified": datetime.now(),
            "name": f"Data Response - {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            "description": "Response to data collection request",
            "task_description": "Data collection response",
            "hash_definition": "MD5",
            "payload_hash": payload_hash,
            "payload_data_type": "json",
            "payload_schema": {
                "$schema": "http://json-schema.org/draft-07/schema#",
                "type": "object",
                "additionalProperties": {"type": ["string", "number", "boolean", "object", "array", "null"]}
            },
            "payload": payload_json
        }
    
    else:
        raise ValueError(f"Unknown template type: {template_type}") 