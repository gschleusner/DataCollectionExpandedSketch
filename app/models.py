from sqlalchemy import Column, Integer, String, Text, DateTime, JSON
from sqlalchemy.sql import func
from database import Base

class StrangeMatterComponent(Base):
    __tablename__ = "strange_matter_components"

    # Primary key
    id = Column(Integer, primary_key=True, index=True)
    
    # StrangeMatter Schema Fields
    component_type = Column(String, index=True)
    component_hash = Column(String)
    author_identifier = Column(String)
    assigned_to_identifier = Column(String, index=True)  # For querying requests by person
    context = Column(String)
    used_as_a = Column(String, default="Instance")
    using = Column(JSON)  # Array of references
    function = Column(JSON)  # Array of function identifiers
    
    # Component Classification
    component_classification_value = Column(String, index=True)
    component_classification_uri = Column(String)
    
    # Unique Identifiers
    entity_guid = Column(String, unique=True, index=True)
    component_guid = Column(String, unique=True, index=True)
    component_version_guid = Column(String, unique=True, index=True)
    
    # Timestamps
    date_created = Column(DateTime, default=func.now())
    last_modified = Column(DateTime, default=func.now(), onupdate=func.now())
    
    # Name and Description
    name = Column(String)
    description = Column(Text)
    task_description = Column(Text)
    
    # Hash and Payload
    hash_definition = Column(String, default="MD5")
    payload_hash = Column(String)
    payload_data_type = Column(String, default="json")
    payload_schema = Column(JSON)
    payload = Column(Text)  # JSON string of the actual payload data 