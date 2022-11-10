import cv2
import numpy as np
 
# read the image
image = cv2.imread(r"C:\Users\julia\Documents\GitHub\2D---Plotter-Contourous-\hh.jpg")

#grayscale
cv2.imshow('Original',image)
cv2.waitKey(0)
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale', grayscale)

cv2.waitKey(0)

#Threshold to binary image
(thresh, im_bw) = cv2.threshold(grayscale, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) #which determines the threshold automatically from the image using Otsu's method
cv2.imshow('treshold', im_bw)

cv2.waitKey(0)

#FindContours
contours, hierarchy = cv2.findContours(im_bw, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
print("Number of Contours found = " + str(len(contours)))

#Show Contours
cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
cv2.imshow('Contours', image)

cv2.waitKey(0)

#kill
cv2.destroyAllWindows()