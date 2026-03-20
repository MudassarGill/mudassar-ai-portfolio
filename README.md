# AI/ML Portfolio Web Application

Welcome to the full-stack portfolio of Mudassar Hussain, an AI/ML Engineer specializing in Deep Learning, NLP, Generative AI, and LLMs.

## Overview
This portfolio seamlessly merges an advanced, futuristic AI-themed frontend with a robust, asynchronous FastAPI backend. The frontend delivers a highly optimized user experience through hardware-accelerated scroll animations, glassmorphism UI traits, and real-time dynamically drawn charting configurations via Chart.js.

The fast, secure python backend controls fetching the CV details & dynamic projects while safely storing form messages received from recruiters directly onto an SQLite database using SQLAlchemy.

## Technologies Used

* **Frontend:**
  * HTML5 Semantic Architecture
  * CSS3 (Glassmorphism, CSS Custom Props, Radial Gradients & Filters, CSS Transform & Opacity Animations)
  * JavaScript (IntersectionObserver API, Fetch API, Chart.js)
  
* **Backend:**
  * Python 3 & FastAPI
  * Uvicorn (ASGI web server)
  * SQLite & SQLAlchemy (ORM structure)
  * Pydantic (Strong type validations)

## Getting Started

To run the application locally, you no longer need to run the HTML page manually. The FastAPI server hosts and dynamically serves the whole web instance alongside its internal network APIs routing requests in real-time.

### Installation

1. Create a secure local environment to house dependencies:
   ```bash
   python -m venv venv
   # On Windows run:
   venv\Scripts\activate
   ```

2. Recursively install all module requirements:
   ```bash
   pip install -r requirements.txt
   ```

3. Change to the backend directory:
   ```bash
   cd backend
   ```

4. Boot the Uvicorn runtime instance to trigger both frontend delivery and API mounts:
   ```bash
   uvicorn main:app --reload
   ```

### Accessing the Web Interface
Simply launch your favorite browser and visit the local network routing link:
```
http://127.0.0.1:8000
```
*Note: Due to the CORS layer definitions setup, ensure you load through 8000.*

## Architecture Logic

* `main.py`: Drives routing parameters utilizing FastAPI. StaticFiles module loads the root HTML into the DOM, securely bridging all `../assets` endpoints.
* `database.py/models.py`: Defines mapping logic to construct local DB data nodes efficiently without migration bloat.
