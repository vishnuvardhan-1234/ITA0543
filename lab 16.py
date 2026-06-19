import cv2
import numpy as np
from matplotlib import pyplot as plt

# Step 1: Read the image
image = cv2.imread('C:/Users/mbala/Downloads/istockphoto-1912511508-612x612.jpg')   # Replace with your image path

# Step 2: Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Apply Sobel filter in X direction
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)

# Step 4: Apply Sobel filter in Y direction
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Step 5: Convert back to uint8
sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)

# Step 6: Combine both directions
sobel_combined = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

# Step 7: Display images
cv2.imshow("Original Image", image)
cv2.imshow("Sobel X", sobel_x)
cv2.imshow("Sobel Y", sobel_y)
cv2.imshow("Sobel Combined", sobel_combined)

cv2.waitKey(0)
cv2.destroyAllWindows()
