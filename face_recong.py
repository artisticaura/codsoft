import cv2
import face_recognition
import numpy as np

def load_face_image(image_path, name="Unknown"):
    print(f"[INFO] Loading image for: {name}")
    bgr_image = cv2.imread(image_path)

    if bgr_image is None:
        print(f"[ERROR] Cannot open image: {image_path}")
        return None, None

    rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)

    encodings = face_recognition.face_encodings(rgb_image)
    if len(encodings) == 0:
        print(f"[WARNING] No face detected in {image_path}")
        return None, None

    return encodings[0], name


known_face_encodings = []
known_face_names = []

face_data = [
    ("C:/Users/Bhumika/OneDrive/Documents/TASK/image_1.jpg", "image 1"),
]

for img_path, name in face_data:
    encoding, person_name = load_face_image(img_path, name)
    if encoding is not None:
        known_face_encodings.append(encoding)
        known_face_names.append(person_name)

if not known_face_encodings:
    print("[ERROR] No valid known faces loaded. Exiting...")
    exit()

print("[INFO] Face data loaded successfully!")


video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("[ERROR] Failed to read from camera.")
        break

    rgb_frame = frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)

    cv2.imshow('Face Detection & Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
