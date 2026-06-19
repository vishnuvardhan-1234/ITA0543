import cv2
import numpy as np

# Load the image
img = cv2.imread("C:/Users/mbala/OneDrive/Desktop/Subject all/Computer vision/24 lab.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Could not find image.png")
else:
    # 1. Define a 7x7 kernel
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))

    # 2. Extract dark features (Black Hat)
    black_hat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

    # 3. Dilate the extracted features to enlarge them
    dilated_foreground = cv2.dilate(black_hat, kernel, iterations=1)

    # 4. Display the results
    cv2.imshow('Original Image', img)
    cv2.imshow('Black Hat (Dark Details)', black_hat)
    cv2.imshow('Dilated Foreground', dilated_foreground)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
