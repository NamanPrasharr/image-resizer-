# to run this program run pip install opencv-python

import cv2

# add your image name and format

image = cv2.imread("your file name . format")

cv2.imshow("tittle", image)

# size you want to resize your image to

width = 200
height = 3000

resized_image = cv2.resize(image, (width,height)) 

cv2.imwrite("resized_image.jpg",resized_image)

cv2.waitKey(0)
