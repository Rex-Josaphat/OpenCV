import cv2
import numpy as np

'''If images are to be resized, the scale need to apply to both the original image and the template'''
image = cv2.imread('Images\Practice.jpg', 0)
ball = cv2.imread('Images\Ball.png', 0)
shoe =cv2.imread('Images\Shoe.png', 0)
img = image.copy()
h, w = shoe.shape # Get the height and width of the template image
H, W = ball.shape

'''Load in different template matching methods'''
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

# Use all methods on an image
for method in methods:
    img = image.copy()

    result = cv2.matchTemplate(img, shoe, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if method in [cv2.TM_SQDIFF_NORMED, cv2.TM_SQDIFF]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img, location, bottom_right, 255, 3)
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()