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
        {"id": 1, "title": "AMFiller – Automatic Missing Value Filler", "description": "Developed a Python package to automatically detect and handle missing values in structured datasets, reducing manual data cleaning effort by over 40%.", "tech_stack": "Python, Pandas, NumPy, Scikit-learn", "github_link": "https://github.com/MudassarGill", "image_url": "https://images.unsplash.com/photo-1555949963-aa79dcee981c?w=500&q=80"},
        {"id": 2, "title": "Autonomous Drone Detection System", "description": "Built an autonomous drone detection system using deep learning and computer vision techniques for real-time object detection with YOLO.", "tech_stack": "Python, OpenCV, TensorFlow, CNNs", "github_link": "https://github.com/MudassarGill", "image_url": "https://images.unsplash.com/photo-1508614589041-895b88991e3e?w=500&q=80"},
        {"id": 3, "title": "Breast Cancer Prediction Model", "description": "Developed a machine learning model to predict breast cancer diagnoses using clinical datasets, achieving up to 96% accuracy.", "tech_stack": "Python, Scikit-learn, Pandas, Seaborn", "github_link": "https://github.com/MudassarGill", "image_url": "https://images.unsplash.com/photo-1576086213369-97a306d36557?w=500&q=80"},
        {"id": 4, "title": "Sentiment Analysis System", "description": "Developed a sentiment analysis system to classify text reviews into Positive, Negative, and Neutral categories using RNN, LSTM, and GRU models, achieving up to 94% accuracy.", "tech_stack": "Python, NLTK, Scikit-learn, RNN, LSTM, GRU, TF-IDF", "github_link": "https://github.com/MudassarGill", "image_url": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=500&q=80"}
    ]
    return mock_projects
