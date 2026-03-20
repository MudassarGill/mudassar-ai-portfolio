from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from database import Base

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    message = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    tech_stack = Column(String)
    github_link = Column(String)
    image_url = Column(String)
