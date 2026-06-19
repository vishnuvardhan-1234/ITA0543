import cv2
import numpy as np

# Read original image
original = cv2.imread(r"C:/Users/mbala/Downloads/istockphoto-1912511508-612x612.jpg")

# Read watermark image
watermark = cv2.imread(r"C:/Users/mbala/Downloads/istockphoto-1912511508-612x612.jpg")

# Check if images loaded successfully
if original is None:
    print("Original image not found!")
    exit()

if watermark is None:
    print("Watermark image not found!")
    exit()

# Resize watermark
watermark = cv2.resize(watermark, (original.shape[1], original.shape[0]))

# Transparency
alpha = 0.7
beta = 0.3

# Blend images
watermarked_image = cv2.addWeighted(original, alpha, watermark, beta, 0)

# Display
cv2.imshow("Original Image", original)
cv2.imshow("Watermarked Image", watermarked_image)

# Save
cv2.imwrite("watermarked_output.jpg", watermarked_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
