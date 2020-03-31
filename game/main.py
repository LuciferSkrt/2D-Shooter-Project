#modules and imports
import sys
import random
import pygame

# initializer
pygame.init()
pygame.mixer.init()

# window size
g_width = 1100
g_height = 600

# framerate
fps = 60
clock = pygame.time.Clock()

# colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# window information
g = pygame.display.set_mode((g_width, g_height))
pygame.display.set_caption('Pew Pew - Test Build')


class Player(pygame.sprite.Sprite):
    # sprite for the player
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.center = (g_width / 2, g_height / 2)
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = -4
        if keystate[pygame.K_d]:
            self.speedx = 4
        self.rect.x += self.speedx
        if keystate[pygame.K_w]:
            self.speedy = -4
        if keystate[pygame.K_s]:
            self.speedy = 4
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


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)


# game loop
while True:
    # keep game running at right speed
    clock.tick(fps)
    # process input (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # update
    all_sprites.update()
    #draw / render
    g.fill(black)
    all_sprites.draw(g)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
