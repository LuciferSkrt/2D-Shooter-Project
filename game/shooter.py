import os
from math import atan2, degrees

import pygame
from glm import vec2


class Shooter:
    """
    Shooter Class

    Arguments:
        start_pos {vec2} -- Starting position
        speed {vec2} -- Movement speed
    """

    def __init__(self, start_pos, speed):
        self.pos = start_pos
        self.speed = speed
        self.vel = vec2(0)
        self.hdg = 90

        scale_x = 170
        scale_y = int(scale_x / 2)
        self.img = pygame.transform.scale(
            pygame.image.load(os.path.join("data", "sprites", "player.png")),
            (scale_x, scale_y)
        )
        self.rect = self.img.get_rect()

    def look_at(self, pos: vec2):
        dx = pos.x - self.pos.x
        dy = pos.y - self.pos.y
        angle = atan2(dy, dx)
        self.hdg = degrees(angle)

    def move(self, vec: vec2):
        self.vel = self.speed * vec

    def update(self, delta):
        self.pos += self.vel * delta

    def render(self, window: pygame.Surface):
        img = pygame.transform.rotate(self.img, -self.hdg)
        rect = img.get_rect()
        pos = (self.pos.x - rect.width / 2, self.pos.y - rect.height / 2)

        window.blit(img, pos)
        self.rect = rect
