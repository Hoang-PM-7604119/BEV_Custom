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
img=cv2.imread('/home/hoangpm/AICS/anti_motor_thief/BEV_custom/test2/img0.png')
undist = cv2.undistort(img, mtx, dist, None, mtx)
gray = cv2.cvtColor(undist, cv2.COLOR_BGR2GRAY)

cv2.imwrite("undis.jpg",undist)

