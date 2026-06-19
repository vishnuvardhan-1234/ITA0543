import cv2

# Load face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Read image
image = cv2.imread(r"C:/Users/mbala/OneDrive/Desktop/Subject all/Computer vision/38 image.jpg")

# Check image
if image is None:
    print("Image not found. Check the file path.")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 5)

# Draw rectangles
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

print("Faces detected:", len(faces))

cv2.imshow("Face Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
