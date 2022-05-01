import cv2

'''Face detection using OpenCV Haar cascades'''
cap = cv2.VideoCapture(0)

# Define face and eye cascades
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    ret, frame = cap.read()

    gray_scale_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_scale_image, 1.1, 3)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)

        ''' Grab the face itself so that we can use that area to find the eyes. You find the face and pass it to the eye detector to find the eyes'''
        roi_gray = gray_scale_image[y:y+w, x:x+w] #region of interest on the grayscale image
        roi_color = frame[y:y+h, x:x+w] #region of interest on the colored image

        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 3)

    cv2.imshow('Face Recognition', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()