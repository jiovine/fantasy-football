from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World", "status": "success"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "FastAPI Application"}

@app.get("/data")
def get_data():
    return {
        "users": [
            {"id": 1, "name": "John Doe", "email": "john@example.com"},
            {"id": 2, "name": "Jane Smith", "email": "jane@example.com"}
        ],
        "total": 2
    }