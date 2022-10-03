#This is the code for the reverse kinematics 

from math import acos, atan2, cos, sin

#lengths of Joints
a1 = 50
a2 = 50

#Final position of EOAT
endX = 50
endY = 10

#Calculation of angles for end pos
q2 = acos((endX*endX+endY*endY-a1*a1-a2*a2)/(2*a1*a2))
q1 = atan2(endY, endX)-atan2(a2*sin(q2), a1 + a2*cos(q2))

print(f'q1: {q1}  q2: {q2}')

resultX = 0
resultY = 0

resultX = a1*cos(q1) + a2 * cos (q1+q2)
resultY = a1*sin(q1) + a2 * sin(q1+q2)

print(f'endX: {endX}, endY: {endY}')
print(f'resultX: {resultX}, resultY: {resultY}')