import pygame
import time
pygame.init()
clock=pygame.time.Clock()
display_width=800
display_height=600
screen=pygame.display.set_mode((display_width,display_height))
Exit=False
width=50
height=20
x=10
y=400
WHITE=(255,255,255)
Black=(0,0,0)
#pygame.draw.rect(screen,WHITE,[x,y,width,height])
while not Exit:
    x_change=0
    screen.fill(Black)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            Exit=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                x_change=15
            if event.key == pygame.K_LEFT:
                x_change = -15
            if event.key==pygame.K_a:
                pygame.draw.rect(screen,WHITE,[x+25,y,20,90])


    x=x+x_change

    pygame.draw.rect(screen, WHITE, [x, y, width, height])
    pygame.display.update()
    clock.tick(500)
pygame.quit()
quit()