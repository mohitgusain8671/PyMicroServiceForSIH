# app/main.py
from fastapi import FastAPI
from .routes import prediction

app = FastAPI()

# Include your routes
app.include_router(prediction.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI microservice"}
