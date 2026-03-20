from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models, schemas
from database import engine, get_db
from typing import List

# Create DB tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mudassar Hussain Portfolio API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/contact", response_model=schemas.MessageResponse)
def create_message(message: schemas.MessageCreate, db: Session = Depends(get_db)):
    db_message = models.Message(**message.dict())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

@app.get("/projects", response_model=List[schemas.ProjectResponse])
def get_projects(db: Session = Depends(get_db)):
    # In a real app, projects would be fetched from DB. Here we return hardcoded mock data.
    mock_projects = [
        {"id": 1, "title": "AMFiller", "description": "Data cleaning automation library with robust null-filling strategies.", "tech_stack": "Python, Pandas", "github_link": "https://github.com/MudassarGill", "image_url": "https://images.unsplash.com/photo-1555949963-aa79dcee981c?w=500&q=80"},
        {"id": 2, "title": "PreMLCheck", "description": "Machine learning preprocessing library and feature engineering support.", "tech_stack": "Python, Scikit-learn", "github_link": "https://github.com/MudassarGill", "image_url": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=500&q=80"},
        {"id": 3, "title": "PyMessenger System", "description": "WhatsApp-like messaging backend using FastAPI for real-time communication.", "tech_stack": "FastAPI, WebSockets", "github_link": "https://github.com/MudassarGill", "image_url": "https://images.unsplash.com/photo-1611162617474-5b21e879e113?w=500&q=80"},
        {"id": 4, "title": "Intelligent AI System", "description": "End-to-end AI product with decision-making capabilities and real-world workflow integration.", "tech_stack": "Python, PyTorch", "github_link": "https://github.com/MudassarGill", "image_url": "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=500&q=80"},
        {"id": 5, "title": "Personal E-Learning System", "description": "Assignment and learning platform with student management and backend-driven architecture.", "tech_stack": "FastAPI, HTML/CSS/JS", "github_link": "https://github.com/MudassarGill", "image_url": "https://images.unsplash.com/photo-1501504905252-473c47e087f8?w=500&q=80"}
    ]
    return mock_projects
