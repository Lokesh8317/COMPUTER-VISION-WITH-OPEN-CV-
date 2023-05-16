import cv2

# Load images
img1 = cv2.imread("C:/Users/koppo/Downloads/Genshin-Impact-1068x601.png")
img2 = cv2.imread("C:/Users/koppo/Downloads/Genshin-Impact_Key-Art-EN-920x518.png")

# Crop a region of interest (ROI) from img1
roi = img1[100:300, 200:400]

# Copy the ROI into img2 at a specified location
x_offset = 50
y_offset = 100
img2[y_offset:y_offset+roi.shape[0], x_offset:x_offset+roi.shape[1]] = roi

# Display the resulting image
cv2.imshow("Result", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
