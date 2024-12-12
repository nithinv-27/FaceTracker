import cv2

cap = cv2.VideoCapture(0)
cap.open(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    success, frame = cap.read()

    if not success:
        print("Cannot receive frame")
        break

    cv2.imshow("Recording", frame)
    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()