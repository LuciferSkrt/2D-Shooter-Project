import sys
import pygame


class Game:
    def __init__(self, win_size):
        self.width = win_size[0]
        self.height = win_size[1]
        self.win = pygame.display.set_mode(win_size)
        pygame.display.set_caption("Pew Pew!")

    def input(self, keys):
        pass

    def update(self, delta):
        print(delta)

    def render(self, window):
        pass


def main():
    g = Game((1024, 700))
    clock = pygame.time.Clock()
    fps = 60

    while True:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        g.input(pygame.key.get_pressed())
        g.update(clock.get_time() / 1000)
        g.render(g.win)


if __name__ == "__main__":
    main()
    sys.exit()
