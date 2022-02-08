import pygame
import pygame_menu
import random
import time
import os
from math import pi

pygame.init()
pygame.font.init()
pygame.mixer.init()

#Define game window
display_w = 800
display_h = 600
gameDisplay = pygame.display.set_mode((display_w,display_h))
pygame.display.set_caption("Makhmal Palace")
gameIcon = pygame.image.load('Images/makhs.png')
pygame.display.set_icon(gameIcon)
clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

#Define colors
black = (0,0,0)
white = (255,255,255)
bg = (50,50,50)
btncolor = (0, 255, 245)

#Define sounds
pause_sound = pygame.mixer.Sound('Audio/pause.wav')


block_color = (53,115,255)
makhs_h = 56
makhs_w = 56
makhs = pygame.image.load('Images/makhs.png')
makhs_vel = 10
makhspos_x = 0
makhspos_y = 0
treat = pygame.image.load('Images/treat.png')
nip = pygame.image.load('Images/nip.png')

#Set classes
class Collectibles(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((40,40))
        # self.surf.fill((128,255,40))
        self.speed = 10
        self.pos_x = display_w / 2
        self.pos_y = 0
        self.rect = self.surf.get_rect()

treats = Collectibles()
nips = Collectibles()



#Menu test
def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def start_the_game():
    # Do the job here !
    pass

# menu = pygame_menu.Menu('Welcome', 400, 300,
#                        theme=pygame_menu.themes.THEME_BLUE)

# menu.add.text_input('Name :', default='John Doe')
# menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
# menu.add.button('Play', start_the_game)
# menu.add.button('Quit', pygame_menu.events.EXIT)

#Define game actions
lastbuttonclick = time.time()
print(lastbuttonclick)
def button(msg,x,y,w,h,ic,ac,action=None):
    global lastbuttonclick
    if (time.time() < lastbuttonclick+1):
        return
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h),border_radius=(15))
        if click[0] == 1 and action != None:
            action()
            lastbuttonclick = time.time()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h),border_radius=(15))
    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)),(y+(h/2)))
    gameDisplay.blit(textSurf, textRect)

        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         pygame.quit()
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_p:
        #             unpause()

def makhs_movement(keys_pressed):
    global makhspos_x
    global makhspos_y
    if keys_pressed[pygame.K_LEFT] and makhspos_x - makhs_vel > 0: # LEFT
        makhspos_x -= makhs_vel
    if keys_pressed[pygame.K_RIGHT] and makhspos_x + makhs_vel + makhs_w < display_w: # RIGHT
        makhspos_x += makhs_vel
    if keys_pressed[pygame.K_UP] and makhspos_y - makhs_vel > 0: # UP
        makhspos_y -= makhs_vel
    if keys_pressed[pygame.K_DOWN] and makhspos_y + makhs_vel + makhs_h < display_h: # DOWN
        makhspos_y += makhs_vel

def unpause():
    global pause
    # pygame.mixer.Sound.play(pause_sound)
    pygame.mixer.music.unpause()
    pause = False

def paused():
    print('paused')
    global pause
    pause = True
    pygame.mixer.Sound.play(pause_sound)
    pygame.mixer.music.pause()
    largeText = pygame.font.SysFont("freesansbold.ttf",115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_w/2),(display_h/2))
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    unpause()

        button("Continue",50,450,120,50,btncolor,white,unpause)
        button("Help",250,450,120,50,btncolor,white,help_menu)
        button("New Game",450,450,120,50,btncolor,white,game_loop)
        button("Main Menu",650,450,120,50,btncolor,white,game_menu)

        pygame.display.update()
        #test the time.wait function!
        # pygame.time.wait()
        # clock.tick(15)  

def help_menu():
    print('help menu')
    gameDisplay.fill(bg)
    largeText = pygame.font.SysFont("freesansbold.ttf",115)
    TextSurf, TextRect = text_objects("Help Menu", largeText)
    TextRect.center = ((display_w/2),(display_h/2))
    gameDisplay.blit(TextSurf, TextRect)

    # while pause:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             quit()
    #         if event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_p:
    #                 unpause()

    button("Continue",150,450,120,50,btncolor,white,unpause)
    button("New Game",350,450,120,50,btncolor,white,game_loop)
    button("Main Menu",550,450,120,50,btncolor,white,game_menu)

    pygame.display.update()

