import asyncio
import websockets
import time
from datetime import datetime as dt
import json

def log_data(filename, data):
    try:
        with open(filename, 'a') as file:
            file.write(data + '\n')
        print("Data logged successfully.")
    except Exception as e:
        print(f"Error logging data: {str(e)}")

async def server(websocket, path):
    print("Server Started ...")
    try:
        async for message in websocket:
            message = json.loads(message)
            print(f"\033[93;1m[{dt.now().strftime('%d-%m-%Y %H:%M:%S')}]\033[0m Recieved from \033[36;1m client ({message['client_name']})\033[0m: " + message["message"])
            
            # log request data from the clients
            log_data(
                'server_logs.txt', 
                f"[{dt.now().strftime('%d-%m-%Y %H:%M:%S')}] Recieved from client ({message['client_name']}): " + message["message"]
            )
            
            # simulating server response time lag
            time.sleep(1)
            
            await websocket.send("Pong!")
    except websockets.exceptions.ConnectionClosedOK:
        print("Client disconnected")

start_server = websockets.serve(server, "0.0.0.0", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()