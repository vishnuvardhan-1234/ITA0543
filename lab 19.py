import cv2
import numpy as np

# Read the image
img = cv2.imread('C:/Users/mbala/Downloads/istockphoto-1912511508-612x612.jpg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert to binary image
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Create kernel (structuring element)
kernel = np.ones((5,5), np.uint8)

# Apply erosion
eroded = cv2.erode(binary, kernel, iterations=1)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Binary Image", binary)
cv2.imshow("Eroded Image", eroded)

cv2.waitKey(0)
cv2.destroyAllWindows()
