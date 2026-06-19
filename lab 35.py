import cv2
import numpy as np

# User input
text = input("Enter text: ")

# Create white image
img = np.ones((400, 600, 3), dtype=np.uint8) * 255

# Put text on image
cv2.putText(img, text, (50, 200),
            cv2.FONT_HERSHEY_SIMPLEX,
            1, (0, 0, 255), 2)

# Show image
cv2.imshow("Output", img)

print("Press any key on image window to close")

cv2.waitKey(0)
cv2.destroyAllWindows() 
