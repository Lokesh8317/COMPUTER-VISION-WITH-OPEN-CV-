import cv2
import numpy as np

# Load the image
img = cv2.imread("C:/Users/koppo/Downloads/Genshin-Impact_Key-Art-EN-920x518.png", cv2.IMREAD_GRAYSCALE)

# Create a structuring element
kernel = np.ones((5,5), np.uint8)

# Apply dilation
dilation = cv2.dilate(img, kernel, iterations=1)

# Display the result
cv2.imshow("Original", img)
cv2.imshow("Dilation", dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()
