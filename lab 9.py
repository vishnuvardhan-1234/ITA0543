import cv2

# Step 1: Read the image
img = cv2.imread("C:/Users/mbala/Downloads/istockphoto-1912511508-612x612.jpg")

# Step 2: Check image loaded
if img is None:
    print("Error: Image not loaded")
else:
    print("Image loaded successfully")
    print("Original size:", img.shape)

    # Step 3: Resize to bigger size (Upscaling)
    bigger_img = cv2.resize(img, None, fx=2, fy=2)

    # Step 4: Resize to smaller size (Downscaling)
    smaller_img = cv2.resize(img, None, fx=0.5, fy=0.5)

    # Step 5: Show images
    cv2.imshow("Original Image", img)
    cv2.imshow("Bigger Image", bigger_img)
    cv2.imshow("Smaller Image", smaller_img)

    # Step 6: Wait and close window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
