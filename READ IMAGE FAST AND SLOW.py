import cv2

# Read the video
cap = cv2.VideoCapture("C:/Users/maheshpabbisetti/OneDrive/Pictures/Camera Roll/WIN_20230502_11_01_05_Pro.mp4")

# Check if the video is opened successfully
if not cap.isOpened():
    print("Error opening video file")

# Define the video writer for slow motion
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out_slow = cv2.VideoWriter('slow_motion.mp4', fourcc, 30, (int(cap.get(3)),int(cap.get(4))), True)

# Define the video writer for fast motion
out_fast = cv2.VideoWriter('fast_motion.mp4', fourcc, 30, (int(cap.get(3)),int(cap.get(4))), True)

# Read and display each frame of the video
while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        # Display the frame
        cv2.imshow('Original Video', frame)

        # Write the frame to slow motion video
        out_slow.write(frame)
        
        # Write the frame to fast motion video
        out_fast.write(frame)

        # Wait for 25 milliseconds and check for key press
        key = cv2.waitKey(25) & 0xFF
        if key == ord('q'):
            break

    else:
        break

# Release the video capture and video writers
cap.release()
out_slow.release()
out_fast.release()

# Close all windows
cv2.destroyAllWindows()
