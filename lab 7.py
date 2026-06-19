import cv2

# Step 1: Read captured video
video = cv2.VideoCapture("C:/Users/mbala/Downloads/14007279_1080_1920_30fps.mp4")

# Step 2: Check video opened
if not video.isOpened():
    print("Error: Video not opened")
else:
    print("Video opened successfully")

    while True:
        # Step 3: Read frame
        ret, frame = video.read()

        # Step 4: Stop if video ends
        if not ret:
            break

        # Step 5: Show normal video
        cv2.imshow("Normal Video", frame)

        # Step 6: Show slow motion
        cv2.imshow("Slow Motion Video", frame)
        cv2.waitKey(100)   # More delay = slow motion

        # Step 7: Show fast motion
        cv2.imshow("Fast Motion Video", frame)
        cv2.waitKey(10)    # Less delay = fast motion

        # Press q to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Step 8: Release video
video.release()
cv2.destroyAllWindows()
