import cv2

# Step 1: Read the image
original_img = cv2.imread("C:/Users/mbala/Downloads/istockphoto-1912511508-612x612.jpg")

# Step 2: Convert to grayscale
gray_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)

# Step 3: Save the grayscale image
cv2.imwrite('output_gray_opencv.jpg', gray_img)
print("Grayscale image saved as 'output_gray_opencv.jpg'")

# Optional: Display (press any key to close)
cv2.imshow('Original', original_img)
cv2.imshow('Grayscale', gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
