import pygame
import time
import random

pygame.init()
white = (255, 255, 255)  # rgb
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
display_width = 800
display_height = 600
block_size = 20
fps = 15
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('snakebywat')
#icon = pygame.image.load('apple.png')  # 32x32
#pygame.display.set_icon(icon)

gameExit = False

#img = pygame.image.load('snakeheader.png')
#appleimg = pygame.image.load("apple.png")

clock = pygame.time.Clock()
appleThickness = 30

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)


def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                    # gameDisplay.fill(white)
        messeage_to_screen("Paused", black, -100, size="large")
        messeage_to_screen("press c to continue q to quit", black, 25)
        pygame.display.update()
        clock.tick(5)


def score(score):
    text = smallfont.render("Score :" + str(score), True, black)
    gameDisplay.blit(text, [0, 0])


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
        gameDisplay.fill(white)
        messeage_to_screen("welcome to snake ", green, -100, "large")
        messeage_to_screen("press C to play,P to pause or Q to quit", black, 180)
        pygame.display.update()
        clock.tick(15)

def text_objects(text, color, size):
    if size is "small":
        textSurface = smallfont.render(text, True, color)
    if size is "medium":
        textSurface = medfont.render(text, True, color)
    if size is "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()


def messeage_to_screen(msg, color, y_displace=0, size="small"):
    # screen_text = font.render(msg, True, color)
    # gameDisplay.blit(screen_text,[display_width/2,display_height/2])
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width / 2), (display_height / 2) + y_displace
    gameDisplay.blit(textSurf, textRect)


def game_loop():

    gameExit = False
    gameOver = False

    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(white)
            messeage_to_screen("game  over  ", red, -50, size="large")
            messeage_to_screen("press C to playagain or Q to quit", black, 50)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                   pass

                if event.key == pygame.K_RIGHT:
                   pass
                if event.key == pygame.K_UP:
                   pass
                if event.key == pygame.K_DOWN:
                   pass
                if event.key == pygame.K_p:
                    pause()


        gameDisplay.fill(white)


        pygame.display.update()  # updates small portion.flip will updatee whole window


    pygame.quit()
    quit()


game_intro()
game_loop()

