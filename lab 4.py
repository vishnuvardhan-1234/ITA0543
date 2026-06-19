import cv2
import numpy as np
from matplotlib import pyplot as plt

# Function to analyze histogram
def analyze_histogram(image_path):

    # Step 1: Read image
    img = cv2.imread(image_path)

    # Step 2: Check image loaded
    if img is None:
        print("Error: Image not loaded")
        return

    print("Image loaded successfully")
    print("Image shape:", img.shape)

    # Step 3: Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Step 4: Calculate histogram
    histogram = cv2.calcHist([gray], [0], None, [256], [0,256])

    # Step 5: Show image
    cv2.imshow("Original Image", img)

    # Step 6: Plot histogram
    plt.title("Histogram of Image")
    plt.xlabel("Pixel Value")
    plt.ylabel("Number of Pixels")
    plt.plot(histogram)
    plt.show()

    # Step 7: Close window
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Call function
analyze_histogram("C:/Users/mbala/Downloads/istockphoto-1912511508-612x612.jpg")
