import cv2
import face_recognition

def recognize_face():
    """Function to recognize a face from the webcam."""
    video_capture = cv2.VideoCapture(0)

    while True:
        ret, frame = video_capture.read()
        rgb_frame = frame[:, :, ::-1]  # Convert BGR to RGB

        # Find all face locations and encodings in the current frame
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # Here you would compare the face_encoding with known employee encodings
            # For now, we will just display the rectangle around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()
