import cv2

# Read image
img = cv2.imread('C:/Users/mbala/Downloads/istockphoto-1912511508-612x612.jpg')

# Check if image loaded properly
if img is None:
    print("Error: Image not found")
    exit()

# Get image dimensions
height, width = img.shape[:2]

# Show original image
cv2.imshow("Original Image", img)

# Define ROI safely inside image
roi = img[50:150, 50:180]   # Crop area

# Copy ROI
cropped = roi.copy()

# Get cropped dimensions
h, w = cropped.shape[:2]

# Define safe paste position
paste_y = 200
paste_x = 200

# Check if paste location is inside image boundary
if paste_y + h <= height and paste_x + w <= width:
    img[paste_y:paste_y+h, paste_x:paste_x+w] = cropped
else:
    print("Paste location exceeds image size!")

# Show cropped and modified images
cv2.imshow("Cropped ROI", cropped)
cv2.imshow("Modified Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
