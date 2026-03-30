import cv2
import os
from datetime import datetime

# folder_name = "motion_screenshots"
# os.makedirs(folder_name, exist_ok=True)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera could not be opened")
    exit()

ret, prev_frame = cap.read()
if not ret:
    print("Could not read first frame")
    cap.release()
    exit()

prev_frame = cv2.flip(prev_frame, 1)
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
prev_gray = cv2.GaussianBlur(prev_gray, (11, 11), 0)

print("Press Q to quit")
print("Press S to save screenshot")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Could not read frame")
        break

    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (11, 11), 0)

    diff = cv2.absdiff(prev_gray, gray)

    # lower threshold = more sensitive
    _, thresh = cv2.threshold(diff, 15, 255, cv2.THRESH_BINARY)

    thresh = cv2.dilate(thresh, None, iterations=2)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    motion_detected = False

    for contour in contours:
        # smaller area = more sensitive
        if cv2.contourArea(contour) < 500:
            continue

        motion_detected = True
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "Motion Detected", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    if motion_detected:
        cv2.putText(frame, "Status: Motion", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    else:
        cv2.putText(frame, "Status: No Motion", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    cv2.imshow("Motion Detector", frame)
    cv2.imshow("Threshold", thresh)

    key = cv2.waitKey(30) & 0xFF

    if key == ord('q'):
        break
    elif key == ord('s'):
        file_name = datetime.now().strftime("screenshot_%Y%m%d_%H%M%S.png")
        file_path = os.path.join(folder_name, file_name)
        cv2.imwrite(file_path, frame)
        print("Screenshot saved:", file_path)

    prev_gray = gray.copy()

cap.release()
cv2.destroyAllWindows()