def first_help_menu():
    print('first help menu')
    gameDisplay.fill(bg)
    largeText = pygame.font.SysFont("freesansbold.ttf",115)
    TextSurf, TextRect = text_objects("Help Menu", largeText)
    TextRect.center = ((display_w/2),(display_h/2))
    gameDisplay.blit(TextSurf, TextRect)

    # while pause:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             quit()
    #         if event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_p:
    #                 unpause()

    # button("Continue",150,450,120,50,btncolor,white,unpause)
    button("New Game",350,450,120,50,btncolor,white,game_loop)
    button("Main Menu",550,450,120,50,btncolor,white,game_menu)

    pygame.display.update()

def quitgame():
    pygame.quit()
    quit()

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: "+str(count), True, black)
    gameDisplay.blit(text,(10,10))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
   # pygame.draw.polygon(gameDisplay, color, ())

# def treats(treatx, treaty, treatw, treath):
#     pass

def makhmal(x,y):
    gameDisplay.blit(makhs, (x,y))

def crash():
    print('crashed!')
    # pygame.mixer.Sound.play(crash_sound)
    # pygame.mixer.music.stop()
    largeText = pygame.font.SysFont('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects("You ded.", largeText)
    TextRect.center = ((display_h/2),(display_h/2))
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #gameDisplay.fill(white)

        button("Play again",150,450,120,50,btncolor,white,game_loop)
        button("Help",350,450,120,50,btncolor,white,first_help_menu)
        button("Main menu",550,450,120,50,btncolor,white,game_menu)

        pygame.display.update()
        clock.tick(15)

# Define game components
def game_menu():
    print('game menu')
    intro = True
    pygame.mixer.music.load('Audio/menu.wav')
    pygame.mixer.music.play(-1)

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(bg)
        largeText = pygame.font.Font('freesansbold.ttf',90)
        TextSurf, TextRect = text_objects("Makhmal Palace", largeText)
        TextRect.center = ((display_w/2),(display_h/2))
        gameDisplay.blit(TextSurf, TextRect)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        button("Start",150,450,120,50,btncolor,white,game_loop)
        button("Help",350,450,120,50,btncolor,white,first_help_menu)
        button("Quit",550,450,120,50,btncolor,white,quitgame)

        # if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
        #     pygame.draw.rect(gameDisplay, bright_green, (150,450,100,50))
        # else:
        #     pygame.draw.rect(gameDisplay, green, (150,450,100,50))
        
        # smallText = pygame.font.Font("freesansbold.ttf",20)
        # textSurf, textRect = text_objects("Start", smallText)
        # textRect.center = ( (150+(100/2)), (450+(50/2)) )
        # gameDisplay.blit(textSurf, textRect)

        # pygame.draw.rect(gameDisplay, red, (550,450,100,50))

        pygame.display.update()
        clock.tick(15)

def game_loop():
    print('PLAY GAEM')
    global pause
    pygame.mixer.music.load('Audio/gamemusic.wav')
    pygame.mixer.music.play(-1)

    global makhspos_x
    global makhspos_y
    makhspos_x = (display_w * 0.45)
    makhspos_y = (display_h * 0.8)

    goods = pygame.sprite.Group()
    goods.add(treats)
    goods.add(nips)


    thing_speed = 4
    thing_width = 100
    thing_height = 100
    thingpos_x = random.randrange(0, display_w)
    thingpos_y = 0 - thing_height

    thingCount = 1
    dodged = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = True
                    paused()
        keys_pressed = pygame.key.get_pressed()
        makhs_movement(keys_pressed)
        gameDisplay.fill(bg)
        things(thingpos_x, thingpos_y, thing_width, thing_height, block_color)
        thingpos_y += thing_speed
        makhmal(makhspos_x,makhspos_y)
        things_dodged(dodged)
        for entity in goods:
            gameDisplay.blit(entity.surf, entity.rect)

        if thingpos_y > display_h:
            thingpos_y = 0 - thing_height
            thingpos_x = random.randrange(0,display_h)
            dodged += 1
            thing_speed += 1
            # thing_width += (dodged * 1.02)

        # if (makhspos_y < thingpos_y and makhspos_y > thingpos_y+thing_height) or (makhspos_y > thingpos_y):
        if (makhspos_y > thingpos_y-thing_height and makhspos_y < thingpos_y):
            # print('y crossover')

            if (makhspos_x > thingpos_x and makhspos_x < thingpos_x + thing_width) or (makhspos_x+makhs_w > thingpos_x and makhspos_x + makhs_w < thingpos_x+thing_width):
                # print('x crossover')
                crash()


        pygame.display.update()
        clock.tick(60)

game_menu()
# help_menu()
# game_loop()
# game_menu()
# game_loop()
pygame.quit()
quit()