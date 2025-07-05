import cv2
import os

def capture_face_images(student_name):
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Capturing - Press 'q' to Quit")

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    student_folder = f"images/{student_name}"
    os.makedirs(student_folder, exist_ok=True)

    count = 0
    while True:
        ret, frame = cam.read()
        if not ret:
            print("Failed to grab frame")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        for (x, y, w, h) in faces:
            # Add margin around face
            margin = 40
            x1 = max(0, x - margin)
            y1 = max(0, y - margin)
            x2 = min(frame.shape[1], x + w + margin)
            y2 = min(frame.shape[0], y + h + margin)

            roi = frame[y1:y2, x1:x2]
            img_path = f"{student_folder}/{student_name}_{count}.jpg"
            cv2.imwrite(img_path, roi)
            count += 1

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        cv2.imshow("Capturing - Press 'q' to Quit", frame)

        if cv2.waitKey(1) & 0xFF == ord('q') or count >= 10:
            break

    cam.release()
    cv2.destroyAllWindows()
    print(f"[INFO] Saved {count} face images to {student_folder}")

# Entry point
if __name__ == "__main__":
    name = input("Enter Student Name: ").strip().replace(" ", "_")
    capture_face_images(name)
