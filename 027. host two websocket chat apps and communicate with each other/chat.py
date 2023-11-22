import asyncio
import websockets

class WebSocketClient:
    def __init__(self, server_url):
        self.server_url = server_url

    async def connect(self):
        """Used to connect to server using websockets"""
        self.websocket = await websockets.connect(self.server_url)

    async def send_message(self, message):
        """Sends message across the server"""
        if hasattr(self, 'websocket') and self.websocket.open:
            await self.websocket.send(message)
        else:
            print("WebSocket connection is not open.")

    async def receive_message(self):
        """Fetches messages from the server"""
        if hasattr(self, 'websocket') and self.websocket.open:
            message = await self.websocket.recv()
            return message
        else:
            print("WebSocket connection is not open.")

    async def close(self):
        """Closes the websocket connection"""
        if hasattr(self, 'websocket') and self.websocket.open:
            await self.websocket.close()
        else:
            print("WebSocket connection is not open.")

if __name__ == "__main__":
    async def main():
        # Create two instances of WebSocketClient
        client1 = WebSocketClient("ws://localhost:8765")
        client2 = WebSocketClient("ws://localhost:8765")

        # Connect both clients to the WebSocket server
        await client1.connect()
        await client2.connect()

        # Send and receive messages for both clients
        await client1.send_message("Hello from Client 1")
        await client2.send_message("Hello from Client 2")

        message1 = await client1.receive_message()
        message2 = await client2.receive_message()

        print("Client 1 received:", message1)
        print("Client 2 received:", message2)

        # Close the WebSocket connections
        await client1.close()
        await client2.close()

    asyncio.get_event_loop().run_until_complete(main())
