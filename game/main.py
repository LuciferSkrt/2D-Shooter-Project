import pygame
from glm import vec2

from game.shooter import Shooter


class Game:
    def __init__(self, win_size, title):
        self.width = win_size[0]
        self.height = win_size[1]
        self.win = pygame.display.set_mode(win_size)
        pygame.display.set_caption(title)

        self.background = pygame.Color(180, 180, 180)
        self.mouse = pygame.mouse

        self.player = Shooter(
            vec2(self.width / 2, self.height / 2), vec2(350)
        )

    def input(self, keys):
        velocity = vec2(0)

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            velocity.x = -1
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            velocity.x = 1

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            velocity.y = -1
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            velocity.y = 1

        self.player.move(velocity)

    def update(self, delta):
        self.player.look_at(vec2(self.mouse.get_pos()))
        self.player.update(delta)

    def render(self, window):
        window.fill(self.background)

        self.player.render(window)

        pygame.display.update()
