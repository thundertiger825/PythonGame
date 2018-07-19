import  time
import pygame
import random
pygame.init()
clock=pygame.time.Clock()
display_width=800
display_height=600
WHITE=(255,255,255)
BLUE=(0,0,255)
screen=pygame.display.set_mode((display_width,display_height))
die1=pygame.image.load('Untitled8781.png')
die2=pygame.image.load('Untitled8782.png')
die3=pygame.image.load('Untitled8783.png')
die4=pygame.image.load('Untitled8784.png')
die5=pygame.image.load('Untitled8785.png')
die6=pygame.image.load('Untitled8786.png')
die11=pygame.image.load('Untitled87811.png')
die21=pygame.image.load('Untitled87821.png')
die31=pygame.image.load('Untitled87831.png')
die41=pygame.image.load('Untitled87841.png')
die51=pygame.image.load('Untitled87851.png')
die61=pygame.image.load('Untitled87861.png')

player=pygame.image.load('happy_smiley_face_round_stickers-rbdcd90a58b8e40a9b895e7c2fd1e65ef_v9waf_8byvr_3241.jpg')
ludo=pygame.image.load('stock-vector-snakes-and-ladders-board-game-snakes-ladders-start-finish-163384724.jpg')
player2=pygame.image.load("Untitled8881.png")
def comp(x2,y2,s,t):
    y11_change=t
    if (x2 > 551 or x2 < 0):
        y11_change = -59
        # print(x1-551)
        if (x2 > 551):
            z = round((x2 - 551) / 59)
            # print(z)
            x2 = 10 + (10 - z) * 59
            y2 = y2 + y11_change
        if (x2 < 10):
            if (y2 > 0 and y2 < 59):
                x2 = x2 - s
                y11_change = 0
                y2 = y2 + y11_change

            else:
                z1 = round((10 - x2) / 59)
                print(z1)
                x2 = 10 + (z1 - 1) * 59
                y2 = y2 + y11_change
                # print(y11_change)
                # x_change=-((x2-551)/59)

                # print(y2)
                # x2 = x2 + x_change
                # print(x_change)
                # print(x2)
    if (y2 > 0 and y2 < 1 * 59):
        if (x2 >= 10 and x2 < 59):
            text_to_display("YoU WoN", 72, WHITE, 0)
            option()
            print("you won")

    if (y2 > 9 * 59 and y2 < 10 * 59):
        if (x2 > 3 * 59 and x2 < 4 * 59):
            x2 = 10 + 6 * 59
            y11_change = -59
            y2 = y2 + y11_change

        if (x2 > 8 * 59 and x2 < 9 * 59):
            x2 = 10 + 9 * 59
            y11_change = -3 * 59
            y2 = y2 + y11_change

    elif (y2 > 7 * 59 and y2 < 8 * 59):
        if (x2 > 0 and x2 < 1 * 59):
            x2 = 10 + (2 - 1) * 59
            y11_change = -2 * 59
            # print(y11_change)
            y2 = y2 + y11_change
        if (x2 > 7 * 59 and x2 < 8 * 59):
            x2 = 10 + (4 - 1) * 59
            y11_change = -6 * 59
            y2 = y2 + y11_change
    elif (y2 > 4 * 59 and y2 < 5 * 59):
        print("i am here")
        if (x2 > 9 * 59 and x2 < 10 * 59):
            x2 = 10 + (7 - 1) * 59
            y11_change = -59
            y2 = y2 + y11_change
        if (x2 > 6 * 59 and x2 < 7 * 59):
            x2 = 10 + 6 * 59
            y11_change = 2 * 59
            y2 = y2 + y11_change

    elif (y2 > 2 * 59 and y2 < 3 * 59):
        if (x2 > 8 * 59 and x2 < 9 * 59):
            x2 = 10 + 9 * 59
            y11_change = -2 * 59
            y2 = y2 + y11_change
        if (x2 > 0 and x2 < 59):
            x2 = 10 + (2 - 1) * 59
            y11_change = -2 * 59
            y2 = y2 + y11_change

    elif (y2 > 0 and y2 < 59):
        if (x2 > 2 * 59 and x2 < 3 * 59):
            x2 = 10 + (2 - 1) * 59
            y11_change = 2 * 59
            y2 = y2 + y11_change
        if (x2 > 5 * 59 and x2 < 6 * 59):
            x2 = 10 + (5 - 1) * 59
            y11_change = 2 * 59
            y2 = y2 + y11_change
        if (x2 > 7 * 59 and x2 < 8 * 59):
            x2 = 10 + (8 - 1) * 59
            y11_change = 2 * 59
            y2 = y2 + y11_change
    elif (y2 > 59 and y2 < 2 * 59):
        if (x2 > 6 * 59 and x2 < 7 * 59):
            x2 = 10 + (5 - 1) * 59
            y11_change = 5 * 59
            y2 = y2 + y11_change
    elif (y2 > 3 * 59 and y2 < 4 * 59):
        if (x2 > 3 * 59 and x2 < 4 * 59):
            x2 = 10
            y11_change = 59
            y2 = y2 + y11_change
        if (x2 > 1 * 59 and x2 < 2 * 59):
            x2 = 10 + (2 - 1) * 59
            y11_change = 5 * 59
            y2 = y2 + y11_change
    elif (y2 > 8 * 59 and y2 < 9 * 59):
        if (x2 > 3 * 59 and x2 < 4 * 59):
            x2 = 10 + 6 * 59
            y11_change = 59
            y2 = y2 + y11_change
    screen.blit(player2,[x2,y2])


