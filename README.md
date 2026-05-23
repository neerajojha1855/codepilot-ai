# CodePilot 🚀
**AI-Powered Code Review Platform**

CodePilot is an intelligent code review assistant that automatically analyzes your GitHub repositories to detect bugs, security vulnerabilities, code smells, and performance issues using advanced Large Language Models.

![CodePilot Logo](./static/favicon.svg)

---

## 🎯 Features

- **Automated Repository Scanning:** Just paste a GitHub URL, and CodePilot will fetch the code automatically using the GitHub API.
- **Real AI Code Analysis:** Powered by the brand new **Google Gemini 2.0 Flash SDK** (`google-genai`), CodePilot understands the exact context and semantics of your code to spot complex vulnerabilities.
- **Asynchronous Background Processing:** Built with `django-q2`, ensuring the UI remains lightning-fast while the AI crunches through large repositories in the background.
- **Beautiful & Dynamic UI:** Built with **Tailwind CSS v4**, featuring real-time status badges, custom SVG iconography, and glassmorphic design elements.
- **Production Ready:** Pre-configured for deployment on **Render.com** with PostgreSQL, Gunicorn, and Whitenoise static file delivery.

---

## 🏗️ Architecture

- **Backend:** Django (Python 3.12)
- **Database:** PostgreSQL (Production via `dj_database_url`) / SQLite (Local)
- **AI Engine:** Google Gemini (`gemini-2.0-flash` & `gemini-1.5-flash`)
- **Task Queue:** Django Q2 (using ORM Broker)
- **Frontend:** HTML5, Tailwind CSS v4 (Compiled Locally)

---

## ⚙️ Quick Start (Local Development)

### 1. Clone the repository
```bash
git clone https://github.com/neerajojha1855/codepilot-ai.git
cd codepilot-ai
```

### 2. Set up the Environment
Create a `.env` file in the root directory:
```env
# Required AI Key
GEMINI_API_KEY=your_gemini_api_key_here

# Django Security Settings
SECRET_KEY=your_local_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

### 3. Install Dependencies
```bash
python -m venv venv
source venv/Scripts/activate  # On Windows
pip install -r requirements.txt
```

### 4. Build Tailwind CSS
```bash
python manage.py tailwind install
python manage.py tailwind build
```

### 5. Run the Servers
You will need **two terminal windows**.

**Terminal 1 (Web Server):**
```bash
python manage.py migrate
python manage.py runserver
```

**Terminal 2 (Background AI Worker):**
```bash
python manage.py qcluster
```

Now open `http://127.0.0.1:8000/` and start analyzing code!

---

## 🚀 Deployment (Render.com)

CodePilot is fully configured for deployment on Render. Here is how to set it up manually:

1. **Push to GitHub**: Push your local repository to a new GitHub repository.
2. **Create Database**: On Render, create a new **PostgreSQL** database. Copy the "Internal Database URL".
3. **Create Web Service**: 
   - Create a new **Web Service** connected to your GitHub repo.
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn CodePilot.wsgi:application`
   - Add Environment Variables:
     - `PYTHON_VERSION`: `3.12.0`
     - `DATABASE_URL`: *(Paste the Internal Database URL)*
     - `SECRET_KEY`: *(Generate a random string)*
     - `DEBUG`: `False`
     - `ALLOWED_HOSTS`: `.onrender.com`
     - `GEMINI_API_KEY`: *(Your Google AI Studio Key)*
4. **Create Background Worker**:
   - Create a new **Background Worker** connected to the same repo.
   - **Build Command**: `./build.sh`
   - **Start Command**: `python manage.py qcluster`
   - Link all the exact same environment variables as above!

---

## 🗄️ Database Models
- **Repository:** Tracks the GitHub URL, owner, name, and scan status (`PENDING`, `ANALYZING`, `COMPLETED`, `FAILED`).
- **FileAnalysis:** Stores quality and risk scores for individual files.
- **Vulnerability:** Tracks security flaws, their severity, and proposed fixes.
- **ReviewComment:** Stores AI-generated code smells and optimization recommendations.