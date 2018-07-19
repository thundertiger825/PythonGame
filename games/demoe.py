import pygame
import time
import random
pygame.init()
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,155,0)
blue =(0,0,255)
navy=(135,57,232)
display_width = 800
display_height = 600
icon = pygame.image.load('rr.png')#32x32
pygame.display.set_icon(icon)
gameDisplay= pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('SHIELD')
smallfont = pygame.font.SysFont("comicsansms", 20)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)
lead_x_change =0
gameDisplay.fill(white)
img = pygame.image.load('roman.png')
left=pygame.image.load('romanl.png')
right=pygame.image.load('leftroman.png')
bary=pygame.image.load('bary.png')
amb=pygame.image.load('latamb.png')
rollins=pygame.image.load('seth.png')
shield=pygame.image.load('snew.png')



clock = pygame.time.Clock()
count =0




height = int(display_height / 7)
def barrier(barr_x):
    gameDisplay.blit(bary, (barr_x, height+3))
    gameDisplay.blit(bary, (barr_x+580, height + 3))
    gameDisplay.blit(bary, (barr_x + 300, height*2 + 3))
    gameDisplay.blit(bary, (barr_x, height*3 + 3))
    gameDisplay.blit(bary, (barr_x + 580, height*3 + 3))
    gameDisplay.blit(bary, (barr_x+50, height * 4 + 3))
    gameDisplay.blit(bary, (barr_x + 600, height * 4+ 3))
    gameDisplay.blit(bary, (barr_x + 300, height * 5 + 3))
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



def design(rectlist):
    height=  int(display_height/7)
    if rectlist[0] == 't':
        pygame.draw.rect(gameDisplay, blue, (10, 10, 60, (height - 10)+2))
    else :
        pygame.draw.rect(gameDisplay, (92,46,6), (10, 10, 60, (height - 10)+2))#(topleftcordinates,width,heigjt)
    if rectlist[1] == 't':
        pygame.draw.rect(gameDisplay, blue, (730, 10, 60, (height - 10)+2))
    else :
        pygame.draw.rect(gameDisplay, (92,46,6), (730, 10, 60, height - 10))
    if rectlist[3] == 't':
        pygame.draw.rect(gameDisplay, blue, (40, height * 2 + 10, 60, height - 10))
    else:
        pygame.draw.rect(gameDisplay, (92,46,6), (40, height * 2 +10, 60, height - 10))
    if rectlist[2] == 't':
        pygame.draw.rect(gameDisplay, blue, (430, height + 10, 60, height - 10))
    else:
        pygame.draw.rect(gameDisplay, (92,46,6), (430, height + 10, 60, height - 10))
    if rectlist[4] == 't':
        pygame.draw.rect(gameDisplay, blue, (700, height * 2 + 10, 60, height - 10))
    else:
         pygame.draw.rect(gameDisplay, (92,46,6), (700, height*2 + 10, 60, height - 10))
    if rectlist[5] == 't':
        pygame.draw.rect(gameDisplay, blue, (250, height * 3 + 10, 60, height - 10))
    else :
        pygame.draw.rect(gameDisplay, (92,46,6), (250, height*3 + 10, 60, height - 10))
    if rectlist[6] == 't':
        pygame.draw.rect(gameDisplay, blue, (40, height * 5 + 10, 60, height - 10))
    else:
        pygame.draw.rect(gameDisplay, (92,46,6), (40, height*5 + 10, 60, height - 10))
    if rectlist[7] == 't':
        pygame.draw.rect(gameDisplay, blue, (700, height * 6 + 10, 60, height - 10))
    else:
        pygame.draw.rect(gameDisplay, (92,46,6), (700, height*6 + 10, 60, height - 10))

    pygame.draw.line(gameDisplay, black, (0,height), (100, height), 5)
    pygame.draw.line(gameDisplay, black, (150, height), (650, height), 5)
    pygame.draw.line(gameDisplay, black, (700, height), (800, height), 5)

    pygame.draw.line(gameDisplay, black, (0, height*2), (250, height*2), 5)
    pygame.draw.line(gameDisplay, black, (300, height*2), (600, height*2), 5)
    pygame.draw.line(gameDisplay, black, (650, height*2), (800, height*2), 5)
    pygame.draw.line(gameDisplay, black, (0, height * 3), (375, height * 3), 5)
    pygame.draw.line(gameDisplay, black, (425, height * 3), (800, height * 3), 5)
    pygame.draw.line(gameDisplay, black, (0, height*4), (100, height*4), 5)
    pygame.draw.line(gameDisplay, black, (150, height*4), (650, height*4), 5)
    pygame.draw.line(gameDisplay, black, (700, height*4), (800, height*4), 5)
    pygame.draw.line(gameDisplay, black, (0, height * 5), (250, height * 5), 5)
    pygame.draw.line(gameDisplay, black, (300, height * 5), (600, height * 5), 5)
    pygame.draw.line(gameDisplay, black, (650, height * 5), (800, height * 5), 5)
    pygame.draw.line(gameDisplay, black, (0, height * 6), (375, height * 6), 5)
    pygame.draw.line(gameDisplay, black, (425, height * 6), (800, height * 6), 5)

