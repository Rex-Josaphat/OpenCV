import numpy as np
import cv2

# Load video file or define camera device
cap = cv2.VideoCapture(0)

# Loading video or capture device
while True:
    ret, frame = cap.read()

    # Defining screen dimensions
    width = int(cap.get(3))
    height = int(cap.get(4))

    # Mirroring video into all quadrants
    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    image[:height//2, :width//2] = smaller_frame
    image[height // 2:, :width // 2] = smaller_frame
    image[:height // 2, width // 2:] = smaller_frame
    image[height // 2:, width // 2:] = smaller_frame

    cv2.imshow('Frame', image)

    if cv2.waitKey(1) == ord('q'):
        break

# Release camera and close window
cap.release()
cv2.destroyAllWindows()
