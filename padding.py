import cv2
import numpy as np

# Read the image
image = cv2.imread('/home/hoangpm/AICS/anti_motor_thief/BEV_custom/16dcdccd434fea11b35e.jpg')  # Replace with the path to your image

# Rotate the image left 90 degrees
rotated_image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

# Resize the rotated image to a width of 200 pixels while maintaining the aspect ratio
target_width = 100
aspect_ratio = rotated_image.shape[1] / rotated_image.shape[0]
target_height = int(target_width / aspect_ratio)

resized_image = cv2.resize(rotated_image, (target_width, target_height))

# Create a blank image with the target shape and fill it with a color (e.g., white)
target_shape = (640, 360)
padded_image = 255 * np.ones((target_shape[1], target_shape[0], 3), dtype=np.uint8)

# Calculate the position to paste the resized image in the center
start_x = (target_shape[0] - target_width) // 2
start_y = (target_shape[1] - target_height) // 2

# Paste the resized image onto the padded image
padded_image[start_y:start_y + target_height, start_x:start_x + target_width] = resized_image

# Display the original, rotated, resized, and padded images
cv2.imshow('Original Image', image)
cv2.imshow('Rotated Image', rotated_image)
cv2.imshow('Resized Image', resized_image)
cv2.imshow('Padded Image', padded_image)

cv2.imwrite('padded.jpg',padded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
