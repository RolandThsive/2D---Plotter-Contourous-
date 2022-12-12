#/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/#
# WELCOME TO OUR PROGRAM
# You will be able to make a robot draw a photo on paper by following these steps
# 1. Setup the robot proprely
# 2. Place your picture within the file and rename it: myPic (as a .jpg file)
# 3. Run the Program
#/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/#

#Get Contours

from controuring import contouring as ctr
from Kinematics import coordtoangles as cta
import cv2
from test import motors as rbt
# image processed has to be saved in C:\Users\julia\Documents\GitHub\2D---Plotter-Contourous-\original.jpg")

#get image from webcam
cam = cv2.VideoCapture(0)
while(True):
    result, image = cam.read()
    cv2.imshow('frame', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite(r"C:\Users\Luc Pichot\Documents\GitHub\2D---Plotter-Contourous-\hh.jpg", image) #devide bby 2.5 for picture to fit in format
        cv2.imwrite(r"C:\Users\julia\Documents\GitHub\2D---Plotter-Contourous-\1-original.jpg", image) #devide bby 2.5 for picture to fit in format
        break
cam.release()
cv2.destroyAllWindows()

#Get size of image
imgSize = image.shape

#Get contours of Image 
contours = ctr()

#Get motor angles from contours
angles = cta(contours,imgSize) #get angles

rbt(angles)

