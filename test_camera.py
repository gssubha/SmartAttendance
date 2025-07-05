import cv2

for i in range(5):
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"Camera opened at index {i}")
        ret, frame = cap.read()
        if ret:
            cv2.imshow(f'Camera Index {i}', frame)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        cap.release()
