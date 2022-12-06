#This is the code for the reverse kinematics 

from math import acos, atan, cos, sin, atan2, degrees,sqrt
import numpy as np

def coordtoangles(contours):

    #lengths of Joints, will crash if a length is 0
    a1 = 221.86
    a2 = 121.86
    
    x0 = 0
    y0 = 0
    farReach = a1+a2
    closeReach = a1-a2
    
    listcontours = list(contours)
    #print(listcontours[0])
    #print(listcontours[0][0])

    scale = 2.5
    xTranslate = 0
    yTranslate = 100
    

    for i, icontour in enumerate(listcontours): 
        for j, contourpoint in enumerate(icontour):
        #Final position of EOAT
            endX = contourpoint[0][1]/scale + xTranslate
            endY = contourpoint[0][0]/scale + yTranslate
    
        triedDist = sqrt( pow(x0-endX,2) + pow(y0-endY,2) );
        print("q2: ")
        print(triedDist)
        if triedDist > farReach or triedDist < closeReach:
            print('impossible target and/or error')
        else:
        #Calculation of angles for end pos
            q2 = acos( (pow(endX-x0,2)+pow(endY-y0,2)-pow(a1,2)-pow(a2,2)) / (2*a1*a2) );
            q1 = atan2( (endY-y0) , (endX-x0)) + atan2( (a2*sin(q2)) , (a1+a2*cos(q2)) );

            listcontours[i][j][0][0] = degrees(q1)
            listcontours[i][j][0][1] = degrees(q2)
                        
    angles = listcontours
        
    return angles



"""

def solver(endX, endY, b1, b2):
    
    inter_q2 = (endX*endX+endY*endY-b1*b1-b2*b2)/(2*b1*b2)

    #also testing for bad input, because acos needs a value between 1 and -1
    if inter_q2 > 1 or inter_q2 < -1:
        print('impossible target and/or error')
        return False, 0, 0


    print('target achievable')
    q2 = acos(inter_q2)
    q1 = atan2(endY, endX)-atan2(b2*sin(q2), b1 + b2*cos(q2))
    return True, q1, q2

def FKsolver(q1, q2, b1, b2):
    resultX = b1*cos(q1) + b2 * cos (q1+q2)
    resultY = b1*sin(q1) + b2 * sin(q1+q2)
    return resultX, resultY


no_errors, q1, q2 = solver(endX, endY, b1, b2)

print(f'q1: {q1}  q2: {q2}')

resultX, resultY = FKsolver(q1, q2, b1, b2)


print(f'endX: {endX}, endY: {endY}')
print(f'resultX: {resultX}, resultY: {resultY}')
"""
