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

    # Step 3: Create kernel
    kernel = np.ones((5,5), np.uint8)

    # Step 4: Apply dilation
    dilated_img = cv2.dilate(img, kernel, iterations=1)

    # Step 5: Show original image
    cv2.imshow("Original Image", img)

    # Step 6: Show dilated image
    cv2.imshow("Dilated Image", dilated_img)

    # Step 7: Wait and close window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
