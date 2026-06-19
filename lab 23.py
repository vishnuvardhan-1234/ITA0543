import cv2
import numpy as np
import os

# 1. Provide the FULL path if the image isn't in the script's folder
path = "C:/Users/mbala/OneDrive/Desktop/Subject all/Computer vision/homejpg.jpg"

# 2. Load the image
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

# 3. Check if image loaded successfully to prevent the "Assertion failed" error
if img is None:
    print(f"Error: Could not load image at {os.path.abspath(path)}. Check the file name and path.")
else:
    # 4. Define kernel and apply Top Hat
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
    top_hat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

    # 5. Display results
    cv2.imshow('Original', img)
    cv2.imshow('Top Hat (Bright Regions)', top_hat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
