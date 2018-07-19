import pygame
pygame.init()
direction="right"
WHITE=(255,255,255)
display_width=800
display_height=600
size=(display_width,display_height)
screen=pygame.display.set_mode(size)
smileImg=pygame.image.load("happy_smiley_face_round_stickers-rbdcd90a58b8e40a9b895e7c2fd1e65ef_v9waf_8byvr_3241.jpg")
#def ludo():

def SnakeWorld():
    import pygame
    import time
    import random
    pygame.init()
    clock = pygame.time.Clock()
    display_width = 800
    display_height = 600
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    pygame.display.set_caption("SNAKE WORLD")
    FunnyImg = pygame.image.load(
        "animals-snakes-medical_research-making_money-snake_bite-bitten_by_a_snake-cgan1811_low.jpg")
    SnakeImg = pygame.image.load("Untitled8.png")
    AppleImg = pygame.image.load("Untitled9.png")
    Icon = pygame.image.load("3e3cb45360c1e445c8ab6fff83939daa.jpg")
    Option = pygame.image.load("Untitled19.png")
    sadImg = pygame.image.load("Spiral.png")
    pygame.display.set_icon(Icon)

    def objective():
        screen.fill((176, 255, 255))
        screen.blit(FunnyImg, [20, 200])
        font = pygame.font.SysFont("Timesnewroman", 28)
        # font4 = font.render("THERE ARE TWO LEVELS IN THIS GAME, ", True, BLACK)

        font4 = font.render("YOU HAVE TO EAT AS MUCH AS CHERRIES AS YOU CAN, ", True, BLACK)
        font5 = font.render("IF YOU HIT THE BOUNDARY OF WINDOW YOU LOSE", True, RED)
        font6 = font.render("IF YOU HIT THE WALLS YOU LOSE ", True, BLACK)

        screen.blit(font4, [1, 10])
        screen.blit(font5, [1, 50])
        screen.blit(font6, [1, 100])
        pygame.display.update()
        time.sleep(6)
        option()

    def end():
        screen.fill(WHITE)
        pygame.mixer.music.load('mariobrosd_9r81556y.mp3')
        pygame.mixer.music.play(-1)

        screen.blit(sadImg, [0, 0])
        text_to_display("You Lose", 72, BLUE, 50)
        text_to_display("press c to play again and q to exit", 36, RED, -50)
        pygame.display.update()
        time.sleep(2)
        restart()

    def option():
        y_param = 300
        Cartoon = pygame.image.load("cartoon-snake-frame-illustration-54299249.jpg")
        screen.blit(Option, [70, y_param])
        font = pygame.font.SysFont("Comicsansms", 36)
        font1 = font.render("START ", True, RED)
        screen.blit(font1, [105, 300])
        font2 = font.render("OBJECTIVE ", True, BLACK)
        screen.blit(font2, [105, 350])
        font3 = font.render("Press a after choosing your choice", True, BLUE)

        select = False
        while not select:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        y_param = 350
                    if event.key == pygame.K_UP:
                        y_param = 300
                    if event.key == pygame.K_a:
                        if y_param == 300:
                            gameloop()
                        elif y_param == 350:
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
        font1 = font.render("SNAKE WORLD ", True, RED)
        screen.blit(font1, [200, 100])
        Viper = pygame.image.load("d20bb6f128c818ce4e6a2508137ed7b9.jpg")
        screen.blit(Viper, [200, 300])

        pygame.display.update()
        time.sleep(4)
        option()

    def score(score1):
        font = pygame.font.SysFont("Comicsansms", 18)
        font1 = font.render("Score :" + str(score1), True, RED)
        screen.blit(font1, [1, 2])
        pygame.display.update()

    def restart():
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    gameloop()

    def Level(text):
        BoundaryImg = pygame.image.load("Untitled56.png")
        BoundaryImg1 = pygame.image.load("Untitled57.png")
        screen.fill(WHITE)
        font = pygame.font.SysFont("Comicsansms", 48)
        font1 = font.render(text, True, RED)
        LevelImg = pygame.image.load("cute-snake-cartoon-illustration-55471879.jpg")
        screen.blit(font1, [10, 20])
        screen.blit(LevelImg, [-270, 78])
        wallImg1 = pygame.image.load("Untitled99.png")
        wallImg2 = pygame.image.load("Untitled98.png")

        pygame.display.update()
        time.sleep(2)
        screen.fill(WHITE)
        global direction
        pygame.mixer.music.load('snakemusik1.mid')
        pygame.mixer.music.play(-1)

        Score = 5
        winscore = 15
        snakelist = []
        snakelength = 1
        thingx = display_width / 2
        thingy = display_height / 2
        changex = 0
        changey = 0
        radius = 6
        thingwidth = 20
        thingheight = 10
        x_1 = round(random.randrange(30, 200 - thingwidth-5) / 10) * 10
        y_1 = round(random.randrange(34, 400 - thingheight-5) / 10) * 10
        x_2 = round(random.randrange(200, display_width - 32) / 10) * 10
        y_2 = round(random.randrange(34, 100 - thingheight-5) / 10) * 10
        x_3 = round(random.randrange(30, display_width - 32) / 10) * 10
        y_3 = round(random.randrange(200, 400 - thingheight-5) / 10) * 10
        x_4 = round(random.randrange(220, 500 - thingwidth-5) / 10) * 10
        y_4 = round(random.randrange(400, 569 - thingheight-5) / 10) * 10
        x_5 = round(random.randrange(420, display_width - 32) / 10) * 10
        y_5 = round(random.randrange(32, 400 - thingheight-5) / 10) * 10

        list = [[x_1, y_1], [x_2, y_2], [x_3, y_3], [x_4, y_4], [x_5, y_5]]
        choose = random.randint(0, 4)
        x = list[choose][0]
        y = list[choose][1]
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

            if thingx > display_width - 28 or thingx < 28 or thingy > 569 or thingy < 32:
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

            screen.blit(BoundaryImg, [0, 0])
            screen.blit(BoundaryImg, [0, 200])
            screen.blit(BoundaryImg, [0, 400])
            # screen.blit(BoundaryImg, [0, 600])
            screen.blit(BoundaryImg, [769, 0])
            screen.blit(BoundaryImg, [769, 200])
            screen.blit(BoundaryImg, [769, 400])
            # screen.blit(BoundaryImg, [769, 600])

            screen.blit(wallImg2, [200, 100])
            # screen.blit(wallImg1, [600, 10])
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
            if (
                        thingx > x and thingx < x + Applewidth or thingx + thingwidth > x and thingx + thingwidth < x + Applewidth):
                # print("apple x")
                if (
                            thingy > y and thingy < y + Applewidth or thingy + thingwidth > y and thingy + thingwidth < y + Applewidth):
                    x_1 = round(random.randrange(30, 200 - thingwidth-5) / 10) * 10
                    y_1 = round(random.randrange(34, 400 - thingheight-5) / 10) * 10
                    x_2 = round(random.randrange(200, display_width - 32) / 10) * 10
                    y_2 = round(random.randrange(34, 100 - thingheight-5) / 10) * 10
                    x_3 = round(random.randrange(30, display_width - 32) / 10) * 10
                    y_3 = round(random.randrange(200, 400 - thingheight-5) / 10) * 10
                    x_4 = round(random.randrange(220, 500 - thingwidth-5) / 10) * 10
                    y_4 = round(random.randrange(400, 569 - thingheight-5) / 10) * 10
                    x_5 = round(random.randrange(420, display_width - 32) / 10) * 10
                    y_5 = round(random.randrange(32, 400 - thingheight-5) / 10) * 10

                    list = [[x_1, y_1], [x_2, y_2], [x_3, y_3], [x_4, y_4], [x_5, y_5]]
                    choose = random.randint(0, 4)
                    x = list[choose][0]
                    y = list[choose][1]

                    snakelength += 1
            if thingx >= 0 and thingx + thingwidth <= 200 or thingx <= 200 and thingx >= 0:
                # print("hello")
                if thingy + thingheight > 400 and thingy < 456:
                    end()
            if thingx >= 200 and thingx + thingwidth <= 500 or thingx <= 200 and thingx >= 500:
                # print("hello")
                if thingy + thingheight > 100 and thingy < 184:
                    end()
                    # if thingx >= 600 and thingx + thingwidth <= 800 or thingx <= 800 and thingx >=600:
                    #   print("hello")
                    #  if thingy+thingheight > 10 and thingy < 166:
                    #     print(thingx,thingy)
                    #    end()
            if thingx >= 500 and thingx + thingwidth <= 800 or thingx <= 800 and thingx >= 500:
                # print("hello")
                if thingy + thingheight > 400 and thingy < 484:
                    end()

            clock.tick(15)

    def text_to_display(text, size, color, y_displace):

        font = pygame.font.SysFont("Comicsansms", size)
        font1 = font.render(text, True, color)
        screen.blit(font1, [100, display_height / 2 + y_displace])
        pygame.display.update()
        time.sleep(1)
        #    for event in pygame.event.get():
        #       if event.type==pygame.KEYDOWN:
        #          if event.key==pygame.K_q:
        #             pygame.quit()
        #            quit()
        #       if event.key==pygame.K_c:
        #          gameloop()

    screen = pygame.display.set_mode((display_width, display_height))
    #direction = "right"

    def win():
        screen.fill(RED)
        font = pygame.font.SysFont("Comicsansms", 48)
        font1 = font.render("YOU WON", True, BLUE)
        screen.blit(font1, [300, display_height / 2])
        pygame.display.update()
        time.sleep(3)
        start_window()

    def snake(thingwidth, snakeList):

        if direction == "right":
            head = pygame.transform.rotate(SnakeImg, 270)
        if direction == "up":
            head = SnakeImg
        if direction == "down":
            head = pygame.transform.rotate(SnakeImg, 180)
        if direction == "left":
            head = pygame.transform.rotate(SnakeImg, 90)
        screen.blit(head, (snakeList[-1][0], snakeList[-1][1]))
        for XnY in snakeList[:-1]:
            pygame.draw.rect(screen, (34, 177, 76), [XnY[0], XnY[1], thingwidth, thingwidth])

    def gameloop():

        pygame.mixer.music.load('snakemusik1.mid')
        pygame.mixer.music.play(-1)
        global direction
        Score = 10
        snakelength = 1
        winscore = 40
        snakelist = []

        thingx = display_width / 2
        thingy = display_height / 2
        changex = 0
        changey = 0
        radius = 6
        thingwidth = 20
        thingheight = 10
        x = round(random.randrange(0, display_width - thingwidth) / 10) * 10
        y = round(random.randrange(0, display_height - thingwidth) / 10) * 10
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

            if thingx > display_width or thingx < 0 or thingy > 600 or thingy < 0:
                end()
            screen.fill((255, 255, 255))
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
            if (
                        thingx > x and thingx < x + Applewidth or thingx + thingwidth > x and thingx + thingwidth < x + Applewidth):
                print("apple x")
                if (
                            thingy > y and thingy < y + Applewidth or thingy + thingwidth > y and thingy + thingwidth < y + Applewidth):
                    x = round(random.randrange(0, display_width - thingwidth) / 10) * 10
                    y = round(random.randrange(0, display_height - thingwidth) / 10) * 10
                    snakelength += 1
            if (snakelength - 1 == Score):
                Level("Next Level")

            clock.tick(15)

    start_window()

    gameloop()

    pygame.quit()
    quit()
