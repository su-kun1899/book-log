import sys

import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((400, 300))
FPSCLOCK = pygame.time.Clock()


def main():
    # noinspection PyUnresolvedReferences
    logo = pygame.image.load("pythonlogo.jpg")
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((225, 225, 225))

        # 左上が(20,50)の位置にロゴを描画
        SURFACE.blit(logo, (20, 50))

        pygame.display.update()
        FPSCLOCK.tick(30)


if __name__ == '__main__':
    main()
