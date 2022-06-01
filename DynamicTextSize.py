'''This is a program that detects the position of a face from the camera and then shows it in the record.
It also includes a dynamic text adjustment that changes size f the text depending where the person is.'''
import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
import numpy as np

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)

textList = ['Hello, My name is Rex',
            'I live at Ruyenzi.',
            "I'm a big fan of computer programming.",
            'My favorite language is Python.',
            "I do believe I'm very good at it"]

while True:
    success, img = cap.read()
    imgText = np.zeros_like(img)
    img = cv2.flip(img, 1)
    img, faces = detector.findFaceMesh(img, draw= False)

    #Find Eye Points if any face is available or detected.
    if faces:
        face = faces[0]
        pointLeft = face[145]
        pointRight = face[374]

        cv2.circle(img, pointLeft, 5, (255,45, 135), cv2.FILLED)
        cv2.circle(img, pointRight, 5, (255,45, 135), cv2.FILLED)
        cv2.line(img, pointLeft, pointRight, (255, 255, 15), 2)

        w, _ = detector.findDistance(pointLeft, pointRight) #Distance in pixels of image in camera
        W = 6.3 # Average distance between the left and right eye

        f = 840
        d = int((W*f)/w)
        print(d)

        cvzone.putTextRect(img, f'Distance: {d}cm', (face[10][0]-130, face[10][0]-225), scale=1.8)

        for i, text in enumerate(textList):
            singleHeight = 50
            cv2.putText(imgText, text, (50, 50 + (i*singleHeight)), cv2.FONT_ITALIC, 2, (255, 255, 255), 2)

    imgStacked = cv2.stackImages([img, imgText], 2, 1)
    cv2.imshow("Face-Camera Distance", imgStacked)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()