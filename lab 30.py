import cv2

# Load Smile Cascade Classifier
smile_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_smile.xml'
)

# Read image
image = cv2.imread("C:/Users/mbala/OneDrive/Desktop/Subject all/Computer vision/30 image.jpg")

# Check image
if image is None:
    print("Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect smiles
smiles = smile_cascade.detectMultiScale(
    gray,
    scaleFactor=1.8,
    minNeighbors=20
)

# Draw rectangles around smiles
for (x, y, w, h) in smiles:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Display output
cv2.imshow("Smile Detection", image)

print("Number of smiles detected:", len(smiles))

cv2.waitKey(0)
cv2.destroyAllWindows()
