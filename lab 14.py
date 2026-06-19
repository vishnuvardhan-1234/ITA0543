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

    rows, cols, ch = img.shape

    # Step 3: Define four points in original image
    pts1 = np.float32([[50, 50], [cols-50, 50], [50, rows-50], [cols-50, rows-50]])

    # Step 4: Define four points in output image
    pts2 = np.float32([[0, 0], [cols, 0], [0, rows], [cols, rows]])

    # Step 5: Create perspective transformation matrix
    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    # Step 6: Apply perspective transformation
    transformed_img = cv2.warpPerspective(img, matrix, (cols, rows))

    # Step 7: Show images
    cv2.imshow("Original Image", img)
    cv2.imshow("Perspective Transformed Image", transformed_img)

    # Step 8: Wait and close window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
