import cv2
import time

# Replace 'your_rtsp_url' with your actual RTSP URL
rtsp_url = 'rtsp://admin:AICSlabcam@192.168.1.64:8001/Streaming/Channels/102/?transportmode=unicast'

# Set the recording duration (in seconds)
duration = 60  

# Create a VideoCapture object
cap = cv2.VideoCapture(rtsp_url)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open the RTSP stream.")
    exit()

# Create a VideoWriter object to save the recording in MP4 format
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('output2.mp4', fourcc, 20.0, (640, 360))

# Create a window to display the video
cv2.namedWindow('RTSP Video', cv2.WINDOW_NORMAL)

# Record video for the specified duration
start_time = time.time()
while time.time() - start_time < duration:
    # Read a frame from the RTSP stream
    ret, frame = cap.read()

    # If the frame is read successfully, display it and write it to the output file
    if ret:
        cv2.imshow('RTSP Video', frame)
        out.write(frame)

    # Break the loop if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture, VideoWriter, and close the window
cap.release()
out.release()
cv2.destroyAllWindows()
