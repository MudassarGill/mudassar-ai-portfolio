from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class MessageCreate(BaseModel):
    name: str
    email: EmailStr
    message: str

class MessageResponse(BaseModel):
    id: int
    name: str
    email: str
    message: str
    created_at: datetime

    class Config:
        from_attributes = True

class ProjectResponse(BaseModel):
    id: int
    title: str
    description: str
    tech_stack: str
    github_link: str
    image_url: Optional[str] = None

    class Config:
        from_attributes = True
