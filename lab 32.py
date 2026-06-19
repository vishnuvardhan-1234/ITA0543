import cv2
import numpy as np

# Get image size from user
height = int(input("Enter image height: "))
width = int(input("Enter image width: "))

# Create a white image
image = np.ones((height, width, 3), dtype=np.uint8) * 255

# Size of each box = 1/10th of image size
box_h = height // 10
box_w = width // 10

# Top-Left Corner : Black
image[0:box_h, 0:box_w] = (0, 0, 0)

# Top-Right Corner : Blue
image[0:box_h, width-box_w:width] = (255, 0, 0)

# Bottom-Left Corner : Green
image[height-box_h:height, 0:box_w] = (0, 255, 0)

# Bottom-Right Corner : Red
image[height-box_h:height, width-box_w:width] = (0, 0, 255)

# Display image
cv2.imshow("Colored Corner Boxes", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# input 500 and 500
