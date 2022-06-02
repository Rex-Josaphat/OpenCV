'''This is a program that detects the position of a face from the camera and then shows it in the record.
It also includes a dynamic text adjustment that changes size f the text depending where the person is.'''
import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
import numpy as np

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)
sen = 10 #More sen results into lower sensitivity
textList = ['Hello, My name is Rex',
            'I live at Ruyenzi.',
            "I'm a big fan of computer",
            "programming.",
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

        w, _ = detector.findDistance(pointLeft, pointRight) #Distance in pixels of image in camera
        W = 6.3 # Average distance between the left and right eye

        f = 840
        d = (W*f)/w
        # print(d)

        cvzone.putTextRect(img, f'Distance: {int(d)}cm', (face[10][0]-130, face[10][0]-225), scale=1.8)

        for i, text in enumerate(textList):
            singleHeight = 20 + int((int(d/sen)*sen)/5)
            scale = 0.4+ (int(d/sen)*sen)/100
            cv2.putText(imgText, text, (30, 50 + (i*singleHeight)), cv2.FONT_ITALIC, scale, (255, 255, 255), 2)

    imgStacked = cvzone.stackImages([img, imgText], 2, 1)
    cv2.imshow("Face-Camera Distance", imgStacked)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()