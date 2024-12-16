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

stream_active = True

def generate():
    global stream_active, cap
    while stream_active:
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


@app.get('/')
def home():
    return {"suc":"ces"}

@app.get("/capture")
def capture():
    global stream_active, cap
    stream_active = True
    cap = cv2.VideoCapture(0)  # Reinitialize the camera
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    return StreamingResponse(generate(), media_type="multipart/x-mixed-replace;boundary=frame")

@app.post("/stop")
def stop_capture():
    global stream_active, cap
    stream_active = False
    cap.release()
    # generate(isStreaming=False)
    return {"st":"op"}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)



# @app.websocket("/ws")
# async def receive_video(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         data = await websocket.receive_bytes()
#         await websocket.send_bytes(data)
