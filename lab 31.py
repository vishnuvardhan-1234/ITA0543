import cv2

# Read input image
image = cv2.imread("C:/Users/mbala/OneDrive/Desktop/Subject all/Computer vision/30 image.jpg")

# Check image
if image is None:
    print("Image not found!")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply threshold segmentation
threshold_value = 127

ret, segmented = cv2.threshold(
    gray,
    threshold_value,
    255,
    cv2.THRESH_BINARY
)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Segmented Image", segmented)

cv2.waitKey(0)
cv2.destroyAllWindows()
