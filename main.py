from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.get('/')
def home():
    return{"suc":"ces"}

@app.websocket("/ws")
async def receive_video(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_bytes()
        await websocket.send_bytes(data)