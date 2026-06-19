import cv2
import numpy as np

# Step 1: Read the image
img = cv2.imread("C:/Users/mbala/Downloads/istockphoto-1912511508-612x612.jpg")

# Step 2: Check image loaded
if img is None:
    print("Error: Image not loaded")
else:
    print("Image loaded successfully")
    print("Image shape:", img.shape)

    # Step 3: Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Step 4: Convert to float32
    gray = np.float32(gray)

    # Step 5: Apply Harris Corner Detection
    corners = cv2.cornerHarris(gray, 2, 3, 0.04)

    # Step 6: Dilate corner points for better visibility
    corners = cv2.dilate(corners, None)

    # Step 7: Mark corners in red color
    img[corners > 0.01 * corners.max()] = [0, 0, 255]

    # Step 8: Show result
    cv2.imshow("Harris Corner Detection", img)

    # Step 9: Wait and close window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
