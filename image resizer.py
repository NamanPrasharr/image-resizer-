# to run this program run pip install opencv-python

import cv2

# add your image name and format

image = cv2.imread("Your image name.format")

# size you want to resize your image to

width = 200
height = 300

resized_image = cv2.resize(image, (width,height)) 

cv2.imwrite("resized_image.jpg",resized_image)