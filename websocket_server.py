# import asyncio
# import websockets

# async def echo(websocket, path):
#     print("Client connected")
#     try:
#         async for message in websocket:
#             print(f"Received: {message}")
#             await websocket.send(f"Echo: {message}")
#     except websockets.ConnectionClosed:
#         print("Client disconnected")

# start_server = websockets.serve(echo, "0.0.0.0", 8765)

# asyncio.get_event_loop().run_until_complete(start_server)
# print("WebSocket server started on port 8765")
# asyncio.get_event_loop().run_forever()

import asyncio
import websockets

# CORS Headers
extra_headers = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type"
}

# WebSocket handler
async def echo(websocket, path):
    print("Client connected")
    try:
        async for message in websocket:
            print(f"Received: {message}")
            await websocket.send(f"Echo: {message}")
    except websockets.ConnectionClosed as e:
        print(f"Client disconnected: {e}")

# Start the WebSocket server
start_server = websockets.serve(
    echo,
    "0.0.0.0",  # Listen on all available interfaces
    8765,       # Port number
    ping_interval=None,
    ping_timeout=None,
    extra_headers=extra_headers
)

print("WebSocket server started on port 8765")

# Run the WebSocket server event loop
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

