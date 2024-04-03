import pickle
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Read in the saved camera matrix and distortion coefficients
# These are the arrays you calculated using cv2.calibrateCamera()

with open("/home/hoangpm/AICS/anti_motor_thief/BEV_custom/cameraMatrix.pkl", "rb") as f:
    camera_matrix_data = pickle.load(f)

# Load distortion coefficients
with open("/home/hoangpm/AICS/anti_motor_thief/BEV_custom/dist.pkl", "rb") as f:
    distortion_data = pickle.load(f)

# Extracting camera matrix and distortion coefficients
mtx = camera_matrix_data
print(mtx)
# mtx = np.array(mtx).reshape((3, 3))
dist = distortion_data[0]
print("Shape of Camera Matrix (mtx):", mtx.shape)
print("Shape of Distortion Coefficients (dist):", dist.shape)

# dist_pickle = pickle.load( open( "wide_dist_pickle.p", "rb" ) )
# print(type(dist_pickle ))
# print("dist_pickle; ",dist_pickle)
# mtx = dist_pickle["mtx"]
# dist = dist_pickle["dist"]

# Read in an image
img = cv2.imread('/home/hoangpm/AICS/anti_motor_thief/BEV_custom/images/img3.png')
nx = 9 # the number of inside corners in x
ny = 6 # the number of inside corners in y

img_size = (img.shape[1], img.shape[0])

# MODIFY THIS FUNCTION TO GENERATE OUTPUT 
# THAT LOOKS LIKE THE IMAGE ABOVE
def corners_unwarp(img, nx, ny, mtx, dist):
    # Pass in your image into this function
    # Write code to do the following steps
    # 1) Undistort using mtx and dist
    
    undist = cv2.undistort(img, mtx, dist, None, mtx)
    
    # cv2.imshow("undist",undist)
    # cv2.waitKey()
    # 2) Convert to grayscale
    gray = cv2.cvtColor(undist,cv2.COLOR_BGR2GRAY)
    # 3) Find the chessboard corners
    ret, corners = cv2.findChessboardCorners(gray, (nx, ny), None)
    warped = None
    M=None
    # 4) If corners found: 
    if ret == True:
            # a) draw corners
        cv2.drawChessboardCorners(undist, (nx, ny), corners, ret)
            # b) define 4 source points src = np.float32([[,],[,],[,],[,]])
                 #Note: you could pick any four of the detected corners 
                 # as long as those four corners define a rectangle
                 #One especially smart way to do this would be to use four well-chosen
                 # corners that were automatically detected during the undistortion steps
                 #We recommend using the automatic detection of corners in your code
        # src = np.float32([corners[0],corners[7],corners[47],corners[40]])
        src = np.float32([corners[0], corners[nx - 1], corners[-1], corners[-nx]])
        # src = np.float32([(192,63), (401,29), (576,306), (98,342)])
            # c) define 4 destination points dst = np.float32([[,],[,],[,],[,]])
        dst = np.float32([[150,150],[250,150],[250,250],[150,250]])
            # d) use cv2.getPerspectiveTransform() to get M, the transform matrix
        M = cv2.getPerspectiveTransform(src, dst)
        # M,status = cv2.findHomography(src, dst)
            # e) use cv2.warpPerspective() to warp your image to a top-down view
        warped = cv2.warpPerspective(undist, M, img_size, flags=cv2.INTER_LINEAR)
    #delete the next two lines
    return warped, M

warped, perspective_M = corners_unwarp(img, nx, ny, mtx, dist)
f, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 9))
f.tight_layout()
ax1.imshow(img)
ax1.set_title('Original Image', fontsize=50)
ax2.imshow(warped)
ax2.set_title('Undistorted and Warped Image', fontsize=50)
plt.subplots_adjust(left=0., right=1, top=0.9, bottom=0.)
plt.show()