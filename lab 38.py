import cv2

# Load face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Read image
img = cv2.imread("C:/Users/mbala/OneDrive/Desktop/Subject all/Computer vision/38 image.jpg")

# Check image
if img is None:
    print("Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

# Draw rectangles around faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Count faces
count = len(faces)

print("Number of Faces Detected:", count)

# Display image
cv2.imshow("Face Count", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
