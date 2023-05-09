import cv2

# Read the image
img = cv2.imread("C:/Users/maheshpabbisetti/OneDrive/Pictures/openCV/gray scale conversion image.png")

# Define the kernel size for dilation
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))

# Dilate the image
dilated_img = cv2.dilate(img, kernel, iterations=1)

# Display the original and dilated images side by side
cv2.imshow("Original Image", img)
cv2.imshow("Dilated Image", dilated_img)
cv2.waitKey(0)
