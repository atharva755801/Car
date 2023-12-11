from ctypes import py_object

import pygame,time,sys,random
pygame.init()
gray=(127,127,127)
black=(0,0,0)
red=(255,0,0)
green=(11,107,2)
blue=(0,0,200)
bright_red=(255,50,50)
bright_green=(0,255,0)
bright_blue=(0,0,255)
display_width=800
display_height=600



gamedisplays=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("car game")
clock=pygame.time.Clock()
carimg=pygame.image.load('car1.jpg')
boom=pygame.image.load('source.gif')
backgroundpic=pygame.image.load("download12.jpg")
backgroundpic1=pygame.image.load("download121.jpg")
yellow_strip=pygame.image.load("yellow strip.jpg")
strip=pygame.image.load("strip.jpg")
intro_background=pygame.image.load("intro.jpg")
instruction_background=pygame.image.load("instruction.jpg")
car_width=56
pause=False

#defining function for choosing map
def theme():
    theme = True
    while theme:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(backgroundpic, (0, 0))
        gamedisplays.blit(backgroundpic, (100, 0))
        gamedisplays.blit(backgroundpic, (200, 0))
        gamedisplays.blit(backgroundpic, (300, 0))
        gamedisplays.blit(backgroundpic1, (400, 0))
        gamedisplays.blit(backgroundpic1, (500, 0))
        gamedisplays.blit(backgroundpic1, (600, 0))
        gamedisplays.blit(backgroundpic1, (700, 0))
        largetext = pygame.font.SysFont('impact', 115)
        TextSurf, TextRect = text_objects("MAP", largetext)
        TextRect.center = (400, 100)
        gamedisplays.blit(TextSurf, TextRect)
        button("BACK", 0, 0, 100, 50, green, bright_green, "menu")
        button("Grass", 150, 520, 100, 50, green, bright_green, "play1")
        button("Snow", 550, 520, 100, 50, red, bright_red, "play2")

        pygame.display.update()
        clock.tick(50)

#defining function for intro screen
def intro_loop():
    intro=True
    
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(intro_background,(0,0))
        largetext=pygame.font.SysFont('forte',115)
        TextSurf,TextRect=text_objects("CAR GAME",largetext)
        TextRect.center=(400,100)
        gamedisplays.blit(TextSurf,TextRect)
        button("START",130,350,100,50,green,bright_green,"themee")
        button("QUIT",130,520,100,50,red,bright_red,"quit")
        button("INSTRUCTION",85,440,200,50,blue,bright_blue,"intro")
        pygame.display.update()
        clock.tick(50)

