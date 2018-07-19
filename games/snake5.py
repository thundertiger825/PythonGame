import pygame
import time
import  random
pygame.init()
clock=pygame.time.Clock()
display_width=800
display_height=600
WHITE=(255,255,255)
BLACK=(0,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
RED=(255,0,0)
pygame.display.set_caption("SNAKE WORLD")
FunnyImg=pygame.image.load("animals-snakes-medical_research-making_money-snake_bite-bitten_by_a_snake-cgan1811_low.jpg")
SnakeImg=pygame.image.load("Untitled8.png")
AppleImg=pygame.image.load("Untitled9.png")
Icon=pygame.image.load("3e3cb45360c1e445c8ab6fff83939daa.jpg")
Option=pygame.image.load("Untitled19.png")
sadImg=pygame.image.load("Spiral.png")
pygame.display.set_icon(Icon)
def objective():
    screen.fill((176,255,255))
    screen.blit(FunnyImg,[20,200])
    font=pygame.font.SysFont("Timesnewroman",28)
    #font4 = font.render("THERE ARE TWO LEVELS IN THIS GAME, ", True, BLACK)

    font4=font.render("YOU HAVE TO EAT AS MUCH AS CHERRIES AS YOU CAN, ",True,BLACK)
    font5=font.render("IF YOU HIT THE BOUNDARY OF WINDOW YOU LOSE",True,RED)
    font6 = font.render("IF YOU HIT THE WALLS YOU LOSE ", True, BLACK)

    screen.blit(font4,[1,10])
    screen.blit(font5,[1,50])
    screen.blit(font6, [1, 100])
    pygame.display.update()
    time.sleep(6)
    option()
def end():
    screen.fill(WHITE)
    pygame.mixer.music.load('mariobrosd_9r81556y.mp3')
    pygame.mixer.music.play(-1)

    screen.blit(sadImg,[0,0])
    text_to_display("You Lose", 72, BLUE, 50)
    text_to_display("press c to play again and q to exit", 36, RED, -50)
    pygame.display.update()
    time.sleep(2)
    restart()



def option():
    y_param = 300
    Cartoon=pygame.image.load("cartoon-snake-frame-illustration-54299249.jpg")
    screen.blit(Option, [70, y_param])
    font = pygame.font.SysFont("Comicsansms", 36)
    font1 = font.render("START ", True, RED)
    screen.blit(font1, [105, 300])
    font2 = font.render("OBJECTIVE ", True, BLACK)
    screen.blit(font2, [105, 350])
    font3=font.render("Press a after choosing your choice",True,BLUE)


    select=False
    while not select:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    y_param = 350
                if event.key == pygame.K_UP:
                    y_param = 300
                if event.key==pygame.K_a:
                    if y_param==300:
                        gameloop()
                    elif y_param==350:
                        objective()
        screen.fill(WHITE)
        screen.blit(Cartoon, [0, 0])

        screen.blit(Option, [70, y_param])
        screen.blit(font1, [105, 300])
        screen.blit(font2, [105, 350])
        screen.blit(font3, [105, 400])
        pygame.display.update()







def start_window():
    screen.fill(BLACK)
    font = pygame.font.SysFont("Comicsansms", 72)
    font1 = font.render("SNAKE WORLD " , True, RED)
    screen.blit(font1, [200, 100])
    Viper=pygame.image.load("d20bb6f128c818ce4e6a2508137ed7b9.jpg")
    screen.blit(Viper,[200,300])


    pygame.display.update()
    time.sleep(4)
    option()


def score(score1):
    font = pygame.font.SysFont("Comicsansms", 18)
    font1 = font.render("Score :"+str(score1), True, RED)
    screen.blit(font1, [1, 2])
    pygame.display.update()


def restart():
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_q:
                pygame.quit()
                quit()
            if event.key==pygame.K_c:
                gameloop()

def Level(text):
    BoundaryImg=pygame.image.load("Untitled56.png")
    BoundaryImg1 = pygame.image.load("Untitled57.png")
    screen.fill(WHITE)
    font = pygame.font.SysFont("Comicsansms", 48)
    font1 = font.render(text, True, RED)
    LevelImg=pygame.image.load("cute-snake-cartoon-illustration-55471879.jpg")
    screen.blit(font1, [10, 20])
    screen.blit(LevelImg,[-270,78])
    wallImg1 = pygame.image.load("Untitled99.png")
    wallImg2 = pygame.image.load("Untitled98.png")

    pygame.display.update()
    time.sleep(2)
    screen.fill(WHITE)
    pygame.mixer.music.load('snakemusik1.mid')
    pygame.mixer.music.play(-1)
    global direction
    Score = 5
    winscore = 40
    snakelist = []
    snakelength=1
    thingx = display_width / 2
    thingy = display_height / 2
    changex = 0
    changey = 0
    radius = 6
    thingwidth = 20
    thingheight = 10
    x_1 = round(random.randrange(30, 200-thingwidth) / 10) * 10
    y_1 = round(random.randrange(34, 400-thingheight) / 10) * 10
    x_2 = round(random.randrange(200, display_width-28) / 10) * 10
    y_2 = round(random.randrange(34, 100-thingheight) / 10) * 10
    x_3 = round(random.randrange(30, display_width-28) / 10) * 10
    y_3 = round(random.randrange(200, 400-thingheight) / 10) * 10
    x_4 = round(random.randrange(220, 500-thingwidth) / 10) * 10
    y_4 = round(random.randrange(400, 569 - thingheight) / 10) * 10
    x_5 = round(random.randrange(420, display_width - 28) / 10) * 10
    y_5 = round(random.randrange(32, 400 - thingheight) / 10) * 10

    list=[[x_1,y_1],[x_2,y_2],[x_3,y_3],[x_4,y_4],[x_5,y_5]]
    choose=random.randint(0,4)
    x=list[choose][0]
    y=list[choose][1]
    print(x_1)
    print(y_1)
    game_exit = False
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    changex = -10
                    changey = 0
                if event.key == pygame.K_RIGHT:
                    direction = "right"
                    changex = 10
                    changey = 0
                if event.key == pygame.K_UP:
                    direction = "up"
                    changey = -10
                    changex = 0
                if event.key == pygame.K_DOWN:
                    direction = "down"
                    changey = 10
                    changex = 0
                    # if event.type==pygame.KEYUP:
                    #    if event.key == pygame.K_UP or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN:
                    #       changey = 0
                    #      changex = 0

        Applewidth = 30
        thingx += changex
        thingy += changey

        if thingx > display_width-28 or thingx < 28 or thingy > 569 or thingy < 32:
            end()
        screen.fill(WHITE)
        screen.blit(BoundaryImg1, [0, 0])
        screen.blit(BoundaryImg1, [200, 0])
        screen.blit(BoundaryImg1, [400, 0])
        screen.blit(BoundaryImg1, [600, 0])
        screen.blit(BoundaryImg1, [0, 564])
        screen.blit(BoundaryImg1, [200, 564])
        screen.blit(BoundaryImg1, [400, 564])
        screen.blit(BoundaryImg1, [600, 564])

        screen.blit(BoundaryImg,[0,0])
        screen.blit(BoundaryImg, [0, 200])
        screen.blit(BoundaryImg, [0, 400])
        #screen.blit(BoundaryImg, [0, 600])
        screen.blit(BoundaryImg, [769, 0])
        screen.blit(BoundaryImg, [769, 200])
        screen.blit(BoundaryImg, [769, 400])
        #screen.blit(BoundaryImg, [769, 600])

        screen.blit(wallImg2, [200, 100])
        #screen.blit(wallImg1, [600, 10])
        screen.blit(wallImg2, [500, 400])
        screen.blit(wallImg1, [0, 400])

        snakehead = []
        snakehead.append(int(thingx))
        snakehead.append(int(thingy))
        snakelist.append(snakehead)
        if (snakelength < len(snakelist)):
            del (snakelist[0])
        screen.blit(AppleImg, (x, y))
        snake(thingwidth, snakelist)
        if (snakelength - 1 > winscore):
            win()
        score(snakelength - 1)
        for segment in snakelist[:-1]:
            if (segment == snakehead):
                text_to_display("You Collide Press q to quit or c to play again", 36, RED, 0)
                restart()

        pygame.display.update()
        # if(thingx==x and thingy==y):
        #    x = round(random.randrange(0, display_width - thingwidth) / 10) * 10
        #   y = round(random.randrange(0, display_height - thingwidth) / 10) * 10
        #  snakelength+=1
        if (thingx > x and thingx < x + Applewidth or thingx + thingwidth > x and thingx + thingwidth < x + Applewidth):
            #print("apple x")
            if (thingy > y and thingy < y + Applewidth or thingy + thingwidth > y and thingy + thingwidth < y + Applewidth):
                x_1 = round(random.randrange(30, 200 - thingwidth) / 10) * 10
                y_1 = round(random.randrange(34, 400 - thingheight) / 10) * 10
                x_2 = round(random.randrange(200, display_width - 28) / 10) * 10
                y_2 = round(random.randrange(34, 100 - thingheight) / 10) * 10
                x_3 = round(random.randrange(30, display_width - 28) / 10) * 10
                y_3 = round(random.randrange(200, 400 - thingheight) / 10) * 10
                x_4 = round(random.randrange(220, 500 - thingwidth) / 10) * 10
                y_4 = round(random.randrange(400, 569 - thingheight) / 10) * 10
                x_5 = round(random.randrange(420, display_width - 28) / 10) * 10
                y_5 = round(random.randrange(32, 400 - thingheight) / 10) * 10

                list = [[x_1, y_1], [x_2, y_2], [x_3, y_3], [x_4, y_4], [x_5, y_5]]
                choose = random.randint(0, 4)
                x = list[choose][0]
                y = list[choose][1]

                snakelength += 1
        if thingx >=0 and thingx+thingwidth<=200 or thingx<=200 and thingx>=0:
            #print("hello")
            if thingy+thingheight>400 and thingy < 456:
                end()
        if thingx >= 200 and thingx + thingwidth <= 500 or thingx <= 200 and thingx >= 500:
            #print("hello")
            if thingy +thingheight> 100 and thingy < 184:
                end()
        #if thingx >= 600 and thingx + thingwidth <= 800 or thingx <= 800 and thingx >=600:
         #   print("hello")
          #  if thingy+thingheight > 10 and thingy < 166:
           #     print(thingx,thingy)
            #    end()
        if thingx >= 500 and thingx + thingwidth <= 800 or thingx <= 800 and thingx >= 500:
            #print("hello")
            if thingy +thingheight> 400 and thingy < 484:
                end()

        clock.tick(15)





def text_to_display(text,size,color,y_displace):

    font = pygame.font.SysFont("Comicsansms", size)
    font1=font.render(text,True,color)
    screen.blit(font1,[100,display_height/2+y_displace])
    pygame.display.update()
    time.sleep(1)
#    for event in pygame.event.get():
 #       if event.type==pygame.KEYDOWN:
  #          if event.key==pygame.K_q:
   #             pygame.quit()
    #            quit()
     #       if event.key==pygame.K_c:
      #          gameloop()

screen=pygame.display.set_mode((display_width,display_height))
direction="right"
def win():
    screen.fill(WHITE)
    font = pygame.font.SysFont("Comicsansms", 48)
    font1 = font.render("YOU WON", True, BLUE)
    screen.blit(font1, [300, display_height/2 ])
    pygame.display.update()
    time.sleep(3)
    start_window()


def snake( thingwidth, snakeList):

    if direction=="right":
        head=pygame.transform.rotate(SnakeImg,270)
    if direction=="up":
        head=SnakeImg
    if direction=="down":
        head=pygame.transform.rotate(SnakeImg,180)
    if direction=="left":
        head=pygame.transform.rotate(SnakeImg,90)
    screen.blit(head,(snakeList[-1][0],snakeList[-1][1]))
    for XnY in snakeList[:-1]:
        pygame.draw.rect(screen, (34,177,76), [XnY[0], XnY[1], thingwidth, thingwidth])

def  gameloop():
    pygame.mixer.music.load('snakemusik1.mid')
    pygame.mixer.music.play(-1)
    global direction
    Score=1
    snakelength=1
    winscore=40
    snakelist=[]

    thingx = display_width / 2
    thingy = display_height / 2
    changex = 0
    changey = 0
    radius=6
    thingwidth = 20
    thingheight = 10
    x=round(random.randrange(0,display_width-thingwidth)/10)*10
    y=round(random.randrange(0,display_height-thingwidth)/10)*10
    game_exit=False
    while not game_exit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    direction="left"
                    changex=-10
                    changey=0
                if event.key==pygame.K_RIGHT:
                    direction="right"
                    changex=10
                    changey=0
                if event.key==pygame.K_UP:
                    direction="up"
                    changey=-10
                    changex=0
                if event.key==pygame.K_DOWN:
                    direction="down"
                    changey=10
                    changex=0
            #if event.type==pygame.KEYUP:
             #    if event.key == pygame.K_UP or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN:
              #       changey = 0
               #      changex = 0

        Applewidth=30



        thingx+=changex
        thingy+=changey

        if thingx > display_width or thingx < 0 or thingy > 600 or thingy < 0:
            end()
        screen.fill((255,255,255))
        snakehead=[]
        snakehead.append(int(thingx))
        snakehead.append(int(thingy))
        snakelist.append(snakehead)
        if(snakelength<len(snakelist)):
            del(snakelist[0])
        screen.blit(AppleImg,(x,y))
        snake(thingwidth,snakelist)
        if (snakelength-1>winscore):
            win()
        score(snakelength-1)
        for segment in snakelist[:-1]:
            if(segment==snakehead):
                text_to_display("You Collide Press q to quit or c to play again",36,RED,0)
                restart()

        pygame.display.update()
        #if(thingx==x and thingy==y):
        #    x = round(random.randrange(0, display_width - thingwidth) / 10) * 10
         #   y = round(random.randrange(0, display_height - thingwidth) / 10) * 10
          #  snakelength+=1
        if(thingx > x and thingx < x+Applewidth or thingx+thingwidth>x and thingx+thingwidth<x+Applewidth):
            print("apple x")
            if(thingy > y and thingy< y+Applewidth or thingy + thingwidth>y and thingy+thingwidth<y+Applewidth ):

                x = round(random.randrange(0, display_width - thingwidth) / 10) * 10
                y = round(random.randrange(0, display_height - thingwidth) / 10) * 10
                snakelength+=1
        if (snakelength - 1 == Score ):
            Level("Next Level")

        clock.tick(15)
start_window()

gameloop()

pygame.quit()
quit()