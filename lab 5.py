import cv2
import matplotlib.pyplot as plt

def analyze_color_histogram(image_path):

    image = cv2.imread(image_path)

    if image is None:
        print("Error: Image not found")
        return

    colors = ('blue', 'green', 'red')   # Correct colors
    histograms = {}

    plt.figure()
    plt.title("Color Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")

    for i, color in enumerate(colors):
        hist = cv2.calcHist([image], [i], None, [256], [0,256])
        histograms[color] = hist
        plt.plot(hist, color=color, linewidth=2)

    plt.show()

    return histograms


# Main
histograms = analyze_color_histogram(r"C:/Users/mbala/Downloads/istockphoto-1912511508-612x612.jpg")
