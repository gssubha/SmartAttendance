import face_recognition
import os
import cv2

def load_known_faces(images_path='images'):
    known_encodings = []
    known_names = []

    if not os.path.exists(images_path):
        print(f"[ERROR] Folder '{images_path}' does not exist.")
        return known_encodings, known_names

    for person_name in os.listdir(images_path):
        person_folder = os.path.join(images_path, person_name)
        if not os.path.isdir(person_folder):
            continue

        for img_name in os.listdir(person_folder):
            img_path = os.path.join(person_folder, img_name)
            img = cv2.imread(img_path)

            if img is None:
                print(f"[WARNING] Unable to read image: {img_path}")
                continue

            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            face_locations = face_recognition.face_locations(rgb_img)
            encodings = face_recognition.face_encodings(rgb_img, face_locations)

            if len(encodings) > 0:
                known_encodings.append(encodings[0])
                known_names.append(person_name)
            else:
                print(f"[WARNING] No face found in {img_path}")

    print(f"[INFO] Loaded {len(known_encodings)} valid face encodings.")
    return known_encodings, known_names
