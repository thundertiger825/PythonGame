import pygame
import time
import random
pygame.init()
white=(255,255,255)#rgb
black=(0,0,0)
red=(255,0,0)
green=(0,155,0)
display_width = 800
display_height = 600
block_size=20
gameDisplay= pygame.display.set_mode((display_width,display_height))
fps=15
direction = "right"


pygame.display.set_caption('snakebywat')
icon = pygame.image.load('apple.png')#32x32
pygame.display.set_icon(icon)

gameExit= False
lead_x = display_width/2
lead_y = display_height/2
lead_x_change = 0
lead_y_change = 0
img = pygame.image.load('snakeheader.png')
appleimg = pygame.image.load("apple.png")

clock = pygame.time.Clock()
appleThickness = 30

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)
def pause():
    paused = True
    while paused :
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_c :
                    paused = False
                elif event.key == pygame.K_q :
                     pygame.quit()
                     quit()
         #gameDisplay.fill(white)
        messeage_to_screen("Paused",black,-100,size="large")
        messeage_to_screen("press c to continue q to quit",black,25)
        pygame.display.update()
        clock.tick(5)

def score(score):
    text =smallfont.render("Score :" + str(score),True, black)
    gameDisplay.blit(text,[0,0])

def randAppleGen():
    randAppleX = round(random.randrange(0, display_width - appleThickness))  # / 10.0) * 10.0
    randAppleY = round(random.randrange(0, display_height - appleThickness))  # / 10.0) * 10.0
    return randAppleX,randAppleY

def game_intro() :
    intro = True
    while intro :
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_c :
                    intro = False
                if event.key == pygame.K_q :
                    pygame.quit()
                    quit()
        gameDisplay.fill(white)
        messeage_to_screen("welcome to snake ",green,-100,"large")
        messeage_to_screen("press C to play,P to pause or Q to quit",black,180)
        pygame.display.update()
        clock.tick(15)


def snake(block_size,snakelist):

    if direction == "right" :
        head = pygame.transform.rotate(img,270)
    if direction == "left" :
        head = pygame.transform.rotate(img,90)
    if direction == "up" :
        head = img
    if direction == "down" :
        head = pygame.transform.rotate(img,180)
    gameDisplay.blit(head, (snakelist[-1][0],snakelist[-1][-1]))
    for XnY in snakelist[:-1] :

        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])
def text_objects(text,color,size):
    if size is "small" :
         textSurface= smallfont.render(text,True,color)
    if size is "medium" :
         textSurface= medfont.render(text,True,color)
    if size is "large" :
         textSurface= largefont.render(text,True,color)
    return textSurface,textSurface.get_rect()



def messeage_to_screen(msg, color,y_displace = 0,size="small"):
    #screen_text = font.render(msg, True, color)
    #gameDisplay.blit(screen_text,[display_width/2,display_height/2])
    textSurf,textRect = text_objects(msg,color,size)
    textRect.center=(display_width/2),(display_height/2)+y_displace
    gameDisplay.blit(textSurf,textRect)

def game_loop():
    global direction
    direction = 'right'
    gameExit = False
    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 10
    lead_y_change = 0
    snakeList = []
    snakeLength = 1
    gameOver = False
    randAppleX = round(random.randrange(0,display_width-appleThickness))#/10.0)*10.0
    randAppleY = round(random.randrange(0, display_height -appleThickness))# /10.0)*10.0


    while not gameExit :
        while gameOver == True :
            gameDisplay.fill(white)
            messeage_to_screen("game  over  ",red,-50,size= "large")
            messeage_to_screen("press C to playagain or Q to quit",black,50)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    gameOver= False
                    gameExit=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q :
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        game_loop()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit=True
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_LEFT :
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0

                if event.key == pygame.K_RIGHT :
                    direction = "right"
                    lead_x_change= +block_size
                    lead_y_change = 0
                if event.key == pygame.K_UP :
                    direction ="up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                if event.key == pygame.K_DOWN :
                    direction="down"
                    lead_y_change = +block_size
                    lead_x_change = 0
                if event.key == pygame.K_p :
                    pause()
          #  if event.type == pygame.KEYUP :
               # if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                   # lead_x_change = 0
        if lead_x >= display_width or lead_x <0 or lead_y >= display_height or lead_y < 0 :
            gameOver = True
        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)

        #pygame.draw.rect(gameDisplay,red,[randAppleX,randAppleY,appleThickness,appleThickness])
        gameDisplay.blit(appleimg,(randAppleX,randAppleY))
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength :
            del snakeList[0] #to show movement or to del last segment of snake

        for eachSegment in snakeList[:-1] :
            if eachSegment == snakeHead :
                gameOver = True

        snake(block_size, snakeList)
        #gameDisplay.fill(red,rect=[100,100,20,20])
        score(snakeLength-1)
        pygame.display.update()#updates small portion.flip will updatee whole window
        """
        if lead_x == randAppleX and lead_y== randAppleY :
            randAppleX = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
            randAppleY = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0
            snakeLength += 1 
        
        if lead_x >= randAppleX and lead_x <= randAppleX + appleThickness :
            if lead_y >= randAppleY and lead_y <= randAppleY + appleThickness:
                    randAppleX = round(random.randrange(0, display_width - block_size)) #/ 10.0) * 10.0
                    randAppleY = round(random.randrange(0, display_height - block_size))# / 10.0) * 10.0
                    snakeLength += 1
        """
        if lead_x > randAppleX and lead_x < randAppleX + appleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + appleThickness :
            if lead_y > randAppleY and lead_y < randAppleY + appleThickness :
                """commenting since funt is used
                randAppleX = round(random.randrange(0, display_width - appleThickness))  # / 10.0) * 10.0
                randAppleY = round(random.randrange(0, display_height - appleThickness))  # / 10.0) * 10.0
                """
                randAppleX,randAppleY = randAppleGen()
                snakeLength += 1

            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + appleThickness :
                """
                randAppleX = round(random.randrange(0, display_width - appleThickness))  # / 10.0) * 10.0
                randAppleY = round(random.randrange(0, display_height - appleThickness))  # / 10.0) * 10.0
                """
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1


        clock.tick(fps)
        """    
            messeage_to_screen("youlose",red)
            pygame.display.update()
            time.sleep(2)
        """

    pygame.quit()
    quit()
game_intro()
game_loop()

