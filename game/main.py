#modules and imports
import sys
import os
import random
from math import atan2, degrees, cos, sin, radians
import pygame

# initializer
pygame.init()
pygame.mixer.init()

# window size
g_width = 1100
g_height = 800

# framerate
fps = 60
clock = pygame.time.Clock()

# window information
g = pygame.display.set_mode((g_width, g_height))
pygame.display.set_caption('Pew Pew - Test Build')


class Player:
    """
    Class for player

    Arguments:
        pos {tuple} -- (x position, y position)
    """

    def __init__(self, pos):
        sizex = 170
        sizey = sizex // 2
        self.image = pygame.transform.scale(
            pygame.image.load(os.path.join("data", "sprites", "player.png")),
            (sizex, sizey)
        )
        # self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speedx = 0
        self.speedy = 0
        self.hdg = 100

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        #constraints / boundaries
        if self.rect.right > g_width:
            self.rect.right = g_width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > g_height:
            self.rect.bottom = g_height

    def draw(self):
        img = pygame.transform.rotate(self.image, -self.hdg)
        rect = img.get_rect()
        pos = (self.rect.x - rect.width / 2, self.rect.y - rect.height / 2)
        g.blit(img, pos)
        self.rect.width, self.rect.height = rect.width, rect.height


class Bullet:
    """
    Class for bullets

    Arguments:
        pos {tuple} -- (x position, y position)
        hdg {int} -- heading angle
    """

    def __init__(self, pos, hdg):
        self.radius = 5
        self.rect = pygame.Rect(
            pos[0] - self.radius,
            pos[1] - self.radius,
            self.radius * 2,
            self.radius * 2
        )

        speed = 15
        self.speedx = cos(radians(hdg)) * speed
        self.speedy = sin(radians(hdg)) * speed

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

    def draw(self):
        pygame.draw.ellipse(g, pygame.Color("black"), self.rect)


def get_angle(pos1, pos2):
    """
    Get the angle between 2 points

    Arguments:
        pos1 {int} -- position of 1st object
        pos2 {int} -- position of 2nd object
    """

    dx = pos1[0] - pos2[0]
    dy = pos1[1] - pos2[1]
    return degrees(atan2(dy, dx))


all_sprites = []
player = Player((g_width / 2, g_height / 2))
all_sprites.append(player)


# game loop
while True:
    # keep game running at right speed
    clock.tick(fps)
    # process input (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullet = Bullet((player.rect.x, player.rect.y), player.hdg)
            all_sprites.append(bullet)
    # update
    mouse = pygame.mouse
    keystate = pygame.key.get_pressed()
    move_speed = 4

    if keystate[pygame.K_a] or keystate[pygame.K_LEFT]:
        player.speedx = -move_speed
    elif keystate[pygame.K_d] or keystate[pygame.K_RIGHT]:
        player.speedx = move_speed
    else:
        player.speedx = 0

    if keystate[pygame.K_w] or keystate[pygame.K_UP]:
        player.speedy = -move_speed
    elif keystate[pygame.K_s] or keystate[pygame.K_DOWN]:
        player.speedy = move_speed
    else:
        player.speedy = 0

    player.hdg = get_angle(mouse.get_pos(), (player.rect.x, player.rect.y))

    for sprite in all_sprites:
        sprite.update()
    #draw / render
    g.fill(pygame.Color("gray"))
    for sprite in all_sprites:
        sprite.draw()
    # *after* drawing everything, flip the display
    pygame.display.flip()
