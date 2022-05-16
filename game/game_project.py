########## IN THIS GAME YOU NEED TO SHOOD DOWN POKEBALLS. USE KEYS 'KEYLEFT' AND 'KEYRIGHT'
########## USE THE KEY 'SPACE' TO JUMP AND THE KEY 'F' TO SHOOTING. THE NUMBER OF SCORED IS
########## RECORDING IN THE LOWER LEFT CORNER. THIS GAME DEVELOPED BY SASHASCUL...

########## CODE:

import pygame
import time
import random
from random import randrange

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
baloon = pygame.image.load('baloon.png')

###################


###FIELD & BACKGROUND###
win = pygame.display.set_mode((600, 300))
bg = pygame.image.load('bg.jpg')
########################

font_score = pygame.font.SysFont('Arial', 26, bold = True)

#CHARACTER COORDINATS, SPEED & ACTION#
x = 100
y = 205
speed = 1
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
    global fps

    if fps + 1 >= 25:
        fps = 0
    
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
    
    if keys[pygame.K_RIGHT] and x < 1250:
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

    if appleBool == 1:
        appleX = randrange(30, 570, 20)
        appleY = randrange(50, 100, 20)
        appleR = 25
        appleBool = 0
        apple = appleX, appleY

    pygame.draw.rect(win, pygame.Color('red'),(*apple, 20, 20))
    render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))
    win.blit(render_score, (5, 270))
    win.blit(baloon, (appleX - 15, appleY-20))
    pygame.display.update()

f = open('youscore.txt', 'a')
f.write('Player: ' + name + ' scored ' + str(score) + ' points \n')
f.close()

pygame.quit()