def text_to_display(text,size,color,y_displace):
    screen.fill(BLUE)
    font = pygame.font.SysFont("Comicsansms", size)
    font1=font.render(text,True,color)
    screen.blit(font1,[40,display_height/4+y_displace])
    pygame.display.update()
    time.sleep(1)
front_img=pygame.image.load("Unnamed.png")
def front_window():
    screen.fill(WHITE)
    font = pygame.font.SysFont("Comicsansms", 48)
    font1 = font.render("Snake and Ladders", True, BLUE)
    font3=pygame.font.SysFont("Comicsansms", 36)
    font2= font3.render("Press 'a' to roll a die", True, (0,0,0))
    screen.blit(font1, [40, 500])
    screen.blit(front_img,[200,0])
    screen.blit(font2,[50,550])
    pygame.display.update()
    time.sleep(3)
    screen.fill(BLUE)

    gameloop()


def option():
    text_to_display("Press q to quit or a to play again",48,WHITE,0)
    for event in pygame.event.get():
        if (event.type==pygame.KEYDOWN):
            if(event.key==pygame.K_a):
                gameloop()
            if(event.key==pygame.K_q):
                pygame.quit()
                quit()
cond=0
def gameloop():
    pygame.mixer.music.load('08-china-great-wall.mp3')
    pygame.mixer.music.play(-1)

    global cond
    x1=10
    y1=549
    x2=10
    y2=549
    x_change=0
    y_change=0
    Exit = False
    screen.blit(ludo, [0, 0])
    screen.blit(die1,[600,200])
    screen.blit(player2,[x2,y2])
    #screen.blit(die11,[600,20])
    pygame.display.update()

    #screen.fill(BLUE)
    while not Exit:
        x_change=0
        x1_change=0
        y1_change=0
        y_change=0
        count=0
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYUP:
                x_change=0
                y_change=0
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    x=random.randint(1,6)
                    if((y1>59 and y1<2*59) or(y1>3*59 and y1<4*49) or (y1>5*59 and y1<6*59) or (y1>7*59 and y1<8*59) or(y1>9*59 and y1<10*59) ):
                        if(x==1):
                            x_change=1*59
                            screen.blit(die1,[600,200])
                        if (x == 2):
                            screen.blit(die2, [600, 200])
                            x_change = 2*59
                        if (x == 3):
                            screen.blit(die3, [600, 200])
                            x_change = 3*59
                        if (x == 4):
                            screen.blit(die4, [600, 200])
                            x_change = 4*59
                        if (x == 5):
                            screen.blit(die5, [600, 200])
                            x_change = 5*59
                        if (x == 6):
                            screen.blit(die6, [600, 200])
                            x_change = 6*59
                    if ((y1 > 0 and y1 < 1 * 59) or (y1 > 2 * 59 and y1 < 3 * 49) or (y1 > 4 * 59 and y1 < 5 * 59) or (y1 > 6 * 59 and y1 < 7 * 59) or (y1 > 8 * 59 and y1 < 9 * 59)):
                        if (x == 1):
                            x_change = -(1 * 59)
                            screen.blit(die1, [600, 200])
                        if (x == 2):
                            screen.blit(die2, [600, 200])
                            x_change = -(2 * 59)
                        if (x == 3):
                            screen.blit(die3, [600, 200])
                            x_change = -(3 * 59)
                        if (x == 4):
                            screen.blit(die4, [600, 200])
                            x_change = -(4 * 59)
                        if (x == 5):
                            screen.blit(die5, [600, 200])
                            x_change = -(5 * 59)
                        if (x == 6):
                            screen.blit(die6, [600, 200])
                            x_change = -(6 * 59)
        x9 = random.randint(1, 6)
        if ((y2 > 59 and y2 < 2 * 59) or (y2 > 3 * 59 and y2 < 4 * 49) or (y2 > 5 * 59 and y2 < 6 * 59) or (
                        y2 > 7 * 59 and y2 < 8 * 59) or (y2 > 9 * 59 and y2 < 10 * 59)):
            if (x9 == 1):
                x1_change = 1 * 59
                screen.blit(die11, [600, 20])
            if (x9 == 2):
                screen.blit(die21, [600, 20])
                x1_change = 2 * 59
            if (x9 == 3):
                screen.blit(die31, [600, 20])
                x1_change = 3 * 59
            if (x9 == 4):
                screen.blit(die41, [600, 20])
                x1_change = 4 * 59
            if (x9 == 5):
                screen.blit(die51, [600, 20])
                x1_change = 5 * 59
            if (x9 == 6):
                screen.blit(die61, [600, 20])
                x1_change = 6 * 59
        if ((y2 > 0 and y2 < 1 * 59) or (y2 > 2 * 59 and y2 < 3 * 49) or (y2 > 4 * 59 and y2 < 5 * 59) or (
                        y2 > 6 * 59 and y2 < 7 * 59) or (y2 > 8 * 59 and y2 < 9 * 59)):
            if (x9 == 1):
                x1_change = -(1 * 59)
                screen.blit(die11, [600, 20])
            if (x9 == 2):
                screen.blit(die21, [600, 20])
                x1_change = -(2 * 59)
            if (x9 == 3):
                screen.blit(die31, [600, 20])
                x1_change = -(3 * 59)
            if (x9 == 4):
                screen.blit(die41, [600, 20])
                x1_change = -(4 * 59)
            if (x9 == 5):
                screen.blit(die51, [600, 20])
                x1_change = -(5 * 59)
            if (x9 == 6):
                screen.blit(die61, [600, 20])
                x1_change = -(6 * 59)
        x2=x2+x1_change
        x1=x1+x_change
        print(x1)

        if(x1>551 or x1<0):
            y_change=-59
            #print(x1-551)
            if(x1>551):
                z=round((x1 - 551) / 59)
                #print(z)
                x1=10+(10-z)*59
                y1 = y1 + y_change
            if(x1<10):
                if(y1>0 and y1<59):
                    x1=x1-x_change
                    y_change=0
                    y1 = y1 + y_change

                else:
                    z1=round((10-x1 ) / 59)
                    print(z1)
                    x1=10+(z1-1)*59
                    y1 = y1 + y_change
                    #print(y_change)
            #x_change=-((x1-551)/59)

            #print(y1)
            #x1 = x1 + x_change
        #print(x_change)
        #print(x1)
        if (y1 > 0 and y1 < 1 * 59):
            if (x1 >= 10 and x1<59):
                text_to_display("YoU WoN",72,WHITE,0)
                option()
                print("you won")

        if (y1 > 9 * 59 and y1 < 10 * 59):
            if (x1 > 3 * 59 and x1 < 4 * 59):
                x1 = 10 + 6 * 59
                y_change = -59
                y1 = y1 + y_change

            if (x1 > 8 * 59 and x1 < 9 * 59):
                x1 = 10 + 9 * 59
                y_change = -3 * 59
                y1 = y1 + y_change

        elif (y1 > 7 * 59 and y1 < 8 * 59):
            if (x1 > 0 and x1 <1* 59):
                x1 = 10 + (2 - 1) * 59
                y_change = -2 * 59
                #print(y_change)
                y1 = y1 + y_change
            if (x1 > 7 * 59 and x1 < 8 * 59):
                x1 = 10 + (4 - 1) * 59
                y_change = -6 * 59
                y1 = y1 + y_change
        elif(y1>4*59 and y1<5*59):
            print("i am here")
            if(x1>9*59 and x1<10*59):
                x1=10+(7-1)*59
                y_change=-59
                y1 = y1 + y_change
            if (x1 > 6 * 59 and x1 < 7 * 59):
                x1 = 10 + 6 * 59
                y_change = 2 * 59
                y1 = y1 + y_change

        elif(y1>2*59 and y1<3*59):
            if(x1>8*59 and x1<9*59):
                x1=10+9*59
                y_change=-2*59
                y1 = y1 + y_change
            if(x1>0 and x1<59):
                x1=10+(2-1)*59
                y_change=-2*59
                y1 = y1 + y_change

        elif(y1>0 and y1<59):
            if(x1>2*59 and x1<3*59):
                x1=10+(2-1)*59
                y_change=2*59
                y1 = y1 + y_change
            if(x1>5*59 and x1<6*59):
                x1=10+(5-1)*59
                y_change=2*59
                y1 = y1 + y_change
            if(x1>7*59 and x1<8*59):
                x1=10+(8-1)*59
                y_change=2*59
                y1 = y1 + y_change
        elif(y1>59 and y1<2*59):
            if(x1>6*59 and x1<7*59):
                x1=10+(5-1)*59
                y_change=5*59
                y1 = y1 + y_change
        elif(y1>3*59 and y1<4*59):
            if(x1>3*59 and x1<4*59):
                x1=10
                y_change=59
                y1 = y1 + y_change
            if(x1>1*59 and x1<2*59):
                x1=10+(2-1)*59
                y_change=5*59
                y1 = y1 + y_change
        elif(y1>8*59 and y1<9*59):
            if(x1>3*59 and x1<4*59):
                x1=10+6*59
                y_change=59
                y1 = y1 + y_change
        #elif(y1>4*59 and y1<5*59):
         #   print("i am here")

        screen.blit(ludo, [0, 0])
        for event2 in pygame.event.get():
            if event2.type==pygame.KEYDOWN:
                if event2.key==pygame.K_t:
                    comp(x2,y2,x1_change,y1_change)
        screen.blit(player, [x1, y1])

        pygame.display.update()

        #pygame.draw.rect(screen,WHITE,[100,200,100,100])

        clock.tick(10)
front_window()

pygame.quit()
quit()