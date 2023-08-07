import asyncio
from websockets.server import serve

async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)

async def main():
    async with serve(echo, "192.168.0.109", 8002):
        await asyncio.Future()

asyncio.run(main())
