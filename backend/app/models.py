from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str

class Room(BaseModel):
    room_id: str