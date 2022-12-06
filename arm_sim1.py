import pygame
from math import acos, atan2, cos, sin

pygame.init()

FONT = pygame.font.SysFont(None, 24)

WIDTH = 500
HEIGHT = 500

MIDDLE = WIDTH/2

#scale is how many pixels per milimeters
SCALE = 1

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("arm sim")




def plot(x1,y1, x2, y2, color=(255,0,0)):
    #plot segment start position end position
    
    y1 = HEIGHT-y1
    y2 = HEIGHT-y2

    x1 += MIDDLE
    x2 += MIDDLE

    width = 1
    pygame.draw.line(WIN, color,(x1,y1),(x2,y2), width)
    #pygame.display.update()

def FKsolver(q1, q2, b1, b2):
    resultX = b1*cos(q1) + b2 * cos(q1+q2)
    resultY = b1*sin(q1) + b2 * sin(q1+q2)
    return resultX, resultY

def FKsolver_mid(q1, q2, b1, b2):
    resultX = b1*cos(q1)
    resultY = b1*sin(q1)
    return resultX, resultY

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


#plot(500,500,(0,0,255))
pygame.display.update()

b1 = 221.86
b2 = 121.86


iter = 0

targets = [[-90,0],[-90, 200], [90,200],[90,0]]

clock = pygame.time.Clock()
#input()
try:
    while 1:
        #clock.tick(60)
        
        pygame.event.pump()
        WIN.fill((255,255,255))

        endX, endY = targets[iter]
        endY += 100

        pygame.draw.circle(WIN, (0,0,255), (endX+MIDDLE,HEIGHT-endY), 10,0)

        no_errors, q1, q2 = solver(endX, endY, b1, b2)

        #print(no_errors)

        midX, midY = FKsolver_mid(q1, q2, b1, b2)
        resultX, resultY = FKsolver(q1, q2, b1, b2)


        plot(0,0, midX, midY)
        plot(midX, midY, resultX, resultY)

        print(f'q1: {q1}  q2: {q2}')
        #print(f'q1c: {b2*cos(q1+q2)}  q2s: {b2*sin(q1+q2)}')
        print(f'endX: {endX}, endY: {endY}')
        #print(f'midX: {midX}, midY: {midY}')
        #print(f'resultX: {resultX}, resultY: {resultY}')

        #pygame.draw.circle(WIN, (0,0,255), (midX,HEIGHT-midY), 32,0)
        pygame.display.update()
        iter += 1
        if iter == len(targets):
            iter = 0
        input()






finally:
    pygame.quit()
#rem  

