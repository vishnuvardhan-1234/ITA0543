import cv2
import numpy as np

# Get image size from user
height = int(input("Enter image height: "))
width = int(input("Enter image width: "))

# Create a white image
image = np.ones((height, width, 3), dtype=np.uint8) * 255

# Center of circle
center = (width // 2, height // 2)

# Radius of circle
radius = min(height, width) // 4

# Draw circle
# image, center, radius, color(BGR), thickness
cv2.circle(image, center, radius, (255, 0, 0), 3)

# Display image
cv2.imshow("Circle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
