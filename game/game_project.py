########## IN THIS GAME YOU NEED TO SHOOD DOWN POKEBALLS. USE KEYS 'KEYLEFT' AND 'KEYRIGHT'
########## USE THE KEY 'SPACE' TO JUMP AND THE KEY 'F' TO SHOOTING. THE NUMBER OF SCORED IS
########## RECORDING IN THE LOWER LEFT CORNER. THIS GAME DEVELOPED BY SASHASCUL...

########## CODE:

import pygame
import sys
import time
import random
from random import randrange
from tkinter import *
from array import *
import array

###SEE 'END' ###
print("Print your name: ")
name = str(input())


pygame.init()

pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)

#####ANIMATION#####
walkRight = [pygame.image.load('right1.png'), pygame.image.load('right2.png'),
             pygame.image.load('right3.png'), pygame.image.load('right4.png'),
             pygame.image.load('right5.png')]
walkLeft = [pygame.image.load('l1.png'), pygame.image.load('l2.png'),
             pygame.image.load('l3.png'), pygame.image.load('l4.png'),
             pygame.image.load('l5.png')]
walkStatic = pygame.image.load('back.png')

coin = [pygame.image.load('Coin1.png'), pygame.image.load('Coin2.png'),
        pygame.image.load('Coin3.png'), pygame.image.load('Coin4.png'),
        pygame.image.load('Coin5.png'), pygame.image.load('Coin6.png')]

###################


###FIELD & BACKGROUND###
win = pygame.display.set_mode((600, 300))
screen = pygame.Surface((600, 300))
bg = pygame.image.load('bg.jpg')
########################

font_score = pygame.font.SysFont('Arial', 26, bold = True, italic = True)

#CHARACTER COORDINATS, SPEED & ACTION#
x = 100
y = 205
speed = 1
speedMoney = 1
a = 1       #FOR INFINITY CYCLE
jump = False
left = False
right = False
timejump = 7.5
clock = pygame.time.Clock()
######################################

#####MUSIC EFFECTS#####
space = pygame.mixer.Sound("space.ogg")
throw = pygame.mixer.Sound("throw.ogg")
money = pygame.mixer.Sound("money.ogg")

########OTHER#########
x1 = 5
fps = 30
fps1 = 35
bullets = []
lastMove = "right"
foo_result = False
score = 0
######################

###POINT###
appleBool = 1
###########


###CLASSES & FUNCTIONS###

class gun():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.velx = 3 * facing
        self.vely = 5 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

class Menu:

    def __init__(self, points = [100, 100, 'play', (250, 250, 30), (250, 30, 250)]):
        self.points = points

    def render(self, poverchnost, font, num_punkt):
        for i in self.points:
            if num_punkt == i[5]:
                poverchnost.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                poverchnost.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def menu(self):
        done = True
        font_menu = pygame.font.SysFont('Arial', 26, bold = True)
        point = 0
        while done:
            screen.fill((0, 100, 200))

            mp = pygame.mouse.get_pos()
            for i in self.points:
                if mp[0] > i[0] and mp[0] < i[0] + 155 and mp[1] > i[1] and mp[1] < i[1] + 50:
                    point = i[5]
            self.render(screen, font_menu, point)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()
                    if e.key == pygame.K_UP:
                        if point > 0:
                            point -= 1
                    if e.key == pygame.K_DOWN:
                        if point < len(self.points) - 1:
                            point += 1
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if point == 0:
                        done = False
                    elif point == 1:
                        sys.exit()


            win.blit(screen, (0, 0))
            pygame.display.flip()

#DESTROY OBJECT APPLE#

def destroyObj(appleX, appleY, appleR, self):
    da = self.x - appleX
    db = self.y - appleY
    ddc = da * da + db * db
    ddc = (ddc ** (1/2))
    dc = self.radius + appleR
    if ddc <= dc:
        return True
    return False

#THIS FUNCTION USED FOR CREATE THE CHARACTER & CYCLE THE BULLET#

