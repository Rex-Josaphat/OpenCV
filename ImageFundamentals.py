import cv2

# Load and display images
img = cv2.imread('C10.jpg', 0)
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
cv2.imshow('Image', img)

# Close image window
cv2.waitKey(0)
cv2.destroyAllWindows()

# save image
cv2.imwrite("Image.jpg", img)