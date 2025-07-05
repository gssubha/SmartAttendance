import cv2
import face_recognition
import numpy as np
from face_recognition_module import load_known_faces
from mark_attendance import mark_attendance

# Load known face encodings and names
known_encodings, known_names = load_known_faces()

video = cv2.VideoCapture(0)
print("[INFO] Camera started. Press 'q' to quit.")

while True:
    ret, frame = video.read()
    if not ret:
        print("[ERROR] Failed to capture frame from camera.")
        break

    # Resize frame for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Detect faces and get encodings
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    print(f"[INFO] Found {len(face_locations)} face(s)")

    for i, face_encoding in enumerate(face_encodings):
        name = "Unknown"

        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        face_distances = face_recognition.face_distance(known_encodings, face_encoding)

        if len(face_distances) > 0:
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_names[best_match_index]
                mark_attendance(name)

        # Scale back face location to original size
        top, right, bottom, left = face_locations[i]
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw rectangle and name
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 255, 0), cv2.FILLED)
        cv2.putText(frame, name, (left + 6, bottom - 6),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow("Face Recognition - Press 'q' to Quit", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close windows
video.release()
cv2.destroyAllWindows()
