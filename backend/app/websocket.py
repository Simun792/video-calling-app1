import socket
from sqlite3 import connect
from fastapi import WebSocket

connections = {}

async def websocket_endpoint(websocket: WebSocket, room_id: str):
    await websocket.accept()

    if room_id not in connections:
        connections[room_id] = []

    connections[room_id].append(websocket)

    try:
        while True:
            data = await websocket.receive_text()


            for conn in connections[room_id]:
                if conn != websocket:
                    await conn.send_text(data)

    except:
        connections[room_id].remove(websocket)  


