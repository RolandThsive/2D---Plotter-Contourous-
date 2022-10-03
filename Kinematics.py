#This is the code for the reverse kinematics 

from cmath import acos, atan, cos, sin

#lengths of Joints
a1 = 50
a2 = 50

#Final position of EOAT
endX = 0
endY = 0

#Calculation of angles for end pos
q2 = acos((endX*endX+endY*endY-a1*a1-a2-a2)/(2*a1*a2))
q1 = atan(endY/(a1*a1+a2*a2+2*a1*a2*cos(q2)-endY*endY))-atan((a2*sin(q2))/(a1+a2*cos(q2)))