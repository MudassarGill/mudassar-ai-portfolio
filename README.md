<div align="center">
  <img src="https://img.shields.io/badge/Mudassar_Hussain-AI%2FML_Engineer-00f0ff?style=for-the-badge&logoColor=white" alt="AI/ML Engineer" />
</div>

<h1 align="center">🚀 Mudassar's AI/ML Full-Stack Portfolio</h1>

<p align="center">
  <b>A highly-interactive, full-stack professional portfolio demonstrating expertise in Deep Learning, Generative AI, MLOps, and NLP architectures.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white" />
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white" />
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black" />
</p>

---

## 🌟 Overview
This portfolio seamlessly merges an advanced, futuristic AI-themed frontend with a robust, asynchronous **FastAPI** backend. 

* 🎨 **Frontend**: Features hardware-accelerated scroll animations, glassmorphism UI, real-time dynamically drawn custom progress bars, and high-fidelity AI CPU/Circuit backgrounds.
* ⚙️ **Backend**: A fast, secure Python backend serving dynamic projects and securely storing recruiter contact messages into an **SQLite** database via SQLAlchemy.

---

## 🏗️ Architecture Stack

```text
mudassar-ai-portfolio/
├── backend/
│   ├── database.py     # SQLite Database setup
│   ├── main.py         # FastAPI Root & StaticFiles Mounting
│   ├── models.py       # SQLAlchemy ORM Models
│   └── schemas.py      # Pydantic Schemas for Validation
├── frontend/
│   ├── index.html      # Main Structural DOM
│   ├── script.js       # Scroll Animations, Fetching, Dynamic Counters
│   └── style.css       # Glassmorphism, Theme Variables
├── images/             # Profile & Asset Images
├── README.md           # Documentation
└── requirements.txt    # Python Dependencies
```


## 💻 Getting Started (Local Development)

To run the application locally, you do not need to boot the HTML and Backend separately. The FastAPI server hosts and delivers the entire web ecosystem seamlessly!

1. **Activate your environment** (Optional but recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
2. **Install all required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Boot the Backend Server**:
   ```bash
   cd backend
   uvicorn main:app --reload
   ```
4. **Access the Website**: Open your web browser and navigate to:
   👉 **`http://127.0.0.1:8000`**

---

## 🌐 Making it Live (Global & Mobile Access)

### 1. View on your Mobile Phone instantly (Local Wi-Fi) 📱
Want to test the website on your phone right now? Make sure your laptop and phone are on the **same Wi-Fi network**. Run this command instead:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```
Then, open Chrome/Safari on your phone and type in your laptop's Wi-Fi IP address followed by the port (e.g., `http://192.168.1.15:8000`).

### 2. Deploy to the Global Internet (Available 24/7) 🌍
To make your portfolio permanently available for recruiters to visit worldwide via a custom link, you need a free cloud hosting service:
1. **GitHub Upload**: Push this entire project folder to a repository on GitHub.
2. **Hosting with Render.com** (Recommended Free Flow):
   * Create an account on **Render.com**.
   * Select **"New Web Service"** and connect your GitHub repo.
   * Render will automatically install your `requirements.txt` and you simply set the start command to: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
3. **Result**: You will get a completely free live URL (e.g., `mudassar-ai-portfolio.onrender.com`) that you can put right on your resume!

---

<p align="center">Built by <b>Mudassar Hussain</b></p>
