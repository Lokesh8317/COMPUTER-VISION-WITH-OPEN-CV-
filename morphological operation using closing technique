import cv2
import numpy as np

# Load the image
img = cv2.imread("C:/Users/koppo/Downloads/Genshin-Impact_Key-Art-EN-920x518.png", cv2.IMREAD_GRAYSCALE)

# Create a structuring element
kernel = np.ones((5,5), np.uint8)

# Apply closing
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# Display the result
cv2.imshow("Original", img)
cv2.imshow("Closing", closing)
cv2.waitKey(0)
cv2.destroyAllWindows()
