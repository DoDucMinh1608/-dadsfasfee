# Be sure to install pygame via pip

import pygame
import math
import sys
import random

# initialize it
pygame.init()
# configurations
frames_per_second = 60
window_height = 600
window_width = 600

# snake's body
bodies = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]
line_size = 2
movingInterval = 50
movingTime = 0
inputTime = False
body = (20, 20)
tiles = (math.floor(window_height/body[0]), math.floor(window_height/body[0]))


# colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# creating window
display = pygame.display.set_mode((window_width, window_height))

# creating our frame regulator
clock = pygame.time.Clock()


def drawSquare():
    for i in range(tiles[0]):
        pos = i*body[0]
        pygame.draw.line(display, GRAY, (pos, 0),
                         (pos, window_height), line_size)
    for i in range(tiles[1]):
        pos = i*body[0]
        pygame.draw.line(display, GRAY, (0, pos),
                         (window_width, pos), line_size)


def ee(pos, size):
    return list(map(lambda i: i*size, pos))


def updateSnake():
    for i in bodies:
        pygame.draw.rect(display, BLUE, pygame.Rect(ee(i, body[0]), body), 3)


direct = 'down'


def randomPos():
    return [random.randint(0, tiles[0]-1), random.randint(0, tiles[1]-1)]


def checkPos(pos1, pos2):
    return pos1[0] == pos2[0] and pos1[1] == pos2[1]


font = pygame.font.SysFont("Segoe UI", 20)


def renderScore(score):
    display.blit(font.render(str(score), True, WHITE), (10, 10))


foodPos = randomPos()
clear = True
death = False
score = 0
# forever loop
while True:

    dtime = clock.get_time()
    movingTime += dtime

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and direct != 'right':
        direct = 'left'
    elif keys[pygame.K_d] and direct != 'left':
        direct = 'right'
    elif keys[pygame.K_s] and direct != 'up':
        direct = 'down'
    elif keys[pygame.K_w] and direct != 'down':
        direct = 'up'

    if (movingTime >= movingInterval):
        movingTime = 0
        [x, y] = list(bodies[0])
        if direct == 'left':
            x += -1 if x > 0 else tiles[0]-1
        elif direct == 'right':
            x += 1 if x < tiles[0]-1 else -x
        elif direct == 'up':
            y += -1 if y > 0 else tiles[1]-1
        else:
            y += 1 if y < tiles[1]-1 else -y
        bodies.insert(0, [x, y])
        if clear:
            bodies.pop()
        else:
            clear = True
    # frame clock ticking
    display.fill(BLACK)
    clock.tick(frames_per_second)
    drawSquare()
    # frame Drawing
    pygame.draw.rect(display, WHITE, pygame.Rect(
        ee(foodPos, body[0]), body), 4)

    updateSnake()
    renderScore(score)
    for i in range(1, len(bodies)):
        if (checkPos(bodies[i], bodies[0])):
            death = True
    if (checkPos(bodies[0], foodPos)):
        score += 1
        while True:
            newPos = randomPos()
            a = False
            for i in bodies:
                if checkPos(i, newPos):
                    a = True
            if not a:
                foodPos = newPos
                clear = False
                break
    # event loop
    if death:
        break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
