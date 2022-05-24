import cv2
import cvzone

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    cv2.imshow("Face-Camera Distance", img)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()