#defining function for pausing the function
def paused():
    global pause

    while pause:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            gamedisplays.blit(instruction_background,(0,0))
            largetext=pygame.font.SysFont('impact',115)
            TextSurf,TextRect=text_objects("PAUSED",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            button("Continue",150,450,150,50,green,bright_green,"unpause")
            button("RESTART",350,450,150,50,blue,bright_blue,"themee")
            button("MAIN MENU",550,450,200,50,red,bright_red,"menu")
            pygame.display.update()
            clock.tick(30)


def unpaused():
    global pause
    pause=False


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(gamedisplays,ac,(x,y,w,h))
        if click[0]==1 and action!=None:

            if action=="play1":
                game_loop()
            elif action=="play2":
                game_loop1()
            elif action=="themee":
                theme()
            elif action=="quit":
                pygame.quit()
                quit()
                sys.exit()
            elif action=="intro":
                instruction()
            elif action=="menu":
                intro_loop()
            elif action == "unpause":
                unpaused()



    else:
        pygame.draw.rect(gamedisplays,ic,(x,y,w,h))
    smalltext=pygame.font.SysFont("Showcard Gothic",20)
    textsurf,textrect=text_objects(msg,smalltext)
    textrect.center=((x+(w/2)),(y+(h/2)))
    gamedisplays.blit(textsurf,textrect)


def instruction():
    instruction=True
    while instruction:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(instruction_background,(0,0))
        largetext=pygame.font.SysFont('impact',80)
        smalltext=pygame.font.SysFont('impact',20)
        mediumtext=pygame.font.SysFont('impact',40)
        textSurf,textRect=text_objects("This is an car game in which you need dodge the coming obstacles",smalltext)
        textRect.center=((350),(200))
        TextSurf,TextRect=text_objects("INSTRUCTION",largetext)
        TextRect.center=((400),(100))
        gamedisplays.blit(TextSurf,TextRect)
        gamedisplays.blit(textSurf,textRect)
        stextSurf,stextRect=text_objects("ARROW LEFT : LEFT TURN",smalltext)
        stextRect.center=((150),(400))
        hTextSurf,hTextRect=text_objects("ARROW RIGHT : RIGHT TURN" ,smalltext)
        hTextRect.center=((150),(450))
        atextSurf,atextRect=text_objects("A : ACCELERATE",smalltext)
        atextRect.center=((150),(500))
        rtextSurf,rtextRect=text_objects("B : BRAKE ",smalltext)
        rtextRect.center=((150),(550))
        ptextSurf,ptextRect=text_objects("P : PAUSE  ",smalltext)
        ptextRect.center=((150),(350))
        sTextSurf,sTextRect=text_objects("CONTROLS",mediumtext)
        sTextRect.center=((350),(300))
        gamedisplays.blit(sTextSurf,sTextRect)
        gamedisplays.blit(stextSurf,stextRect)
        gamedisplays.blit(hTextSurf,hTextRect)
        gamedisplays.blit(atextSurf,atextRect)
        gamedisplays.blit(rtextSurf,rtextRect)
        gamedisplays.blit(ptextSurf,ptextRect)
        button("BACK",600,450,100,50,blue,bright_blue,"menu")
        pygame.display.update()
        clock.tick(30)


def obstacle(obs_startx, obs_starty, obs):
    if obs==0:
        obs_pic=pygame.image.load("car.jpg")
    elif obs==1:
        obs_pic=pygame.image.load("car1.jpg")
    elif obs==2:
        obs_pic=pygame.image.load("car2.jpg")
    elif obs==3:
        obs_pic=pygame.image.load("car4.jpg")
    elif obs==7:
        obs_pic=pygame.image.load("car5.jpg")
    elif obs==5:
        obs_pic=pygame.image.load("car6.jpg")
    elif obs==6:
        obs_pic=pygame.image.load("car7.jpg")
    elif obs ==4:
        obs_pic = pygame.image.load("car9.png")
    elif obs ==8:
        obs_pic = pygame.image.load("car10.png")
    elif obs ==9:
        obs_pic = pygame.image.load("car11.png")
    elif obs ==10:
        obs_pic = pygame.image.load("car12.png")
    elif obs ==11:
        obs_pic = pygame.image.load("car13.png")
    gamedisplays.blit(obs_pic,(obs_startx,obs_starty))


def score_system(passed,score):
    font=pygame.font.SysFont(None,25)
    text=font.render("Passed :- "+str(passed),True,black)
    score=font.render("Score :- "+str(score),True,red)
    gamedisplays.blit(text, (390, 50))
    gamedisplays.blit(score, (390, 30))


def text_objects(text,font):
    textsurface=font.render(text,True,black)
    return textsurface,textsurface.get_rect()


def message_display(text):
    largetext=pygame.font.SysFont("impact",80)
    textsurf,textrect=text_objects(text,largetext)
    textrect.center=((display_width/2),(display_height/2))
    gamedisplays.blit(textsurf,textrect)
    gamedisplays.blit(boom, (x-10, y-50))
    pygame.display.update()
    time.sleep(2)
    intro_loop()


def crash():
    message_display("YOU CRASHED")



def car(x,y):
    gamedisplays.blit(carimg,(x,y))

#defining function for running game in grass background
def game_loop():
    global pause
    
    global x
    global y
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change=0
    obstacle_speed=9
    obs=0

    obs_startx=random.randrange(200,(display_width-200))
    obs_starty=-750
    obs_width=56
    obs_height=125
    passed=0
    level=0
    score=0
    y2=7


    bumped=False
    while not bumped:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-5
                if event.key==pygame.K_RIGHT:
                    x_change=5
                if event.key==pygame.K_a:
                    obstacle_speed+=2
                if event.key == pygame.K_b:
                    if obstacle_speed > 1:
                        obstacle_speed -= 2
                    else:
                        obstacle_speed = 1
                if event.key == pygame.K_p:
                    pause = True
                    paused()
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0

        x+=x_change
        pause=True
        gamedisplays.fill(gray)

        #code for moving background
        rel_y=y2%backgroundpic.get_rect().width
        gamedisplays.blit(backgroundpic,(0,rel_y-backgroundpic.get_rect().width))
        gamedisplays.blit(backgroundpic,(700,rel_y-backgroundpic.get_rect().width))
        if rel_y<800:
            gamedisplays.blit(backgroundpic, (0, rel_y))
            gamedisplays.blit(backgroundpic, (700, rel_y))
            gamedisplays.blit(yellow_strip, (300, rel_y))
            gamedisplays.blit(yellow_strip, (500, rel_y))
            gamedisplays.blit(yellow_strip, (300, rel_y + 100))
            gamedisplays.blit(yellow_strip, (300, rel_y + 200))
            gamedisplays.blit(yellow_strip, (300, rel_y + 300))
            gamedisplays.blit(yellow_strip, (300, rel_y + 400))
            gamedisplays.blit(yellow_strip, (300, rel_y + 500))
            gamedisplays.blit(yellow_strip, (300, rel_y - 100))
            gamedisplays.blit(yellow_strip, (500, rel_y + 100))
            gamedisplays.blit(yellow_strip, (500, rel_y + 200))
            gamedisplays.blit(yellow_strip, (500, rel_y + 300))
            gamedisplays.blit(yellow_strip, (500, rel_y + 400))
            gamedisplays.blit(yellow_strip, (500, rel_y + 500))
            gamedisplays.blit(yellow_strip, (500, rel_y - 100))
            gamedisplays.blit(strip, (120, rel_y - 200))
            gamedisplays.blit(strip, (120, rel_y + 20))
            gamedisplays.blit(strip, (120, rel_y + 30))
            gamedisplays.blit(strip, (680, rel_y - 100))
            gamedisplays.blit(strip, (680, rel_y + 20))
            gamedisplays.blit(strip, (680, rel_y + 30))

        y2+=obstacle_speed




        obs_starty-=(obstacle_speed/4)
        obstacle(obs_startx,obs_starty,obs)
        obs_starty+=obstacle_speed
        car(x,y)
        score_system(passed,score)
        if x>690-car_width or x<110:
            crash()
        if x>display_width-(car_width+110) or x<110:
            crash()
        if obs_starty>display_height:
            obs_starty=0-obs_height
            obs_startx=random.randrange(170,(display_width-170))
            obs=random.randrange(0,12)
            passed=passed+1
            score=passed*10
            if int(passed)%10==0:
                level=level+1
                obstacle_speed+2
                largetext=pygame.font.SysFont("impact",80)
                textsurf,textrect=text_objects("LEVEL"+str(level),largetext)
                textrect.center=((display_width/2),(display_height/2))
                gamedisplays.blit(textsurf,textrect)
                pygame.display.update()
                time.sleep(1)


        if y<obs_starty+obs_height:
            if x > obs_startx and x < obs_startx + obs_width or x+car_width > obs_startx and x+car_width < obs_startx+obs_width:

                crash()


        pygame.display.update()
        clock.tick(60)

#defining function for running game in snow background
def game_loop1():
    global pause
    global x
    global y
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change=0
    obstacle_speed=9
    obs=0
    y_change=0
    obs_startx=random.randrange(200,(display_width-200))
    obs_starty=-750
    obs_width=56
    obs_height=125
    passed=0
    level=0
    score=0
    y2=7
    fps=120

    bumped=False
    while not bumped:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-5
                if event.key==pygame.K_RIGHT:
                    x_change=5
                if event.key==pygame.K_a:
                    obstacle_speed+=2
                if event.key == pygame.K_b:
                    if obstacle_speed > 1:
                        obstacle_speed-=2
                    else:
                        obstacle_speed = 1
                if event.key == pygame.K_p:
                    pause = True
                    paused()
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0

        x+=x_change
        pause=True
        gamedisplays.fill(gray)

        # code for moving background
        rel_y=y2%backgroundpic1.get_rect().width
        gamedisplays.blit(backgroundpic1,(0,rel_y-backgroundpic1.get_rect().width))
        gamedisplays.blit(backgroundpic1,(700,rel_y-backgroundpic1.get_rect().width))
        if rel_y<800:
            gamedisplays.blit(backgroundpic1,(0,rel_y))
            gamedisplays.blit(backgroundpic1,(700,rel_y))
            gamedisplays.blit(yellow_strip, (300, rel_y))
            gamedisplays.blit(yellow_strip, (500, rel_y))
            gamedisplays.blit(yellow_strip, (300, rel_y + 100))
            gamedisplays.blit(yellow_strip, (300, rel_y + 200))
            gamedisplays.blit(yellow_strip, (300, rel_y + 300))
            gamedisplays.blit(yellow_strip, (300, rel_y + 400))
            gamedisplays.blit(yellow_strip, (300, rel_y + 500))
            gamedisplays.blit(yellow_strip, (300, rel_y - 100))
            gamedisplays.blit(yellow_strip, (500, rel_y + 100))
            gamedisplays.blit(yellow_strip, (500, rel_y + 200))
            gamedisplays.blit(yellow_strip, (500, rel_y + 300))
            gamedisplays.blit(yellow_strip, (500, rel_y + 400))
            gamedisplays.blit(yellow_strip, (500, rel_y + 500))
            gamedisplays.blit(yellow_strip, (500, rel_y - 100))
            gamedisplays.blit(strip,(120,rel_y-200))
            gamedisplays.blit(strip,(120,rel_y+20))
            gamedisplays.blit(strip,(120,rel_y+30))
            gamedisplays.blit(strip,(680,rel_y-100))
            gamedisplays.blit(strip,(680,rel_y+20))
            gamedisplays.blit(strip,(680,rel_y+30))

        y2+=obstacle_speed




        obs_starty-=(obstacle_speed/4)
        obstacle(obs_startx,obs_starty,obs)
        obs_starty+=obstacle_speed
        car(x,y)
        score_system(passed,score)
        if x>690-car_width or x<110:
            crash()
        if x>display_width-(car_width+110) or x<110:
            crash()
        if obs_starty>display_height:
            obs_starty=0-obs_height
            obs_startx=random.randrange(170,(display_width-170))
            obs=random.randrange(0,12)
            passed=passed+1
            score=passed*10
            if int(passed)%10==0:
                level=level+1
                obstacle_speed+2
                largetext=pygame.font.SysFont("impact",80)
                textsurf,textrect=text_objects("LEVEL"+str(level),largetext)
                textrect.center=((display_width/2),(display_height/2))
                gamedisplays.blit(textsurf,textrect)
                pygame.display.update()
                time.sleep(1)



        if y<obs_starty+obs_height:
            if x > obs_startx and x < obs_startx + obs_width or x+car_width > obs_startx and x+car_width < obs_startx+obs_width:
                crash()

        pygame.display.update()
        clock.tick(60)


intro_loop()
theme()

pygame.quit()
quit()
