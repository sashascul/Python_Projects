import pygame
from pygame import *
pygame.init()

### SCREEN ###

win_w = 800
win_h = 600
win_color = 'green'
win = pygame.display.set_mode((win_w, win_h))
screen = pygame.Surface((win_w, win_h))
screen.fill(win_color)

############################
### CONSTANTS AND OTHERS ###

show = True
objectWidth = 32
objectHeight = 32
objectColor = 'red'

########################

###PLAYER PARAMETERS ###

speed = 7
jumpSpeed = 10
g = 0.65
player_width = 22
player_height = 32
player_color = 'grey'

########################

class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((objectWidth, objectHeight))
        self.image.fill(Color(objectColor))
        self.rect = Rect(x, y, objectWidth, objectHeight)

class Player(sprite.Sprite):

    def __init__(self, x, y):

        sprite.Sprite.__init__(self)

        self.vx = 0
        self.vy = 0
        self.stay = False
        self.xo = x
        self.yo = y
        self.image = Surface((player_width, player_height))
        self.image.fill(Color(player_color))
        self.rect = Rect(x, y, player_width, player_height)

    def update(self, left, right, up, objects):

        if right:

            self.vx = speed

        if left:

            self.vx = -speed

        if not(right or left):

            self.vx = 0

        if up:

            if self.stay:

                self.vy = -jumpSpeed

        if not self.stay:

            self.vy += g

        self.stay = False
        self.rect.y += self.vy
        self.rect.x += self.vx
        self.collide(0, self.vy, objects)
        self.collide(self.vx, 0, objects)

    def collide(self, vx, vy, objects):
        for z in objects:

            if sprite.collide_rect(self, z):

                if vx > 0:

                    self.rect.right = z.rect.left

                if vx < 0:

                    self.rect.left = z.rect.right

                if vy > 0:

                    self.rect.bottom = z.rect.top
                    self.stay = True
                    self.vy = 0

                if vy < 0:

                    self.rect.top = z.rect.bottom
                    self.vy = 0

player = Player(155, 55)
left = False
right = False
up = False

all_objects = pygame.sprite.Group()
objects = []
all_objects.add(player)

level = [
       "-------------------------",
       "-                       -",
       "-                       -",
       "-                       -",
       "-            --         -",
       "-                       -",
       "--                      -",
       "-                       -",
       "-                   --- -",
       "-                       -",
       "-                       -",
       "-      ---              -",
       "-                       -",
       "-   -----------         -",
       "-                       -",
       "-                -      -",
       "-                   --  -",
       "-                       -",
       "-                       -",
       "-------------------------"]

while show == True:

    pygame.time.Clock().tick(60)

    for i in pygame.event.get():
        if i.type == QUIT:
            show = False

    win.blit(screen, (0, 0))

    x = 0
    y = 0

    for j in level:
        for k in j:
            if k == "-":

                block = Platform(x, y)
                all_objects.add(block)
                objects.append(block)

            x += objectWidth
        y += objectHeight
        x = 0

    if i.type == KEYDOWN and i.key == K_LEFT:
        left = True

    if i.type == KEYDOWN and i.key == K_RIGHT:
        right = True

    if i.type == KEYUP and i.key == K_RIGHT:
        right = False

    if i.type == KEYUP and i.key == K_LEFT:
        left = False

    if i.type == KEYDOWN and i.key == K_UP:
        up = True

    if i.type == KEYUP and i.key == K_UP:
        up = False


    player.update(left, right, up, objects)
    all_objects.draw(win)

    pygame.display.update()

pygame.quit()
