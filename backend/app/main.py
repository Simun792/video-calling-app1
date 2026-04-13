from fastapi import FastAPI

app = FastAPI()

active_rooms = {}

@app.get("/")
def home():
    return {"message": "Video Call API running" }


