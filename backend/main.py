from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
import sys, os

# Ensure the backend directory is in the system path so Render can find the modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

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
        {"id": 4, "title": "Sentiment Analysis System", "description": "Developed a sentiment analysis system to classify text reviews into Positive, Negative, and Neutral categories using RNN, LSTM, and GRU models, achieving up to 94% accuracy.", "tech_stack": "Python, NLTK, Scikit-learn, RNN, LSTM, GRU", "github_link": "https://github.com/MudassarGill", "image_url": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=500&q=80"},
        {"id": 5, "title": "AutoPX Library", "description": "High-performance Python ML preprocessing library for automated scalable pipelines.", "tech_stack": "Python, Pandas, Scikit-learn", "github_link": "https://github.com/MudassarGill", "image_url": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=500&q=80"},
        {"id": 6, "title": "PreMLCheck Library", "description": "Machine learning preprocessing library and feature engineering support.", "tech_stack": "Python, Scikit-learn", "github_link": "https://github.com/MudassarGill", "image_url": "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=500&q=80"},
        {"id": 7, "title": "PyMessenger", "description": "A lightweight web-based messenger where users can send and receive messages, with file-based storage and logging, built with Python FastAPI and a frontend in HTML/CSS/JS.", "tech_stack": "FastAPI, HTML/CSS/JS, Python", "github_link": "https://github.com/MudassarGill", "image_url": "https://images.unsplash.com/photo-1611162617474-5b21e879e113?w=500&q=80"},
        {"id": 8, "title": "Personal Expense Tracker", "description": "Dynamic web application for tracking finances and managing personal expenses with secure data storage and insightful visualizations.", "tech_stack": "Python, FastAPI", "github_link": "https://github.com/MudassarGill", "image_url": "https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?w=500&q=80"},
        {"id": 9, "title": "Product Review Intelligence System", "description": "Intelligent system to analyze e-commerce product reviews, extract sentiments, and provide actionable insights using LLMs and NLP.", "tech_stack": "Python, NLP, LLMs", "github_link": "https://github.com/MudassarGill", "image_url": "https://images.unsplash.com/photo-1563986768609-322da13575f3?w=500&q=80"},
        {"id": 10, "title": "AutoML Datalab", "description": "Interactive platform where users upload datasets, and the system autonomously cleans data, detects problem types, and offers options to either download the refined data or train custom models directly.", "tech_stack": "Python, Pandas, Scikit-learn, Web Framework", "github_link": "https://github.com/MudassarGill", "image_url": "https://images.unsplash.com/photo-1555949963-aa79dcee981c?w=500&q=80"}
    ]
    return mock_projects

@app.get("/api/messages")
def get_all_messages(db: Session = Depends(get_db)):
    """Fetch all recruiter contact messages submitted through the portfolio."""
    return db.query(models.Message).all()

# Mount Static Files (Must be at the bottom so it doesn't override API routes)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")
IMAGES_DIR = os.path.join(BASE_DIR, "images")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

# Serve images and assets directories if they exist
if os.path.exists(IMAGES_DIR):
    app.mount("/images", StaticFiles(directory=IMAGES_DIR), name="images")
if os.path.exists(ASSETS_DIR):
    app.mount("/assets", StaticFiles(directory=ASSETS_DIR), name="assets")

# Serve the frontend (index.html, style.css, script.js) at the root "/"
if os.path.exists(FRONTEND_DIR):
    app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")
