import cv2

# 1. SETUP PATHS
xml_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
image_path = r"C:\Users\mbala\OneDrive\Desktop\Subject all\Computer vision\25.png"

# 2. LOAD CLASSIFIER
watch_cascade = cv2.CascadeClassifier(xml_path)

# 3. VALIDATION CHECK
if watch_cascade.empty():
    print(f"ERROR: Could not load XML from {xml_path}")
else:
    # 4. READ IMAGE
    img = cv2.imread(image_path)

    if img is None:
        print(f"ERROR: Could not find image at {image_path}")
    else:
        # 5. CONVERT TO GRAYSCALE
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 6. DETECT OBJECTS
        objects = watch_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5
        )

        # 7. DRAW RESULTS
        print("Detected", len(objects), "object(s).")

        for (x, y, w, h) in objects:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(
                img,
                "Object Detected",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

        # 8. DISPLAY IMAGE
        cv2.imshow("Object Recognition", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
