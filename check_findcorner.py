import cv2
import numpy as np

# Set the number of chessboard corners
nx = 9  # Number of corners in x
ny = 6  # Number of corners in y

# Capture video from the default camera (you may need to change the index if you have multiple cameras)
cap = cv2.VideoCapture('/home/hoangpm/AICS/anti_motor_thief/BEV_custom/output2.mp4')
cap.set(3, 640)  # Set width
cap.set(4, 480)

# Get the frame width, height, and frames per second (fps)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = int(cap.get(5))

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # You can change the codec as needed
out = cv2.VideoWriter('/home/hoangpm/AICS/anti_motor_thief/BEV_custom/output_with_corners.avi', fourcc, fps, (frame_width, frame_height))

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # If the frame is not read successfully, break the loop
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Find chessboard corners
    ret, corners = cv2.findChessboardCorners(gray, (nx, ny), None)

    # If corners are found, draw them on the frame
    if ret:
        cv2.drawChessboardCorners(frame, (nx, ny), corners, ret)

    # Write the frame to the output video
    out.write(frame)

    # Display the frame
    cv2.imshow('Chessboard Corners', frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera, close the VideoWriter, and close the OpenCV window
cap.release()
out.release()
cv2.destroyAllWindows()
