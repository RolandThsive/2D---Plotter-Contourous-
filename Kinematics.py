#This is the code for the reverse kinematics 

from math import acos, atan, cos, sin, atan2, degrees,sqrt
import numpy as np

def coordtoangles(contours,imgSize):

    #lengths of Joints
    a1 = 221.86
    a2 = 121.86
    
    #Point of Origin
    x0 = 0
    y0 = 0
    
    #Reach bounderies of Robot
    farReach = a1+a2
    closeReach = a1-a2
    
    #converting contours array in list
    listcontours = list(contours)

    #Scaling picture to fit in paper
    safetyFact = 1                      #Optional additional factor should be between 0 and 1
    yimgSize = imgSize[0]               #Get size
    xImgSize = imgSize[1]
    #yPaperSize = 210*safetyFact
    #xPaperSize = 297*safetyFact
    yPaperSize = 100
    xPaperSize = 100

    yScale = yimgSize/yPaperSize        #Get side scaling
    xScale = xImgSize/xPaperSize
    if(yScale>xScale):                  #Scale image in reference to largest difference
        scale = yScale
    else:
        scale = xScale
    
    #Set translations
    xTranslate = -xPaperSize/2
    yTranslate = closeReach
    
    #Main Loop running for each point of each contour
    
    for i, icontour in enumerate(listcontours): 
        for j, contourpoint in enumerate(icontour):
        #Final position of EOAT
            
            #Scaling each point and translating reference frame
            endX = contourpoint[0][0]/scale+xTranslate
            endY = contourpoint[0][1]/scale+yTranslate
            
            #endX = contourpoint[0][0]/scale + xTranslate
            #endY = (yimgSize - contourpoint[0][1])/scale + yTranslate
            
            #Distance Reached at point from origin
            triedDist = sqrt( pow(x0-endX,2) + pow(y0-endY,2) );

            #See if point is actually reachable
            if triedDist > farReach or triedDist < closeReach:
                print('impossible target and/or error')
            else:
            #Calculation of angles for end pos
                q2 = acos((endX*endX+endY*endY-a1*a1-a2*a2)/(2*a1*a2))
                q1 = atan2(endY, endX)-atan2(a2*sin(q2), a1 + a2*cos(q2))
            #Writing angles into list 
                listcontours[i][j][0][0] = degrees(q1)
                listcontours[i][j][0][1] = degrees(q2)
                
            #Forward Kinematics calculation to verify
                if j%10 == 0:
                    #forward kinematics:
                    forwardX = a1*cos(q1)+a2*cos(q1+q2)
                    forwardY = a1*sin(q1)+a2*sin(q1+q2)
                    print('endX: ')
                    print(endX)
                    #print('forwardX: ')
                    #print(forwardX)
                    print('endY: ')
                    print(endY)
                    #print('forwardY: ')
                    #print(forwardY)
                    print('-------')

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
