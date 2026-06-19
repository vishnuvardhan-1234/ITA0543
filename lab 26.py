import cv2

# Open input video
video = cv2.VideoCapture("input.mp4")

# Get video properties
fps = int(video.get(cv2.CAP_PROP_FPS))
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Read all frames and store them in a list
frames = []

while True:
    ret, frame = video.read()
    if not ret:
        break
    frames.append(frame)

video.release()

# Create output video
output = cv2.VideoWriter(
    "reversed_video.mp4",
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps,
    (width, height)
)

# Write frames in reverse order
for frame in reversed(frames):
    output.write(frame)

output.release()

print("Video reversed successfully!")
