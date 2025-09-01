# fantasy-football

A simple FastAPI application that returns basic JSON responses.

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the development server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

## API Endpoints

- `GET /` - Returns a hello world message
- `GET /health` - Returns health status  
- `GET /data` - Returns sample user data

## Documentation

Once the server is running, visit `http://127.0.0.1:8000/docs` for interactive API documentation.