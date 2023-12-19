import asyncio
import websockets
from datetime import datetime as dt
import os
import json
import time

async def client():
    uri = "ws://server:8765"

    async with websockets.connect(uri) as websocket:
        
        # Send a message to the server
        message = {
            "message": "Ping!",
            "client_name": os.environ.get('CLIENT_NAME', "anonymous")
        }
        
        while True:
            await websocket.send(json.dumps(message))

            # Receive and print the response from the server
            response = await websocket.recv()
            print(f"\033[93;1m[{dt.now().strftime('%d-%m-%Y %H:%M:%S')}]\033[0m Received from \033[31;1m server\033[0m:", response)
        
            time.sleep(int(os.environ.get("LAG_TIME", 1)))

asyncio.get_event_loop().run_until_complete(client())
