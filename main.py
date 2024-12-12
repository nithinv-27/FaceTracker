from fastapi import FastAPI, WebSocket
from fastapi.responses import StreamingResponse
import cv2

app = FastAPI()

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

def generate():
    while True:
        success, frame = cap.read()

        if not success:
            print("Cannot receive frame")
            break

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.get('/')
def home():
    return {"suc":"ces"}

@app.get("/capture")
def capture():
    return StreamingResponse(generate(), media_type="multipart/x-mixed-replace;boundary=frame")





# @app.websocket("/ws")
# async def receive_video(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         data = await websocket.receive_bytes()
#         await websocket.send_bytes(data)