def Shield():
    import pygame
    import time
    import random
    pygame.init()
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 155, 0)
    blue = (0, 0, 255)
    navy = (135, 57, 232)
    display_width = 800
    display_height = 600
    icon = pygame.image.load('rr.png')  # 32x32
    pygame.display.set_icon(icon)
    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('SHIELD')
    smallfont = pygame.font.SysFont("comicsansms", 20)
    medfont = pygame.font.SysFont("comicsansms", 50)
    largefont = pygame.font.SysFont("comicsansms", 80)
    lead_x_change = 0
    gameDisplay.fill(white)
    img = pygame.image.load('roman.png')
    left = pygame.image.load('romanl.png')
    right = pygame.image.load('leftroman.png')
    bary = pygame.image.load('bary.png')
    amb = pygame.image.load('latamb.png')
    rollins = pygame.image.load('seth.png')
    shield = pygame.image.load('snew.png')

    clock = pygame.time.Clock()
    count = 0

    height = int(display_height / 7)

    def barrier(barr_x):
        gameDisplay.blit(bary, (barr_x, height + 3))
        gameDisplay.blit(bary, (barr_x + 580, height + 3))
        gameDisplay.blit(bary, (barr_x + 300, height * 2 + 3))
        gameDisplay.blit(bary, (barr_x, height * 3 + 3))
        gameDisplay.blit(bary, (barr_x + 580, height * 3 + 3))
        gameDisplay.blit(bary, (barr_x + 50, height * 4 + 3))
        gameDisplay.blit(bary, (barr_x + 600, height * 4 + 3))
        gameDisplay.blit(bary, (barr_x + 300, height * 5 + 3))

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

    def design(rectlist):
        height = int(display_height / 7)
        if rectlist[0] == 't':
            pygame.draw.rect(gameDisplay, blue, (10, 10, 60, (height - 10) + 2))
        else:
            pygame.draw.rect(gameDisplay, (92, 46, 6),
                             (10, 10, 60, (height - 10) + 2))  # (topleftcordinates,width,heigjt)
        if rectlist[1] == 't':
            pygame.draw.rect(gameDisplay, blue, (730, 10, 60, (height - 10) + 2))
        else:
            pygame.draw.rect(gameDisplay, (92, 46, 6), (730, 10, 60, height - 10))
        if rectlist[3] == 't':
            pygame.draw.rect(gameDisplay, blue, (40, height * 2 + 10, 60, height - 10))
        else:
            pygame.draw.rect(gameDisplay, (92, 46, 6), (40, height * 2 + 10, 60, height - 10))
        if rectlist[2] == 't':
            pygame.draw.rect(gameDisplay, blue, (430, height + 10, 60, height - 10))
        else:
            pygame.draw.rect(gameDisplay, (92, 46, 6), (430, height + 10, 60, height - 10))
        if rectlist[4] == 't':
            pygame.draw.rect(gameDisplay, blue, (700, height * 2 + 10, 60, height - 10))
        else:
            pygame.draw.rect(gameDisplay, (92, 46, 6), (700, height * 2 + 10, 60, height - 10))
        if rectlist[5] == 't':
            pygame.draw.rect(gameDisplay, blue, (250, height * 3 + 10, 60, height - 10))
        else:
            pygame.draw.rect(gameDisplay, (92, 46, 6), (250, height * 3 + 10, 60, height - 10))
        if rectlist[6] == 't':
            pygame.draw.rect(gameDisplay, blue, (40, height * 5 + 10, 60, height - 10))
        else:
            pygame.draw.rect(gameDisplay, (92, 46, 6), (40, height * 5 + 10, 60, height - 10))
        if rectlist[7] == 't':
            pygame.draw.rect(gameDisplay, blue, (700, height * 6 + 10, 60, height - 10))
        else:
            pygame.draw.rect(gameDisplay, (92, 46, 6), (700, height * 6 + 10, 60, height - 10))

        pygame.draw.line(gameDisplay, black, (0, height), (100, height), 5)
        pygame.draw.line(gameDisplay, black, (150, height), (650, height), 5)
        pygame.draw.line(gameDisplay, black, (700, height), (800, height), 5)

        pygame.draw.line(gameDisplay, black, (0, height * 2), (250, height * 2), 5)
        pygame.draw.line(gameDisplay, black, (300, height * 2), (600, height * 2), 5)
        pygame.draw.line(gameDisplay, black, (650, height * 2), (800, height * 2), 5)
        pygame.draw.line(gameDisplay, black, (0, height * 3), (375, height * 3), 5)
        pygame.draw.line(gameDisplay, black, (425, height * 3), (800, height * 3), 5)
        pygame.draw.line(gameDisplay, black, (0, height * 4), (100, height * 4), 5)
        pygame.draw.line(gameDisplay, black, (150, height * 4), (650, height * 4), 5)
        pygame.draw.line(gameDisplay, black, (700, height * 4), (800, height * 4), 5)
        pygame.draw.line(gameDisplay, black, (0, height * 5), (250, height * 5), 5)
        pygame.draw.line(gameDisplay, black, (300, height * 5), (600, height * 5), 5)
        pygame.draw.line(gameDisplay, black, (650, height * 5), (800, height * 5), 5)
        pygame.draw.line(gameDisplay, black, (0, height * 6), (375, height * 6), 5)
        pygame.draw.line(gameDisplay, black, (425, height * 6), (800, height * 6), 5)

    def text_objects(text, color, size):
        if size is "small":
            textSurface = smallfont.render(text, True, color)
        if size is "medium":
            textSurface = medfont.render(text, True, color)
        if size is "large":
            textSurface = largefont.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def messeage_to_screen(msg, color, y_displace=0, size="small"):
        textSurf, textRect = text_objects(msg, color, size)
        textRect.center = (display_width / 2), (display_height / 2) + y_displace
        gameDisplay.blit(textSurf, textRect)

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
                        quit()
            gameDisplay.fill((34, 26, 68))
            gameDisplay.blit(shield, (250, 100))
            messeage_to_screen("Welcome to SHIELD ", green, -250, "small")
            messeage_to_screen("AIM:Starting as 1 member of shield try to find other two members ", white, 160)
            messeage_to_screen("of shield by visiting each door in a given Time without touching spikes.", white, 180)
            messeage_to_screen("WARNING :If you touch any spike or time is over your game will be over", red, 200)
            messeage_to_screen("CONTROLS: Press C to play,P to pause,E to enter a door or Q to quit ,Press <-  ,",
                               white, 220)
            messeage_to_screen("to go LEFT,->to go right,up arrow key to go up and down arrow key to go down", white,
                               240)

            pygame.display.update()
            clock.tick(15)

    def game_loop():
        pygame.mixer.music.load("shm_vav.wav")

        pygame.mixer.music.play(-1)
        romandirection = 'front'
        rectlist = ['f', 'f', 'f', 'f', 'f', 'f', 'f', 'f']
        ambrose = random.randrange(1, 9)
        seth = random.randrange(1, 9)
        print(ambrose)
        frame = 0
        print(seth)
        ambfound = False
        sethfound = False
        gameOver = False
        gameExit = False
        bardirection = 'RIGHT'
        bar_x = 20
        lead_x = 400
        lead_y = height * 3 + 10
        lead_x_change = 0
        won = False
        while not gameExit:
            frame = frame + 1
            count = int(frame / 15)
            while gameOver == True:
                gameDisplay.fill((141, 0, 0))
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
                gameDisplay.fill((0, 159, 0))
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
            if bar_x == 180:
                bar_x -= 5
                bardirection = 'LEFT'
            if bar_x == 0:
                bar_x += 5
                bardirection = 'RIGHT'

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit == True
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
                        if lead_y == 10:
                            lead_y_change = 0
                        elif lead_y == height + 10:
                            if ((lead_x > 0 and lead_x < 100) or (lead_x + 30 > 0 and lead_x + 30 < 100)) or (
                                        (lead_x > 150 and lead_x < 650) or (
                                                        lead_x + 30 > 150 and lead_x + 30 < 650)) or (
                                        (lead_x > 700 and lead_x < 800) or (lead_x + 30 > 700 and lead_x + 30 < 800)):
                                lead_y_change = 0
                            else:
                                lead_y_change += -height
                                lead_x_change = 0
                        elif lead_y == height * 2 + 10:
                            if ((lead_x > 0 and lead_x < 250) or (lead_x + 30 > 0 and lead_x + 30 < 250)) or (
                                        (lead_x > 300 and lead_x < 600) or (
                                                        lead_x + 30 > 300 and lead_x + 30 < 600)) or (
                                        (lead_x > 650 and lead_x < 800) or (lead_x + 30 > 650 and lead_x + 30 < 800)):
                                lead_y_change = 0
                            else:
                                lead_y_change += -height
                                lead_x_change = 0
                        elif lead_y == height * 3 + 10:
                            if ((lead_x > 0 and lead_x < 375) or (lead_x + 30 > 0 and lead_x + 30 < 375)) or (
                                        (lead_x > 425 and lead_x < 800) or (
                                                        lead_x + 30 > 425 and lead_x + 30 < 800)):
                                lead_y_change = 0
                            else:
                                lead_y_change += -height
                                lead_x_change = 0
                        elif lead_y == height * 4 + 10:
                            if ((lead_x > 0 and lead_x < 100) or (lead_x + 30 > 0 and lead_x + 30 < 100)) or (
                                        (lead_x > 150 and lead_x < 650) or (
                                                        lead_x + 30 > 150 and lead_x + 30 < 650)) or (
                                        (lead_x > 700 and lead_x < 800) or (lead_x + 30 > 700 and lead_x + 30 < 800)):
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
                            if ((lead_x > 0 and lead_x < 100) or (lead_x + 30 > 0 and lead_x + 30 < 100)) or (
                                        (lead_x > 150 and lead_x < 650) or (
                                                        lead_x + 30 > 150 and lead_x + 30 < 650)) or (
                                        (lead_x > 700 and lead_x < 800) or (lead_x + 30 > 700 and lead_x + 30 < 800)):
                                lead_y_change = 0
                            else:
                                lead_y_change += height
                                lead_x_change = 0
                        elif lead_y == height + 10:
                            if ((lead_x > 0 and lead_x < 250) or (lead_x + 30 > 0 and lead_x + 30 < 250)) or (
                                        (lead_x > 300 and lead_x < 600) or (
                                                        lead_x + 30 > 300 and lead_x + 30 < 600)) or (
                                        (lead_x > 650 and lead_x < 800) or (lead_x + 30 > 650 and lead_x + 30 < 800)):
                                lead_y_change = 0
                            else:
                                lead_y_change += height
                                lead_x_change = 0
                        elif lead_y == height * 2 + 10:
                            if ((lead_x > 0 and lead_x < 375) or (lead_x + 30 > 0 and lead_x + 30 < 375)) or (
                                        (lead_x > 425 and lead_x < 800) or (
                                                        lead_x + 30 > 425 and lead_x + 30 < 800)):
                                lead_y_change = 0
                            else:
                                lead_y_change += height
                                lead_x_change = 0
                        elif lead_y == height * 3 + 10:
                            if ((lead_x > 0 and lead_x < 100) or (lead_x + 30 > 0 and lead_x + 30 < 100)) or (
                                        (lead_x > 150 and lead_x < 650) or (
                                                        lead_x + 30 > 150 and lead_x + 30 < 650)) or (
                                        (lead_x > 700 and lead_x < 800) or (lead_x + 30 > 700 and lead_x + 30 < 800)):
                                lead_y_change = 0
                            else:
                                lead_y_change += height
                                lead_x_change = 0
                        elif lead_y == height * 4 + 10:
                            if ((lead_x > 0 and lead_x < 250) or (lead_x + 30 > 0 and lead_x + 30 < 250)) or (
                                        (lead_x > 300 and lead_x < 600) or (
                                                        lead_x + 30 > 300 and lead_x + 30 < 600)) or (
                                        (lead_x > 650 and lead_x < 800) or (lead_x + 30 > 650 and lead_x + 30 < 800)):
                                lead_y_change = 0
                            else:
                                lead_y_change += height
                                lead_x_change = 0
                        elif lead_y == height * 5 + 10:
                            if ((lead_x > 0 and lead_x < 375) or (lead_x + 30 > 0 and lead_x + 30 < 375)) or (
                                        (lead_x > 425 and lead_x < 800) or (
                                                        lead_x + 30 > 425 and lead_x + 30 < 800)):
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
                        if lead_y == 10:
                            if ambrose == seth:
                                ambfound = True
                                sethfound = True
                            elif (lead_x >= 10 and lead_x + 30 <= 70):
                                rectlist[0] = 't'
                                if (ambrose == 1):
                                    ambfound = True
                                elif (seth == 1):
                                    sethfound = True

                            elif (lead_x >= 730 and lead_x + 30 <= 790):
                                rectlist[1] = 't'
                                if (ambrose == 2):
                                    ambfound = True
                                if (seth == 2):
                                    sethfound = True

                        elif lead_y == height + 10:
                            if ambrose == seth:
                                ambfound = True
                                sethfound = True
                            elif (lead_x >= 430 and lead_x + 30 <= 490):
                                rectlist[2] = 't'
                                if (ambrose == 3):
                                    ambfound = True
                                if (seth == 3):
                                    sethfound = True
                        elif lead_y == height * 2 + 10:
                            if ambrose == seth:
                                ambfound = True
                                sethfound = True
                            elif (lead_x >= 40 and lead_x + 30 <= 100):
                                rectlist[3] = 't'
                                if (ambrose == 4):
                                    ambfound = True
                                if (seth == 4):
                                    sethfound = True
                            elif (lead_x > 700 and lead_x + 30 < 760):
                                rectlist[4] = 't'
                                if (ambrose == 5):
                                    ambfound = True
                                if (seth == 5):
                                    sethfound = True
                        elif lead_y == height * 3 + 10:
                            if ambrose == seth:
                                ambfound = True
                                sethfound = True
                            elif (lead_x >= 250 and lead_x + 30 <= 310):
                                rectlist[5] = 't'
                                if (ambrose == 6):
                                    ambfound = True
                                if (seth == 6):
                                    sethfound = True
                        elif lead_y == height * 5 + 10:
                            if ambrose == seth:
                                ambfound = True
                                sethfound = True
                            elif (lead_x >= 40 and lead_x + 30 <= 100):
                                rectlist[6] = 't'
                                if (ambrose == 7):
                                    ambfound = True
                                if (seth == 7):
                                    sethfound = True
                        elif lead_y == height * 6 + 10:
                            if ambrose == seth:
                                ambfound = True
                                sethfound = True
                            elif (lead_x >= 700 and lead_x + 30 <= 760):
                                rectlist[7] = 't'
                                if (ambrose == 8):
                                    ambfound = True
                                if (seth == 8):
                                    sethfound = True
                    if event.key == pygame.K_p:
                        pause()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        lead_x_change = 0

            if (lead_x + 30 == bar_x and lead_y == height + 10) or (lead_x == bar_x + 20 and lead_y == height + 10):
                gameOver = True
            if (lead_x + 30 == bar_x + 580 and lead_y == height + 10) or (
                    lead_x == bar_x + 580 + 20 and lead_y == height + 10):
                gameOver = True
            if (lead_x + 30 == bar_x + 300 and lead_y == height * 2 + 10) or (
                    lead_x == bar_x + 300 + 20 and lead_y == height * 2 + 10):
                gameOver = True
            if (lead_x + 30 == bar_x + 50 and lead_y == height * 4 + 10) or (
                    lead_x == bar_x + 50 + 20 and lead_y == height * 4 + 10):
                gameOver = True
            if (lead_x + 30 == bar_x + 600 and lead_y == height * 4 + 10) or (
                            lead_x == bar_x + 600 + 20 and lead_y == height * 4 + 10):
                gameOver = True

            if (lead_x + 30 == bar_x and lead_y == height * 3 + 10) or (
                    lead_x == bar_x + 20 and lead_y == height * 3 + 10):
                gameOver = True
            if (lead_x + 30 == bar_x + 580 and lead_y == height * 3 + 10) or (
                            lead_x == bar_x + 580 + 20 and lead_y == height * 3 + 10):
                gameOver = True
            if (lead_x + 30 == bar_x + 300 and lead_y == height * 5 + 10) or (
                            lead_x == bar_x + 300 + 20 and lead_y == height * 5 + 10):
                gameOver = True

            sec = 60 - count
            if sec is 0:
                gameOver = True
            lead_x += lead_x_change

            lead_y += lead_y_change
            gameDisplay.fill(white)
            design(rectlist)
            # pygame.draw.rect(gameDisplay, black, (lead_x,lead_y , 60, height - 10))
            if romandirection == 'front':
                gameDisplay.blit(img, (lead_x, lead_y))
            elif romandirection == 'left':
                gameDisplay.blit(left, (lead_x, lead_y - 5))
            elif romandirection == 'right':
                gameDisplay.blit(img, (lead_x, lead_y))

            barrier(bar_x)
            if ambfound == True and sethfound == True:
                gameDisplay.blit(amb, (lead_x - 10, lead_y + 10))
                gameDisplay.blit(rollins, (lead_x + 10, lead_y + 10))
                won = True
            if sethfound == True:
                gameDisplay.blit(rollins, (lead_x + 25, lead_y + 8))

            if ambfound == True:
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
def ludo():
    import time
    import pygame
    import random
    pygame.init()
    clock = pygame.time.Clock()
    display_width = 800
    display_height = 600
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    screen = pygame.display.set_mode((display_width, display_height))
    die1 = pygame.image.load('Untitled8781.png')
    die2 = pygame.image.load('Untitled8782.png')
    die3 = pygame.image.load('Untitled8783.png')
    die4 = pygame.image.load('Untitled8784.png')
    die5 = pygame.image.load('Untitled8785.png')
    die6 = pygame.image.load('Untitled8786.png')
    player = pygame.image.load(
        'happy_smiley_face_round_stickers-rbdcd90a58b8e40a9b895e7c2fd1e65ef_v9waf_8byvr_3241.jpg')
    ludo = pygame.image.load('stock-vector-snakes-and-ladders-board-game-snakes-ladders-start-finish-163384724.jpg')

    def text_to_display(text, size, color, y_displace):
        screen.fill(BLUE)
        font = pygame.font.SysFont("Comicsansms", size)
        font1 = font.render(text, True, color)
        screen.blit(font1, [40, display_height / 4 + y_displace])
        pygame.display.update()
        time.sleep(1)

    front_img = pygame.image.load("Unnamed.png")

    def front_window():
        screen.fill(WHITE)
        font = pygame.font.SysFont("Comicsansms", 48)
        font1 = font.render("Snake and Ladders", True, BLUE)
        font3 = pygame.font.SysFont("Comicsansms", 36)
        font2 = font3.render("Press 'a' to roll a die", True, (0, 0, 0))
        screen.blit(font1, [40, 500])
        screen.blit(front_img, [200, 0])
        screen.blit(font2, [50, 550])
        pygame.display.update()
        time.sleep(3)
        screen.fill(BLUE)

        gameloop()

    def option():
        text_to_display("Press q to quit or a to play again", 48, WHITE, 0)
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_a):
                    gameloop()
                if (event.key == pygame.K_q):
                    pygame.quit()
                    quit()

    cond = 0

    def gameloop():
        pygame.mixer.music.load('08-china-great-wall.mp3')
        pygame.mixer.music.play(-1)

        global cond
        x1 = 10
        y1 = 549
        x2 = 600
        y2 = 500
        x_change = 0
        y_change = 0
        Exit = False
        screen.blit(ludo, [0, 0])
        screen.blit(die1, [600, 200])
        # screen.blit(player,[x2,y2])
        pygame.display.update()

        # screen.fill(BLUE)
        while not Exit:
            x_change = 0
            y_change = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYUP:
                    x_change = 0
                    y_change = 0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        x = random.randint(1, 6)
                        if ((y1 > 59 and y1 < 2 * 59) or (y1 > 3 * 59 and y1 < 4 * 49) or (
                                y1 > 5 * 59 and y1 < 6 * 59) or (y1 > 7 * 59 and y1 < 8 * 59) or (
                                y1 > 9 * 59 and y1 < 10 * 59)):
                            if (x == 1):
                                x_change = 1 * 59
                                screen.blit(die1, [600, 200])
                            if (x == 2):
                                screen.blit(die2, [600, 200])
                                x_change = 2 * 59
                            if (x == 3):
                                screen.blit(die3, [600, 200])
                                x_change = 3 * 59
                            if (x == 4):
                                screen.blit(die4, [600, 200])
                                x_change = 4 * 59
                            if (x == 5):
                                screen.blit(die5, [600, 200])
                                x_change = 5 * 59
                            if (x == 6):
                                screen.blit(die6, [600, 200])
                                x_change = 6 * 59
                        if ((y1 > 0 and y1 < 1 * 59) or (y1 > 2 * 59 and y1 < 3 * 49) or (
                                y1 > 4 * 59 and y1 < 5 * 59) or (y1 > 6 * 59 and y1 < 7 * 59) or (
                                y1 > 8 * 59 and y1 < 9 * 59)):
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

            x1 = x1 + x_change
            print(x1)
            if (x1 > 551 or x1 < 0):
                y_change = -59
                # print(x1-551)
                if (x1 > 551):
                    z = round((x1 - 551) / 59)
                    # print(z)
                    x1 = 10 + (10 - z) * 59
                    y1 = y1 + y_change
                if (x1 < 10):
                    if (y1 > 0 and y1 < 59):
                        x1 = x1 - x_change
                        y_change = 0
                        y1 = y1 + y_change

                    else:
                        z1 = round((10 - x1) / 59)
                        print(z1)
                        x1 = 10 + (z1 - 1) * 59
                        y1 = y1 + y_change
                        # print(y_change)
                        # x_change=-((x1-551)/59)

                        # print(y1)
                        # x1 = x1 + x_change
            # print(x_change)
            # print(x1)
            if (y1 > 0 and y1 < 1 * 59):
                if (x1 >= 10 and x1 < 59):
                    text_to_display("YoU WoN", 72, WHITE, 0)
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
                if (x1 > 0 and x1 < 1 * 59):
                    x1 = 10 + (2 - 1) * 59
                    y_change = -2 * 59
                    # print(y_change)
                    y1 = y1 + y_change
                if (x1 > 7 * 59 and x1 < 8 * 59):
                    x1 = 10 + (4 - 1) * 59
                    y_change = -6 * 59
                    y1 = y1 + y_change
            elif (y1 > 4 * 59 and y1 < 5 * 59):
                print("i am here")
                if (x1 > 9 * 59 and x1 < 10 * 59):
                    x1 = 10 + (7 - 1) * 59
                    y_change = -59
                    y1 = y1 + y_change
                if (x1 > 6 * 59 and x1 < 7 * 59):
                    x1 = 10 + 6 * 59
                    y_change = 2 * 59
                    y1 = y1 + y_change

            elif (y1 > 2 * 59 and y1 < 3 * 59):
                if (x1 > 8 * 59 and x1 < 9 * 59):
                    x1 = 10 + 9 * 59
                    y_change = -2 * 59
                    y1 = y1 + y_change
                if (x1 > 0 and x1 < 59):
                    x1 = 10 + (2 - 1) * 59
                    y_change = -2 * 59
                    y1 = y1 + y_change

            elif (y1 > 0 and y1 < 59):
                if (x1 > 2 * 59 and x1 < 3 * 59):
                    x1 = 10 + (2 - 1) * 59
                    y_change = 2 * 59
                    y1 = y1 + y_change
                if (x1 > 5 * 59 and x1 < 6 * 59):
                    x1 = 10 + (5 - 1) * 59
                    y_change = 2 * 59
                    y1 = y1 + y_change
                if (x1 > 7 * 59 and x1 < 8 * 59):
                    x1 = 10 + (8 - 1) * 59
                    y_change = 2 * 59
                    y1 = y1 + y_change
            elif (y1 > 59 and y1 < 2 * 59):
                if (x1 > 6 * 59 and x1 < 7 * 59):
                    x1 = 10 + (5 - 1) * 59
                    y_change = 5 * 59
                    y1 = y1 + y_change
            elif (y1 > 3 * 59 and y1 < 4 * 59):
                if (x1 > 3 * 59 and x1 < 4 * 59):
                    x1 = 10
                    y_change = 59
                    y1 = y1 + y_change
                if (x1 > 1 * 59 and x1 < 2 * 59):
                    x1 = 10 + (2 - 1) * 59
                    y_change = 5 * 59
                    y1 = y1 + y_change
            elif (y1 > 8 * 59 and y1 < 9 * 59):
                if (x1 > 3 * 59 and x1 < 4 * 59):
                    x1 = 10 + 6 * 59
                    y_change = 59
                    y1 = y1 + y_change
                    # elif(y1>4*59 and y1<5*59):
                    #   print("i am here")

            screen.blit(ludo, [0, 0])

            screen.blit(player, [x1, y1])
            # pygame.display.update()

            # pygame.draw.rect(screen,WHITE,[100,200,100,100])
            pygame.display.update()
            clock.tick(10)

    front_window()

    pygame.quit()
    quit()
