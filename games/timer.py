import pygame
import time
pygame.init()
smallfont = pygame.font.SysFont("comicsansms", 25)

sec=60
white =(255,255,255)
clock = pygame.time.Clock()

gameDisplay= pygame.display.set_mode((800,600))

while sec is not 0 :
    neg = int(pygame.time.get_ticks() / 1000)
    sec = 60-neg
    gameDisplay.fill(white)
    timer = smallfont.render("TimeLeft :" + str(sec), True,(0,0,0))
    gameDisplay.blit(text, [0, 0])

    pygame.display.update()
    clock.tick(15)
pygame.quit()
quit()