def text_objects(text,color,size):
    if size is "small" :
         textSurface= smallfont.render(text,True,color)
    if size is "medium" :
         textSurface= medfont.render(text,True,color)
    if size is "large" :
         textSurface= largefont.render(text,True,color)
    return textSurface,textSurface.get_rect()

def messeage_to_screen(msg, color,y_displace = 0,size="small"):
    textSurf,textRect = text_objects(msg,color,size)
    textRect.center=(display_width/2),(display_height/2)+y_displace
    gameDisplay.blit(textSurf,textRect)

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
        gameDisplay.fill((34,26,68))
        gameDisplay.blit(shield,(250,100))
        messeage_to_screen("Welcome to SHIELD ",green,-250,"small")
        messeage_to_screen("AIM:Starting as 1 member of shield try to find other two members ",white,160)
        messeage_to_screen("of shield by visiting each door in a given Time without touching spikes.",white,180)
        messeage_to_screen("WARNING :If you touch any spike or time is over your game will be over", red, 200)
        messeage_to_screen("CONTROLS: Press C to play,P to pause,E to enter a door or Q to quit ,Press <-  ,",white,220)
        messeage_to_screen("to go LEFT,->to go right,up arrow key to go up and down arrow key to go down", white, 240)

        pygame.display.update()
        clock.tick(15)



