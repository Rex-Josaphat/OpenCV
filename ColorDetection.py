import numpy as np
import cv2

# Load video file or define camera device
cap = cv2.VideoCapture(0)

# Loading video or capture device
while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    '''Color filtering'''
    # Define range
    light_blue = np.array([90, 50, 50])
    dark_blue = np.array([130, 255, 255])

    # Filter the blue
    mask = cv2.inRange(hsv, light_blue, dark_blue)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('Frame', result)
    cv2.imshow('Mask', mask)
    if cv2.waitKey(1) == ord('q'):
        break

# Release camera and close window
cap.release()
cv2.destroyAllWindows()
