from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import cv2

app = FastAPI()

origins = [
    "http://127.0.0.1:5500",  # Replace with the frontend URL if different
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow only these origins, or use "*" to allow all
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

isStreaming = False
cap = None

def generate():
    global isStreaming, cap
    while isStreaming:
        success, frame = cap.read()

        if not success:
            print("Cannot receive frame")
            break

        detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        faces = detector.detectMultiScale(frame, 1.1, 7)

        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()
    cv2.destroyAllWindows()


@app.get('/')
def home():
    return {"suc":"ces"}

@app.get("/capture")
def capture():
    global isStreaming, cap
    if cap is None or not cap.isOpened():
        cap = cv2.VideoCapture(0)  # Reinitialize the camera
        if not cap.isOpened():
            print("Cannot open camera")
            return {"error": "Cannot open camera"}
    isStreaming = True
    return StreamingResponse(generate(), media_type="multipart/x-mixed-replace;boundary=frame")

@app.get("/stop_capture")
def stop_capture():
    global isStreaming
    isStreaming = False
    return {"st":"op"}




# @app.websocket("/ws")
# async def receive_video(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         data = await websocket.receive_bytes()
#         await websocket.send_bytes(data)
