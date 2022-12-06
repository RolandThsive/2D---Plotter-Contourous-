#This is the code for the reverse kinematics 

from math import acos, atan, cos, sin, degrees
import numpy as np

def coordtoangles(contours):

    #lengths of Joints, will crash if a length is 0
    a1 = 221.86
    a2 = 121.86
    
    listcontours = list(contours)
    print(listcontours[0])
    print(listcontours[0][0])

    

    for i, icontour in enumerate(listcontours): 
        for j, contourpoint in enumerate(icontour):
        #Final position of EOAT
            endX = contourpoint[0][1]
            endY = contourpoint[0][0]

        #Calculation of angles for end pos
            q2 = acos(endX*endX+endY*endY-a1*a1-a2-a2)/(2*a1*a2)
            q1 = atan(endY/(a1*a1+a2*a2+2*a1*a2*cos(q2)-endY*endY))-atan((a2*sin(q2))/(a1+a2*cos(q2)))

            listcontours[i][j][0][0] = q1
            listcontours[i][j][0][1] = q2
    
    return listcontours