RED=(255,0,0)
BLACK=(0,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
Frontimg=pygame.image.load("130b270b3079a6520fb61d2b9cbbfbe8.jpg")
def first_screen():
    y_param = 300

    #Cartoon = pygame.image.load("cartoon-snake-frame-illustration-54299249.jpg")
    screen.blit(smileImg, [70, y_param])
    font = pygame.font.SysFont("Comicsansms", 36)
    font6 = pygame.font.SysFont("Comicsansms", 24)
    font7 = pygame.font.SysFont("Comicsansms", 72)
    font4=font7.render("3 GAMES in 1 ",True,GREEN)
    font1 = font.render("Snake World ", True, RED)
    screen.blit(font1, [105, 300])
    font2 = font.render("SHIELD", True, WHITE)
    screen.blit(font2, [105, 350])
    font67=font.render("Snake and Ladder",True,BLUE)
    screen.blit(font67,[105,400])
    font3 = font6.render("""Press 'a' after choosing your choice""", True, GREEN)
    pygame.mixer.music.load('Rock.mp3')
    pygame.mixer.music.play(-1)

    select = False
    while not select:
        y_change=0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    y_change = 50
                if event.key == pygame.K_UP:
                    y_change=-50
                if event.key == pygame.K_a:
                    if y_param == 300:
                        SnakeWorld()
                    elif y_param == 350:
                        Shield()
                    elif y_param==400:
                        print("hello")
                        ludo()
        y_param=y_param+y_change
        if(y_param>400 or y_param<300):
            y_param=y_param-y_change
        screen.fill(BLACK)
        #screen.blit(Cartoon, [0, 0])
        screen.blit(Frontimg,[300,5])
        screen.blit(smileImg, [30, y_param])
        screen.blit(font1, [105, 300])
        screen.blit(font2, [105, 350])
        screen.blit(font4, [200, 150])
        screen.blit(font3, [205, 500])
        screen.blit(font67, [105, 400])
        pygame.display.update()

first_screen()


