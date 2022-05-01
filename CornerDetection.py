import numpy as np
import cv2

'''When detecting edges, corners, features, you need  to convert the image into grayscale'''
img = cv2.imread('Chess Board.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detecting corners
corners = cv2.goodFeaturesToTrack(img_gray, 100, 0.01, 10)
corners = np.int0(corners) # Converts all values in the matrix to int

# Decompose corners (Using interior arrays in the matrix)
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 3, [255, 0, 0], -1)

# Drawing lines between corners
for i in range(len(corners)):
    for j in range(i + 1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])

        ''' Create a random color in a numpy array and convert the numpy values to regular integers'''
        colour = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
        cv2.line(img, corner1, corner2, colour, 1)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()