# codex-test

This repository contains a minimal skeleton to start a FastAPI project.

## Running the application

Install dependencies and run the server with Uvicorn:

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The application exposes a single `/` route that returns a simple JSON greeting.