def player():
    win.fill((0,0,0))
    win.blit(bg, (0,0))
    global fps, fps1

    if fps + 1 >= 25:
        fps = 0

    if fps1 + 1 >= 25:
        fps1 = 0

    fps1 += 1

    if right:
        win.blit(walkRight[fps // 5], (x, y))
        fps += 1
    elif left:
        win.blit(walkLeft[fps // 5], (x, y))
        fps += 1
    else:
        win.blit(walkStatic, (x, y))

    for bullet in bullets:
        bullet.draw(win)

################################################################

#INFINITY CYCLE#

L = []
with open("youscore.txt", "r") as f:
    for line in f:
        L.append(line)

L.sort(reverse=True)

sor = ['', '', '', '', '', '', '', '', '', '', ''
        '', '', '', '', '', '', '', '', '', '']

for i in range(len(L)):
    sor[i] = L[i]




points = [(120, 100, 'PLAY', (250, 250, 30), (250, 30, 250), 0),
          (350, 0, sor[0], (0, 250, 0), (0, 250, 0), 1),
          (350, 30, sor[1], (0, 250, 0), (0, 250, 0), 1),
          (350, 60, sor[2], (0, 250, 0), (0, 250, 0), 1),
          (350, 90, sor[3], (0, 250, 0), (0, 250, 0), 1),
          (350, 120, sor[4], (0, 250, 0), (0, 250, 0), 1)]

game = Menu(points)
game.menu()

while a == 1:

    pygame.time.delay(8)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            a = 0

    for bullet in bullets:
        if bullet.x < 600 and bullet.x > 0:
            if facing < 0:
                bullet.x += bullet.velx
                bullet.y += bullet.vely
                bullet.vely += 0.1

                if destroyObj(appleX, appleY, appleR, bullet) == True:
                    money.play()
                    appleBool = 1
                    score += 1

            else:
                bullet.x += bullet.velx
                bullet.y -= bullet.vely
                bullet.vely -= 0.1

                if destroyObj(appleX, appleY, appleR, bullet) == True:
                    money.play()
                    appleBool = 1
                    score += 1

        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_f]:
        throw.play()

        if lastMove == "right":
            facing = 1
        else:
            facing = -1

        if len(bullets) < 1:
            bullets.append(gun(round(x + 20 // 2), round(y + 34 // 2), 5, (255, 0, 0), facing))

    if keys[pygame.K_RIGHT] and x < 580:
        x += speed
        right = True
        left = False
        lastMove = "right"
    elif keys[pygame.K_LEFT] and x > 10:
        x -= speed
        right = False
        left = True
        lastMove = "left"
    else:
        right = False
        left = False
        animСount = 0
    if jump == False:
        if keys[pygame.K_SPACE]:
            space.play()
            jump = True
    else:
        if timejump >= -7.5:
            if timejump < 0:
                y += (timejump ** 2) / 2
            else:
                y -= (timejump ** 2) / 2
            timejump -= 1
        else:
            jump = False
            timejump = 7.5

    x1 += speed

    player()

    if appleBool == 0:

        appleX += vMoneyX
        appleY += vMoneyY

        if appleX > 590 or appleX < 10 or appleY > 100 or appleY < 0:
            appleX = randrange(30, 570, 20)
            appleY = randrange(50, 100, 20)
            vMoneyX = random.uniform(-1, 1)
            vMoneyY = random.uniform(-1, 1)
            appleR = 25
            appleBool = 0
            apple = appleX, appleY


    if appleBool == 1:
        appleX = randrange(30, 570, 20)
        appleY = randrange(50, 100, 20)
        vMoneyX = random.random()
        vMoneyY = random.random()
        appleR = 25
        appleBool = 0
        apple = appleX, appleY


    win.blit(coin[fps1 // 5], (appleX - 5, appleY - 5))

    render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))
    win.blit(render_score, (5, 270))
    pygame.display.update()

# f = open('youscore.txt', 'a')
# f.write('Player: ' + name + ' scored ' + str(score) + ' points \n')
# f.close()

f = open('youscore.txt', 'a')
f.write(str(score) + "points by " + str(name) + '\n')
f.close()

pygame.quit()

