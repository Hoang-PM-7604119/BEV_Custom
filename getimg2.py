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
        # return undist, M
    else:
        return None, None


cap = cv2.VideoCapture('rtsp://admin:AICSlabcam@192.168.1.64:8001/Streaming/Channels/102/?transportmode=unicast')
# cap = cv2.VideoCapture(0)
num = 0

while cap.isOpened():

    ret, img = cap.read()
    img, _ = corners_unwarp(img, mtx, dist)
    k = cv2.waitKey(5)

    if k == 27:
        break
    elif k == ord('s'): # wait for 's' key to save and exit
        cv2.imwrite('test2/img' + str(num) + '.png', img)
        print("image saved!")
        num += 1

    cv2.imshow('Img',img)

# Release and destroy all windows before termination
cap.release()

cv2.destroyAllWindows()