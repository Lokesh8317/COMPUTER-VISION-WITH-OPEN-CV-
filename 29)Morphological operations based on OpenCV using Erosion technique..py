import cv2
import numpy as np

# Load the image
img = cv2.imread('C:\Users\Pavan\Pictures\HD-wallpaper-ms-dhoni-cricket-csk-star.jpg' cv2.IMREAD_GRAYSCALE)

# Define the structuring element
kernel = np.ones((5,5), np.uint8)

# Perform erosion
erosion = cv2.erode(img, kernel, iterations=1)

# Display the results
cv2.imshow('Input Image', img)
cv2.imshow('Erosion', erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()
