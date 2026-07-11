# focusflow
---
##### **Introduction**

Build, containerize, deploy, and secure a FastAPI application on Kubernetes using HashiCorp Vault AppRole with a Vault Agent sidecar.

---

## Project Setup 

Goal: Create a simple FastAPI application with a clean structure that we'll extend throughout the course.

**Prerequisites:**
Install:

- Python 3.12+
- Git
- VS Code
- Docker Desktop (or Docker Engine)
- PostgreSQL (or we'll use Docker later)

#### Step 1: Create the project

```bash
mkdir focusflow
cd focusflow
```

**Create the virtual environment:**

```bash
python -m venv .venv

```
Activate it:

**Linux/MacOS**

```bash
<> Bash
source .venv/bin/activate
```

**Windows(Powershell)**

```powershell
<> Powershell
.venv\Scripts\Activate.ps1
```
Upgrade pip:

```bash
<> Bash
python -m pip install --upgrade pip
```


---

#### Step 2: Step 2: Install dependencies

```bash
pip install fastapi uvicorn pydantic pydantic-settings
```

Save them:

```bash
pip freeze > requirements.txt
```
---

#### Step 3: Create the directory structure

```bash
focusflow/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── repositories/
│   ├── api/
│   └── utils/
├── requirements.txt
└── .gitignore

```
Create the folders:

```bash
mkdir -p app/{api,config,models,repositories,schemas,services,utils}
touch app/__init__.py

```

(If you're on Windows without mkdir -p, you can create them manually in VS Code.)

---

#### Step 4: Create the first API

*app/main.py*

```python
<> Python

from fastapi import FastAPI

app = FastAPI(
    title="FocusFlow API",
    version="1.0.0",
    description="Focus Training System"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to FocusFlow"
    }

@app.get("/health")
def health():
    return {
        "status": "UP"
    }

```

---

#### Step 5: Run the application

```bash
uvicorn app.main:app --reload
```
Open:

- http://localhost:8000
- http://localhost:8000/health
- http://localhost:8000/docs


You should see Swagger UI at /docs.



