import random

import pygame, sys, os
from pygame.locals import *
c=0
WIDTH = 500
HEIGHT = 500
BLUE = (104,181,212)
WHITE=(255,255,255)
GRAY=(193,205,205)
LINE_WIDTH = 1
LINE_COLOR = (0, 0, 0)
CROSS_COLOR = (255, 0, 0)
SQUARE_SIZE = 71.5
colums= 6
row=6
pygame.init()

water = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption =('Tom and Gery')
randlistG= [73, 143, 214.5, 286, 357.5, 429]
randlistS= [143, 214.5, 286, 357.5]
x_gery = random.choice(randlistS)
y_gery = random.choice(randlistS)
x_tom = random.choice(randlistS)
y_tom = random.choice(randlistS)
def draw_lines():
    hori_lines = []
    for x in range(0, 6):
        ver_lines = []
        for y in range(0, 6):
            pygame.draw.line(water, LINE_COLOR, ((y + 1) * SQUARE_SIZE, 0), ((y + 1) * SQUARE_SIZE, HEIGHT), LINE_WIDTH)
            ver_lines.append(0)
        pygame.draw.line(water, LINE_COLOR, (0, ((x + 1) * SQUARE_SIZE)), (WIDTH, ((x + 1) * SQUARE_SIZE)), LINE_WIDTH)
        hori_lines.append(ver_lines)
def import_elements(x_gery, y_gery, x_tom, y_tom,c):
    gery = pygame.image.load('gery.png')
    tom = pygame.image.load('tom.png')
    bridge = pygame.image.load('bridge.png')
    ggery = pygame.transform.scale(gery, (50, 50))
    water.blit(ggery,(x_gery,y_gery))
    ttom = pygame.transform.scale(tom, (50, 50))
    water.blit(ttom, (x_tom, y_tom))
    bbridge = pygame.transform.scale(bridge, (70, 70))
    water.blit(bbridge, (429, 214.5))
    if x_tom == x_gery and y_tom == y_gery:
        eaten = pygame.image.load('eat.png')
        eeaten = pygame.transform.scale(eaten, (500, 500))
        water.blit(eeaten, (0, 0))
    if x_gery == 73 or x_gery == 429 or y_gery == 73 or y_gery == 429 or x_gery == 0  or y_gery == 0 :
        if (x_gery == 429 and y_gery == 214.5):
            win = pygame.image.load('win.png')
            wwin = pygame.transform.scale(win, (450, 450))
            water.blit(wwin, (0, 0))
        else :
            drown = pygame.image.load('drown.jpg')
            ddrown = pygame.transform.scale(drown, (500, 500))
            water.blit(ddrown, (0, 0))
    if c >= 20:
        starve = pygame.image.load('starve.png')
        sstarve = pygame.transform.scale(starve, (500, 500))
        water.blit(sstarve, (0, 0))

pygame.display.update()

exit = False
while not exit:
    for event in pygame.event.get():
        water.fill(BLUE)
        pygame.draw.rect(water, WHITE, [73, 73, 357, 357])
        pygame.draw.rect(water, GRAY, [x_gery, y_gery, 71.5, 71.5])
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE]:
            move_list = ['left', 'right', 'up', 'down']
            check_movelist = random.choice(move_list)
            c += 1
            if check_movelist == 'left':
                x_gery -= 71.5
            if check_movelist == 'right':
                x_gery += 71.5
            if check_movelist == 'up':
                y_gery -= 71.5
            if check_movelist == 'down':
                y_gery += 71.5

        if keys_pressed[pygame.K_LEFT]:
            x_gery -= 71.5
            c += 1
        if keys_pressed[pygame.K_RIGHT]:
            x_gery += 71.5
            c += 1
        if keys_pressed[pygame.K_UP]:
            y_gery -= 71.5
            c += 1
        if keys_pressed[pygame.K_DOWN]:
            y_gery += 71.5
            c += 1
        if event.type == pygame.QUIT:
            exit=True
    draw_lines()
    import_elements(x_gery, y_gery, x_tom, y_tom,c)
    pygame.display.update()

    