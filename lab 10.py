import cv2

# Step 1: Read the image
img = cv2.imread("C:/Users/mbala/Downloads/istockphoto-1912511508-612x612.jpg")

# Step 2: Check image loaded
if img is None:
    print("Error: Image not loaded")
else:
    print("Image loaded successfully")
    print("Original shape:", img.shape)

    # Step 3: Rotate image 90 degrees clockwise
    rotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    print("Rotated shape:", rotated_img.shape)

    # Step 4: Show original image
    cv2.imshow("Original Image", img)

    # Step 5: Show rotated image
    cv2.imshow("Rotated Image (90° Clockwise)", rotated_img)

    # Step 6: Wait and close window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
