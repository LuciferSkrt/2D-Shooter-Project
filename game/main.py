import pygame


class Game:
    def __init__(self, win_size, title):
        self.width = win_size[0]
        self.height = win_size[1]
        self.win = pygame.display.set_mode(win_size)
        pygame.display.set_caption(title)

    def input(self, keys):
        pass

    def update(self, delta):
        print(delta)

    def render(self, window):
        pass
