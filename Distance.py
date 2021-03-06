'''This is a program that detects the position of a face from the camera and then shows it in the record.
It also includes a dynamic text adjustment that changes size f the text depending where the person is.'''
import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)

while True:
    success, img = cap.read()
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

        # Finding the focal length of the camera
        # d = 50 # Estimated distance between the face and camera to help us get the value of the focal lenght
        #f = (w*d)/W # Formula to find focal length
        #print(f)
        '''After finding the focal length a fixed value is recorded so as to be used in other calculations
        and we comment out this calculating part'''

        # Finding the distance between camera and face
        f = 840
        d = int((W*f)/w)
        print(d)

        cvzone.putTextRect(img, f'Distance: {d}cm', (face[10][0]-130, face[10][0]-225), scale=1.8)

    cv2.imshow("Face-Camera Distance", img)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()