import cv2

# Load Eye Cascade Classifier
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_eye.xml'
)

# Read image
image = cv2.imread("C:/Users/mbala/OneDrive/Desktop/Subject all/Computer vision/29 image.jpg")

# Check image
if image is None:
    print("Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect eyes
eyes = eye_cascade.detectMultiScale(gray, 1.1, 5)

# Draw rectangles around eyes
for (x, y, w, h) in eyes:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Display output
cv2.imshow("Eye Detection", image)
print("Number of eyes detected:", len(eyes))

cv2.waitKey(0)
cv2.destroyAllWindows()
