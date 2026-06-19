import cv2

# Open video
cap = cv2.VideoCapture("C:/Users/mbala/Downloads/1192116-hd_1920_1080_30fps.mp4")

# Background subtractor
vehicle_detector = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Detect moving objects
    mask = vehicle_detector.apply(frame)

    # Remove noise
    _, mask = cv2.threshold(mask, 200, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_TREE,
        cv2.CHAIN_APPROX_SIMPLE
    )

    # Draw rectangles around vehicles
    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area > 1000:  # Ignore small objects
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

    cv2.imshow("Vehicle Detection", frame)

    if cv2.waitKey(30) & 0xFF == 27:  # Press ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
