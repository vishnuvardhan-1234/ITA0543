import cv2

# Open video
cap = cv2.VideoCapture("video.mp4")

frames = []

# Read and store all frames
while True:
    ret, frame = cap.read()

    if not ret:
        break

    frames.append(frame)

cap.release()

print("Total Frames:", len(frames))

# Play frames in reverse with slow motion
for frame in reversed(frames):

    cv2.imshow("Reverse Slow Motion Video", frame)

    # Increase delay for slow motion
    if cv2.waitKey(100) & 0xFF == 27:   # Press ESC to exit
        break

cv2.destroyAllWindows()
