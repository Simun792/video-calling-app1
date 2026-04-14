import sys
from pathlib import Path

from fastapi import FastAPI
from fastapi import WebSocket

from models import Room, User
from websocket import websocket_endpoint

# Allow importing sibling project modules when running from backend/app.
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from database.database import get_connection

app = FastAPI()

active_rooms = {}

@app.post("/register")
def register(user: User):
    db = get_connection()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO users (username, password) VALUES (%s, %s)",
        (user.username, user.password)
    )
    db.commit()
    return {"message": "User registred"}

@app.post("/create-room")
def create_room(room: Room):
    active_rooms[room.room_id] = []
    return {"message": "Room created"}

@app.get("/join-room/{room_id}/{username}")
def join_room(room_id: str, username: str):
    if room_id not in active_rooms:
        return {"error": "Room not fount"}

    active_rooms[room_id].append(username)
    return {"users": active_rooms[room_id]}

@app.websocket("/ws/{room_id}")
async def websocket_route(websocket: WebSocket, room_id: str):
    await websocket_endpoint(websocket, room_id)