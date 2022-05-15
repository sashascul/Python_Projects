import math
from random import choice
from random import randint as rnd

import pygame
pygame.font.init()
pygame.init()
FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600

class Ball:
    def __init__(self, screen: pygame.Surface, x = 40, y = 450):
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 10

    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 4
        x = self.x
        y = self.y
        r = self.r
        if x + r >=800:
            self.vx *= -1
            self.x = self.x+2 * self.vx
        if x - r <=0:
            self.vx *= -1
            self.x += 2 * self.vx
        if y + r >= 600:
            self.vy *= -0.8
            self.live -= 1
        

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)

    def hittest(self, obj):
        da = self.x - obj.x
        db = self.y - obj.y
        ddc = da*da + db*db
        ddc = ddc**(1/2)
        dc = self.r + obj.r
        if ddc <= dc:
            return True
        return False
class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        global balls
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1] - new_ball.y), (event.pos[0] - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        if event:
            self.an = math.atan((event.pos[1] - 450) / (event.pos[0] - 20))
        if self.f2_on:
            self.color = BLUE
        else:
            self.color = GREY

    def draw(self):
        cos = math.cos(self.an)
        sin = math.sin(self.an)
        x0, y0 = 20, 450
        d = self.f2_power
        g = 8
        x1, y1 = 20+d * cos, 450 + d * sin
        x2, y2 = 20 + sin * g, 450 - g * cos
        x3, y3 = x1 + sin * g, y1 - g * cos
        gg = [(x0,y0),(x1,y1),(x3,y3),(x2,y2)]
        
        pygame.draw.polygon(screen, self.color, gg)
       


    def power_up(self):
        if self.f2_on:
            if self.f2_power < 50:
                self.f2_power += 0.3
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self):
        self.live = 1
        self.new_target()

    def new_target(self):
        x = self.x = rnd(600, 750)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(10, 50)
        self.vx = rnd(-3, 3)
        self.vy = rnd(-3, 3)
        color = self.color = RED


    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
        pygame.draw.circle(screen, BLACK, (self.x, self.y), self.r, 2)
        
    def move(self):
        x, y, vx, vy = self.x, self.y, self.vx, self.vy
        r = self.r
        x += vx
        y += vy
        if x + r + vx > 801:
            vx *= -1
        if x - r + vx < 499:
            vx *= -1
        if y + r + vy > 601:
            vy *= -1
        if y - r + vy < 249:
            vy*=-1
        self.x, self.y, self.vx, self.vy = x, y, vx, vy
            


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
target = Target()
target2 = Target()
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    target.draw()
    target2.draw()
    for b in balls:
        if b.live >= 1:
            b.draw()
    f2 = pygame.font.Font(None, 50)
    text2 = f2.render("Your score: " + str(bullet), True, (40, 50, 150), (0, 0, 0))
    screen.blit(text2, (0, 0))               
    pygame.display.update()
    
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:
        b.move()
        if b.hittest(target) and target.live:
            target.live = 1
            target.new_target()
            bullet += 1
        if b.hittest(target2) and target2.live:
            target2.live = 1
            target2.new_target()
            bullet += 1     
    target.move()
    target2.move()
    gun.power_up()
    

pygame.quit()