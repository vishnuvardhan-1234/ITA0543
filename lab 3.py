import cv2

# Step 1: Read the image
img = cv2.imread("C:/Users/mbala/Downloads/istockphoto-1912511508-612x612.jpg")

# Step 2: Check image loaded
if img is None:
    print("Error: Image not loaded")
else:
    print("Image loaded successfully")
    print("Image shape:", img.shape)

    # Step 3: Convert to grayscale (required for Canny)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Step 4: Apply Canny edge detection
    edges = cv2.Canny(gray, 100, 200)

    # Step 5: Show original image
    cv2.imshow("Original Image", img)

    # Step 6: Show outline image
    cv2.imshow("Canny Edge Image", edges)

    # Step 7: Wait and close
    cv2.waitKey(0)
    cv2.destroyAllWindows()
