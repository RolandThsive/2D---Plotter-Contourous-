
import cv2
import numpy as np

# read the image
def contouring():
    image = cv2.imread(r"C:\Users\Luc Pichot\Documents\GitHub\2D---Plotter-Contourous-\Programming\twitch.png")

    #grayscale
    #cv2.imshow('Original',image)
    #cv2.waitKey(0)
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grayscale = grayscale.astype("uint8")
    cv2.imwrite(r"C:\Users\Luc Pichot\Documents\GitHub\2D---Plotter-Contourous-\Programming\2-grayscale.jpg", grayscale)
    #cv2.imshow('Grayscale', grayscale)
    #cv2.waitKey(0)

        #------------------------# laplacian #------------------------#
    #laplacian = cv2.Laplacian(grayscale,cv2.THRESH_BINARY)
    #cv2.imshow("laplace",laplacian)
    #cv2.waitKey(0)
    
        #------------------------# canny #------------------------#
    
    canny = cv2.Canny(grayscale,100,200)
    cv2.imwrite(r"C:\Users\Luc Pichot\Documents\GitHub\2D---Plotter-Contourous-\Programming\3-canny.jpg", canny)
    #cv2.imshow("edges",canny)
    #cv2.waitKey(0)
    
        #------------------------# sobel #------------------------#
        
    #sobx = cv2.Sobel(grayscale,cv2.CV_64F,1,0,ksize=5)
    #cv2.imshow("sobx",sobx)
    #cv2.waitKey(0)
    #soby = cv2.Sobel(grayscale,cv2.CV_64F,0,1,ksize=5)
    #cv2.imshow("soby",soby)
    #cv2.waitKey(0)
    #sobel = cv2.add(sobx,soby)
    #cv2.waitKey(0)
    #cv2.imshow("Added Image",sobel)
    #cv2.imwrite(r"C:\Users\julia\Documents\GitHub\2D---Plotter-Contourous-\ll.jpg", sobel) 
    #sob = cv2.imread(r"C:\Users\julia\Documents\GitHub\2D---Plotter-Contourous-\ll.jpg")
    #sob = cv2.cvtColor(sob,cv2.COLOR_BGR2GRAY)
    #cv2.waitKey(0)
    
        #------------------------# threshold #------------------------#
        
    #(thresh, im_bw) = cv2.threshold(grayscale, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) #which determines the threshold automatically from the image using Otsu's method
    #cv2.imshow('treshold', im_bw)
    #cv2.waitKey(0)

        #------------------------# FindContours #------------------------#
    contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
    print("Number of Contours found = " + str(len(contours)))

        #------------------------# Show Contours #------------------------#
    for cnt in contours : 

        approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True) 
        cv2.drawContours(image, [approx], -1, (0, 0 , 255), 3)
        n = approx.ravel() 
        i = 0

        for j in n : 
            if(i % 2 == 0): 
                x = n[i] 
                y = n[i + 1] 
                i=i+1
        
    cv2.imwrite(r"C:\Users\Luc Pichot\Documents\GitHub\2D---Plotter-Contourous-\Programming\4-contours.jpg", canny)
    #cv2.imshow('Contours', image)
    #cv2.waitKey(0)

    
    return contours 

#contours are separated in different vectors of point, contours[1][0] gives the first point of the first interesting contour
#points coordinates with openCV coordinate system, to come back to a normal coordinate system, xnew = xold & ynew = ymax - yold
