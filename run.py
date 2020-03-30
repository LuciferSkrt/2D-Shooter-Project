import sys
import pygame
from game.main import Game


def main():
    g = Game((1024, 700), "Pew Pew!")
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
    sys.exit() # @Alex, sys.exit() does the same thing as quit() but its recommended over quit().
