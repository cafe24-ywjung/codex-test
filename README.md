# codex-test

This repository contains a minimal skeleton to start a FastAPI project backed by a MySQL database.

## Running the application

Install dependencies and run the server with Uvicorn:

```bash
pip install -r requirements.txt
python -m app.main
```

Update `app/database.py` with your local MySQL credentials before starting. The application exposes a `/items` route that returns all items stored in the database.
