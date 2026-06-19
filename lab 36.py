import cv2

# Read image
img = cv2.imread("C:/Users/mbala/OneDrive/Desktop/Subject all/Computer vision/36 image.png")

if img is None:
    print("Image not found")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply threshold
_, mask = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# Remove background
result = cv2.bitwise_and(img, img, mask=mask)

# Show results
cv2.imshow("Original", img)
cv2.imshow("Mask", mask)
cv2.imshow("Background Removed", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
