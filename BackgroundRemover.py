import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

cap = cv2.VideoCapture(0)
cap.set(3, 648)
cap.set(4, 400)
segmentor = SelfiSegmentation()
fpsreader = cvzone.FPS()

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    imgOut = segmentor.removeBG(img, (255, 20, 120), threshold=0.8)
    imgStacked = cvzone.stackImages([img, imgOut], 2, 1)

    fps, imgStacked = fpsreader.update(imgStacked)
    cv2.imshow('Background Remover', imgStacked)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
