import cv2
import numpy as np
import matplotlib.pyplot as plt
import pickle

# Load camera matrix and distortion coefficients
with open("/home/hoangpm/AICS/anti_motor_thief/BEV_custom/cameraMatrix.pkl", "rb") as f:
    camera_matrix_data = pickle.load(f)

with open("/home/hoangpm/AICS/anti_motor_thief/BEV_custom/dist.pkl", "rb") as f:
    distortion_data = pickle.load(f)

mtx = camera_matrix_data
dist = distortion_data[0]
img_size=[640,360]

# Define the perspective transform function
def corners_unwarp(img, mtx, dist):
    undist = cv2.undistort(img, mtx, dist, None, mtx)
    # gray = cv2.cvtColor(undist, cv2.COLOR_BGR2GRAY)
    
    # cv2.imwrite("/undiss_image/img"+str(count)+".png",img)
    if ret == True:
        src = np.float32([[330, 117], [355, 200], [341, 154], [202, 226], [212, 186], [212, 173]])
        # dst = np.float32([[100, 100], [200, 100], [200, 200], [100, 200]])
        dst = np.float32([[341, 161], [342, 202], [343, 180], [302, 200], [305, 187], [303, 177]])
        # M = cv2.getPerspectiveTransform(src, dst)
        M, status = cv2.findHomography(src, dst)
        warped = cv2.warpPerspective(undist, M, img_size, flags=cv2.INTER_LINEAR)
        return warped, M
    else:
        return None, None

# Define the video input and output paths
input_video_path = '/home/hoangpm/AICS/anti_motor_thief/BEV_custom/output.mp4'
output_video_path = '/home/hoangpm/AICS/anti_motor_thief/BEV_custom/video_processed.mp4'

# Open the video file
cap = cv2.VideoCapture(input_video_path)

# Get the video properties
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
# frame_width = 200
# frame_height = 200
fps = int(cap.get(5))

# Create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

# Process each frame in the video
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Process the frame using the perspective transform
    processed_frame, _ = corners_unwarp(frame, mtx, dist)
    print(processed_frame.shape)
    print(type(processed_frame))
    # Write the processed frame to the output video
    out.write(processed_frame)

# Release the video capture and writer objects
cap.release()
out.release()

# Display a message indicating the processing is complete
print("Video processing complete.")
