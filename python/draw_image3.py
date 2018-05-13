import sys

import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((400, 300))
FPSCLOCK = pygame.time.Clock()


def main():
    logo = pygame.image.load("pythonlogo.jpg")
    theta = 0

    while True:
        for event in pygame.event.get(QUIT):
            pygame.quit()
            sys.exit()

        theta += 1

        SURFACE.fill((225, 225, 225))

        # ロゴを回転し、左上が(100, 30)の位置にロゴを描画
        new_logo = pygame.transform.rotate(logo, theta)
        SURFACE.blit(new_logo, (100, 30))

        pygame.display.update()
        FPSCLOCK.tick(30)


if __name__ == '__main__':
    main()