def game_loop():
    pygame.mixer.music.load("shm_vav.wav")

    pygame.mixer.music.play(-1)
    romandirection='front'
    rectlist=['f','f','f','f','f','f','f','f']
    ambrose = random.randrange(1, 9)
    seth = random.randrange(1, 9)
    print(ambrose)
    frame=0
    print(seth)
    ambfound = False
    sethfound = False
    gameOver = False
    gameExit = False
    bardirection = 'RIGHT'
    bar_x = 20
    lead_x = 400
    lead_y =height*3+ 10
    lead_x_change = 0
    won = False
    while not gameExit :
                frame=frame+1
                count=int(frame/15)
                while gameOver == True:
                    gameDisplay.fill((141,0,0))
                    messeage_to_screen("Game  Over  ", white, -50, size="large")
                    messeage_to_screen("Press C to playagain or Q to quit", white, 50)
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                            gameOver = False
                            gameExit = True
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                gameExit = True
                                gameOver = False
                            if event.key == pygame.K_c:
                                game_loop()
                while won == True:
                    gameDisplay.fill((0,159,0))
                    messeage_to_screen("CONGRTS YOU HAVE UNITED THE SHIELD  ", red, -50, size="small")
                    messeage_to_screen("Press C to playagain or Q to quit", black, 50)
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                            won = False
                            gameExit = True
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                pygame.quit()
                                quit()
                                won = False
                                gameOver = False
                            if event.key == pygame.K_c:
                                game_loop()

                lead_y_change = 0
                if bar_x < 180 and bardirection == 'RIGHT':
                    bar_x += 5
                if bar_x < 180 and bardirection == 'LEFT':
                    bar_x -= 5
                if bar_x== 180 :
                    bar_x -= 5
                    bardirection= 'LEFT'
                if bar_x== 0 :
                    bar_x += 5
                    bardirection = 'RIGHT'


                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                       gameExit== True
                       pygame.quit()
                       quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            romandirection = 'left'
                            lead_x_change = -10
                            lead_y_change = 0

                        if event.key == pygame.K_RIGHT:
                            romandirection = 'right'
                            lead_x_change = +10
                            lead_y_change = 0

                        if event.key == pygame.K_UP:
                            romandirection = 'front'
                            if lead_y==10 :
                                 lead_y_change = 0
                            elif lead_y==height+10 :
                                if ((lead_x > 0 and lead_x <100) or (lead_x + 30 > 0 and lead_x + 30 <100)) or (
                                    (lead_x > 150 and lead_x < 650) or (
                                            lead_x + 30 > 150 and lead_x + 30 < 650)) or (
                                    (lead_x >700 and lead_x < 800) or (lead_x + 30 > 700 and lead_x + 30 < 800)):
                                    lead_y_change = 0
                                else:
                                    lead_y_change += -height
                                    lead_x_change = 0
                            elif lead_y==height*2+10:
                                if ((lead_x > 0 and lead_x <250) or (lead_x + 30 > 0 and lead_x + 30 <250)) or (
                                    (lead_x > 300 and lead_x < 600) or (
                                            lead_x + 30 > 300 and lead_x + 30 < 600)) or (
                                    (lead_x >650 and lead_x < 800) or (lead_x + 30 > 650 and lead_x + 30 < 800)):
                                    lead_y_change = 0
                                else:
                                    lead_y_change += -height
                                    lead_x_change = 0
                            elif lead_y== height*3+10:
                                if ((lead_x > 0 and lead_x <375) or (lead_x + 30 > 0 and lead_x + 30 <375)) or (
                                    (lead_x > 425 and lead_x < 800) or (
                                            lead_x + 30 > 425 and lead_x + 30 < 800)) :
                                    lead_y_change = 0
                                else:
                                    lead_y_change += -height
                                    lead_x_change = 0
                            elif lead_y == height*4+ 10:
                                if ((lead_x > 0 and lead_x <100) or (lead_x + 30 > 0 and lead_x + 30 <100)) or (
                                    (lead_x > 150 and lead_x < 650) or (
                                            lead_x + 30 > 150 and lead_x + 30 < 650)) or (
                                    (lead_x >700 and lead_x < 800) or (lead_x + 30 > 700 and lead_x + 30 < 800)):
                                    lead_y_change = 0
                                else:
                                    lead_y_change += -height
                                    lead_x_change = 0
                            elif lead_y == height * 5 + 10:
                                if ((lead_x > 0 and lead_x < 250) or (lead_x + 30 > 0 and lead_x + 30 < 250)) or (
                                            (lead_x > 300 and lead_x < 600) or (
                                                            lead_x + 30 > 300 and lead_x + 30 < 600)) or (
                                            (lead_x > 650 and lead_x < 800) or (
                                                    lead_x + 30 > 650 and lead_x + 30 < 800)):
                                    lead_y_change = 0
                                else:
                                    lead_y_change += -height
                                    lead_x_change = 0
                            elif lead_y == height * 6 + 10:
                                if ((lead_x > 0 and lead_x < 375) or (lead_x + 30 > 0 and lead_x + 30 < 375)) or (
                                            (lead_x > 425 and lead_x < 800) or (
                                                            lead_x + 30 > 425 and lead_x + 30 < 800)):
                                    lead_y_change = 0
                                else:
                                    lead_y_change += -height
                                    lead_x_change = 0

                            else:
                                lead_y_change += -height
                                lead_x_change = 0
                        if event.key == pygame.K_DOWN:
                            romandirection = 'front'
                            if lead_y == 10:
                                if ((lead_x > 0 and lead_x <100) or (lead_x + 30 > 0 and lead_x + 30 <100)) or (
                                    (lead_x > 150 and lead_x < 650) or (
                                            lead_x + 30 > 150 and lead_x + 30 < 650)) or (
                                    (lead_x >700 and lead_x < 800) or (lead_x + 30 > 700 and lead_x + 30 < 800)):
                                    lead_y_change = 0
                                else:
                                    lead_y_change += height
                                    lead_x_change = 0
                            elif lead_y==height+10:
                                if ((lead_x > 0 and lead_x <250) or (lead_x + 30 > 0 and lead_x + 30 <250)) or (
                                    (lead_x > 300 and lead_x < 600) or (
                                            lead_x + 30 > 300 and lead_x + 30 < 600)) or (
                                    (lead_x >650 and lead_x < 800) or (lead_x + 30 > 650 and lead_x + 30 < 800)):
                                    lead_y_change = 0
                                else:
                                    lead_y_change += height
                                    lead_x_change = 0
                            elif lead_y== height*2+10:
                                if ((lead_x > 0 and lead_x <375) or (lead_x + 30 > 0 and lead_x + 30 <375)) or (
                                    (lead_x > 425 and lead_x < 800) or (
                                            lead_x + 30 > 425 and lead_x + 30 < 800)) :
                                    lead_y_change = 0
                                else:
                                    lead_y_change += height
                                    lead_x_change = 0
                            elif lead_y == height*3+ 10:
                                if ((lead_x > 0 and lead_x <100) or (lead_x + 30 > 0 and lead_x + 30 <100)) or (
                                    (lead_x > 150 and lead_x < 650) or (
                                            lead_x + 30 > 150 and lead_x + 30 < 650)) or (
                                    (lead_x >700 and lead_x < 800) or (lead_x + 30 > 700 and lead_x + 30 < 800)):
                                    lead_y_change = 0
                                else:
                                    lead_y_change += height
                                    lead_x_change = 0
                            elif lead_y==height*4+10:
                                if ((lead_x > 0 and lead_x <250) or (lead_x + 30 > 0 and lead_x + 30 <250)) or (
                                    (lead_x > 300 and lead_x < 600) or (
                                            lead_x + 30 > 300 and lead_x + 30 < 600)) or (
                                    (lead_x >650 and lead_x < 800) or (lead_x + 30 > 650 and lead_x + 30 < 800)):
                                    lead_y_change = 0
                                else:
                                    lead_y_change += height
                                    lead_x_change = 0
                            elif lead_y== height*5+10:
                                if ((lead_x > 0 and lead_x <375) or (lead_x + 30 > 0 and lead_x + 30 <375)) or (
                                    (lead_x > 425 and lead_x < 800) or (
                                            lead_x + 30 > 425 and lead_x + 30 < 800)) :
                                    lead_y_change = 0
                                else:
                                    lead_y_change += height
                                    lead_x_change = 0
                            elif lead_y == height * 6 + 10:
                                lead_y_change = 0

                            else:
                                lead_y_change += height
                                lead_x_change = 0
                        if event.key == pygame.K_e:
                            if lead_y==10 :
                                if ambrose==seth :
                                    ambfound =True
                                    sethfound=True
                                elif (lead_x >=10 and lead_x+30 <=70):
                                    rectlist[0] = 't'
                                    if (ambrose==1):
                                        ambfound = True
                                    elif(seth==1):
                                       sethfound = True

                                elif(lead_x >=730 and lead_x + 30 <= 790):
                                    rectlist[1] = 't'
                                    if(ambrose == 2):
                                        ambfound = True
                                    if(seth == 2):
                                        sethfound = True

                            elif lead_y==height +10:
                                if ambrose==seth :
                                    ambfound =True
                                    sethfound=True
                                elif (lead_x >= 430 and lead_x + 30 <= 490):
                                    rectlist[2] = 't'
                                    if(ambrose == 3):
                                        ambfound= True
                                    if(seth == 3):
                                        sethfound= True
                            elif lead_y==height*2+10 :
                                if ambrose==seth :
                                    ambfound =True
                                    sethfound=True
                                elif (lead_x >=40 and lead_x+30 <=100):
                                    rectlist[3] = 't'
                                    if(ambrose==4):
                                        ambfound = True
                                    if(seth == 4):
                                        sethfound = True
                                elif(lead_x > 700 and lead_x + 30 < 760):
                                    rectlist[4] = 't'
                                    if(ambrose == 5):
                                            ambfound = True
                                    if(seth == 5):
                                        sethfound = True
                            elif lead_y == height*3 + 10:
                                if ambrose == seth:
                                    ambfound = True
                                    sethfound = True
                                elif (lead_x >= 250 and lead_x + 30 <= 310):
                                    rectlist[5] = 't'
                                    if(ambrose == 6):
                                        ambfound = True
                                    if(seth == 6):
                                        sethfound = True
                            elif lead_y == height*5 + 10:
                                if ambrose == seth:
                                    ambfound = True
                                    sethfound = True
                                elif (lead_x >= 40 and lead_x + 30 <= 100):
                                    rectlist[6] = 't'
                                    if(ambrose == 7):
                                        ambfound = True
                                    if(seth == 7):

                                        sethfound = True
                            elif lead_y == height*6 + 10:
                                if ambrose == seth:
                                    ambfound = True
                                    sethfound = True
                                elif (lead_x >= 700 and lead_x + 30 <= 760):
                                    rectlist[7] = 't'
                                    if(ambrose == 8):
                                        ambfound= True
                                    if(seth == 8):
                                        sethfound = True
                        if event.key == pygame.K_p:
                            pause()




                    if event.type == pygame.KEYUP :
                        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                            lead_x_change =0

                if (lead_x+30 == bar_x and lead_y == height + 10) or (lead_x == bar_x + 20 and lead_y == height + 10):
                    gameOver = True
                if (lead_x+30 == bar_x+580 and lead_y == height + 10) or (lead_x == bar_x+580 + 20 and lead_y == height + 10):
                    gameOver = True
                if (lead_x + 30 == bar_x+300 and lead_y == height*2 + 10) or (lead_x == bar_x+300 + 20 and lead_y == height*2 + 10):
                    gameOver = True
                if (lead_x + 30 == bar_x+50 and lead_y == height*4 + 10) or (lead_x == bar_x+50 + 20 and lead_y == height*4 + 10):
                    gameOver = True
                if (lead_x + 30 == bar_x + 600 and lead_y == height*4 + 10) or (
                        lead_x == bar_x + 600 + 20 and lead_y == height*4 + 10):
                    gameOver = True

                if (lead_x + 30 == bar_x and lead_y == height*3 + 10) or (lead_x == bar_x + 20 and lead_y == height*3 + 10):
                    gameOver = True
                if (lead_x + 30 == bar_x + 580 and lead_y == height*3 + 10) or (
                        lead_x == bar_x + 580 + 20 and lead_y == height*3 + 10):
                    gameOver = True
                if (lead_x + 30 == bar_x + 300 and lead_y == height * 5 + 10) or (
                        lead_x == bar_x + 300 + 20 and lead_y == height * 5 + 10):
                    gameOver = True


                sec =60-count
                if sec is 0:
                   gameOver=True
                lead_x += lead_x_change

                lead_y += lead_y_change
                gameDisplay.fill(white)
                design(rectlist)
                #pygame.draw.rect(gameDisplay, black, (lead_x,lead_y , 60, height - 10))
                if romandirection=='front':
                    gameDisplay.blit(img, (lead_x, lead_y))
                elif romandirection=='left':
                    gameDisplay.blit(left, (lead_x, lead_y-5))
                elif  romandirection=='right':
                    gameDisplay.blit(img, (lead_x, lead_y))




                barrier(bar_x)
                if ambfound==True and sethfound==True :
                    gameDisplay.blit(amb,(lead_x-10, lead_y+10))
                    gameDisplay.blit(rollins,(lead_x+10, lead_y+10))
                    won=True
                if sethfound==True :
                    gameDisplay.blit(rollins,(lead_x+25,lead_y+8))

                if ambfound==True :
                    gameDisplay.blit(amb, (lead_x - 10, lead_y + 10))

                timer = smallfont.render("TimeLeft :" + str(sec), True, black)
                gameDisplay.blit(timer, [0, 570])






                pygame.display.update()
                clock.tick(15)

game_intro()
pygame.init()
game_loop()

pygame.quit()
quit()