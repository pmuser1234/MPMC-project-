import cv2
import pytesseract
# Replace the URL with your ESP-CAM stream URL
url = "http://192.168.137.52:81/stream"

cap = cv2.VideoCapture(url)

if not cap.isOpened():
    print("Error: Could not open video stream")
else:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame")
            break
        # Process the frame as needed
        cv2.imshow("Video Stream", frame)
        img1=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        text=pytesseract.image_to_string(img1)
        print(text)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
