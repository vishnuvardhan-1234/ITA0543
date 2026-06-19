import cv2
import pytesseract

# Set Tesseract path (change according to your system)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Open video
cap = cv2.VideoCapture("video.mp4")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Extract text
    text = pytesseract.image_to_string(gray)

    # Print detected text
    if text.strip() != "":
        print("Detected Text:")
        print(text)

    # Display video
    cv2.imshow("Video", frame)

    if cv2.waitKey(30) & 0xFF == 27:   # ESC key
        break

cap.release()
cv2.destroyAllWindows()
