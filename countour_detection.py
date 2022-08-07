import cv2 as cv
import numpy as np

img = cv.imread("C:/Users/User/Downloads/Rivet_images.jpg")
cv.imshow("My_image",img)

output_copy = img.copy()

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow("gray_img",gray)
cv.waitKey(0)

