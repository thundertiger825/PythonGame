import pygame


pygame.init()
white=(255,255,255)#rgb
black=(0,0,0)
red=(255,0,0)
green=(0,155,0)
blue =(0,0,255)

gameDisplay = pygame.display.set_mode((800,600))
gameDisplay.fill(blue)
Pix = pygame.PixelArray(gameDisplay)
Pix[10][10] = green
pygame.draw.line(gameDisplay,red,(200,300),(500,700),5)
pygame.draw.circle(gameDisplay,red,(50,50),10)
pygame.draw.rect(gameDisplay,green,(150,150,200,100))
pygame.draw.polygon()
while True :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            quit()

    pygame.display.update()

