---
icon: lucide/rocket
---

# FocusFlow

FocusFlow is a FastAPI-based project that demonstrates a clean application structure for building a focus training system. The repository is designed to be extended with additional services, database models, and deployment workflows.

## Overview

This project includes:

- a FastAPI application entry point in [app/main.py](../app/main.py)
- centralized settings in [app/core/config.py](../app/core/config.py)
- versioned API routing in [app/api/v1/router.py](../app/api/v1/router.py)
- centralized exception handling in [app/exceptions/handlers.py](../app/exceptions/handlers.py)

## Project structure

```text
app/
  api/v1/
  core/
  db/
  exceptions/
  middleware/
  models/
  repositories/
  schemas/
  services/
  utils/
tests/
```

## Quick start

1. Create and activate a virtual environment.
2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the development server:

   ```bash
   uvicorn app.main:app --reload
   ```

4. Open the API documentation at:
   - http://localhost:8000/docs
   - http://localhost:8000/health

## API endpoints

- GET / returns a welcome message
- GET /health returns the service health status

## Notes

The application is intentionally organized into clear layers so it can grow into a more complete backend service with authentication, persistence, and deployment automation.
