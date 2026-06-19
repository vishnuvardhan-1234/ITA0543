import cv2

# Step 1: Read the image
img = cv2.imread("C:/Users/mbala/Downloads/istockphoto-1912511508-612x612.jpg")

# Step 2: Check image loaded or not
if img is None:
    print("Error: Image not loaded")
else:
    print("Image loaded successfully")
    print("Image shape:", img.shape)

    # Step 3: Apply Gaussian Blur
    blurred_img = cv2.GaussianBlur(img, (15, 15), 0)

    # Step 4: Show original image
    cv2.imshow("Original Image", img)

    # Step 5: Show blurred image
    cv2.imshow("Blurred Image", blurred_img)

    # Step 6: Wait and close window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
