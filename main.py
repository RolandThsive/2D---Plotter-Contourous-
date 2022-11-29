#/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/#
# WELCOME TO OUR PROGRAM
# You will be able to make a robot draw a photo on paper by following these steps
# 1. Setup the robot proprely
# 2. Place your picture within the file and rename it: myPic (as a .jpg file)
# 3. Run the Program
#/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/#

#Get Contours

from controuring import contouring as ctr
import cv2
# image processed has to be saved in C:\Users\julia\Documents\GitHub\2D---Plotter-Contourous-\pic.jpg")

#get image from webcam
cam = cv2.VideoCapture(1)
while(True):
    result, image = cam.read()
    cv2.imshow('frame', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite(r"C:\Users\julia\Documents\GitHub\2D---Plotter-Contourous-\hh.jpg", image)
        break
cam.release()
cv2.destroyAllWindows()


contours = ctr() #get contours


