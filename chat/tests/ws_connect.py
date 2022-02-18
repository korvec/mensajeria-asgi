import asyncio
import websockets
import json

url = "ws://127.0.0.1:8000/ws/socket-server/"
async def connection():
    async with websockets.connect(url) as ws:
        data = await ws.recv()
        data = json.loads(data)
        return data
