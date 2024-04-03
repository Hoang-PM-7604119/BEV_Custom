import cv2
import numpy as np


points = []

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Tọa độ x, y:", x, y)
        points.append((x, y))
        cv2.circle(img, (x, y), 5, (0, 255, 0), -1)
        cv2.imshow('image', img)

img = cv2.imread('/home/hoangpm/AICS/anti_motor_thief/BEV_custom/img10.png')
w,h=img.shape[:2]
size=w*h
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)

while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cv2.destroyAllWindows()

print("Tọa độ các điểm:", points)

if len(points) == 4:
    x, y = zip(*points)
    area = 0.5 * abs(sum(x[i] * y[i + 1] - x[i + 1] * y[i] for i in range(3)) + x[3] * y[0] - x[0] * y[3])
    print("Diện tích của tứ giác là:", area)
else:
    print("Cchon sai.")

print( "phan tram tren anh: ",area/size)