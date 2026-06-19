import cv2
import numpy as np

# Get image size from user
height = int(input("Enter image height: "))
width = int(input("Enter image width: "))

# Create a white image
image = np.ones((height, width, 3), dtype=np.uint8) * 255

# Draw a rectangle
# (start point), (end point), color(BGR), thickness
cv2.rectangle(image, (50, 50), (250, 150), (0, 0, 255), 3)

# Display image
cv2.imshow("Rectangle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# input 400 and 500
