import random

import pygame, sys, os
from pygame.locals import *

WIDTH = 500
HEIGHT = 500
BLUE = (0,0,139)
WHITE=(255,255,255)
LINE_WIDTH = 1
LINE_COLOR = (0, 0, 0)
CROSS_COLOR = (255, 0, 0)
SQUARE_SIZE = 71.5
colums= 6
row=6
pygame.init()
#border = pygame.display.set_mode((500,500))
water = pygame.display.set_mode((WIDTH,HEIGHT))
#land= pygame.display.set_mode((200,200))
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
def import_elements(x_gery, y_gery, x_tom, y_tom):
    gery = pygame.image.load('gery.png')
    tom = pygame.image.load('tom.png')
    bridge = pygame.image.load('bridge.png')
    ggery = pygame.transform.scale(gery, (50, 50))
    water.blit(ggery,(x_gery,y_gery))
    ttom = pygame.transform.scale(tom, (50, 50))
    water.blit(ttom, (x_tom, y_tom))
    bbridge = pygame.transform.scale(bridge, (70, 70))
    water.blit(bbridge, (429, 214.5))

pygame.display.update()

exit = False
while not exit:
    for event in pygame.event.get():
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE]:
            move_list = ['left', 'right', 'up', 'down']
            check_movelist = random.choice(move_list)
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
        if keys_pressed[pygame.K_RIGHT]:
            x_gery += 71.5
        if keys_pressed[pygame.K_UP]:
            y_gery -= 71.5
        if keys_pressed[pygame.K_DOWN]:
            y_gery += 71.5
        if event.type == pygame.QUIT:
            exit=True
    #border.fill(WHITE)
    water.fill(BLUE)
    #land.fill(WHITE)
    pygame.draw.rect(water, WHITE, [73,73, 357, 357])
    draw_lines()
    import_elements(x_gery, y_gery, x_tom, y_tom)

    pygame.display.update()
    