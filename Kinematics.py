#This is the code for the reverse kinematics 

from math import acos, atan2, cos, sin

#lengths of Joints, will crash if a length is 0
b1 = 221.86
b2 = 121.86

#Final position of EOAT
endX = 0
endY = 100

#Calculation of angles for end pos
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
