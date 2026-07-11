# focusflow
---
##### **Introduction**

Build, containerize, deploy, and secure a FastAPI application on Kubernetes using HashiCorp Vault AppRole with a Vault Agent sidecar.

---

## Final Project Structure

```python
focusflow/
│
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── router.py
│   │       ├── health.py
│   │       ├── users.py
│   │       └── tasks.py
│   │
│   ├── core/
│   │       config.py
│   │       logger.py
│   │       security.py
│   │
│   ├── db/
│   │
│   ├── middleware/
│   │
│   ├── exceptions/
│   │
│   ├── models/
│   │
│   ├── repositories/
│   │
│   ├── schemas/
│   │
│   ├── services/
│   │
│   ├── utils/
│   │
│   ├── main.py
│   │
│   └── __init__.py
│
├── tests/
│
├── .env
│
├── requirements.txt
│
└── README.md

```


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

---

#### Step 6: Add configuration with Pydantic

Create *app/core/config.py:*

```python
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str = "FocusFlow"

    VERSION: str = "1.0"

    API_PREFIX: str = "/api/v1"

    DEBUG: bool = True

    class Config:
        env_file = ".env"


settings = Settings()
```

Update *app/main.py:*

```python
from fastapi import FastAPI
from app.config.settings import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version
)
```
This introduces centralized configuration. Later, Vault will provide secrets that these settings depend on.

---

#### Step 7: Initialize Git

```bash
git init
```

Create .gitignore

```bash
.venv/
__pycache__/
*.pyc
.env
```

Commit your work:

```git
git add .
git commit -m "Initial FastAPI project setup"
```







