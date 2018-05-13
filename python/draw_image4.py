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
        for _ in pygame.event.get(QUIT):
            pygame.quit()
            sys.exit()

        theta += 1

        SURFACE.fill((225, 225, 225))

        # ロゴを回転し、中心が(200, 150)の位置にロゴを描画
        new_logo = pygame.transform.rotate(logo, theta)
        rect = new_logo.get_rect()
        rect.center = (200, 150)
        SURFACE.blit(new_logo, rect)

        pygame.display.update()
        FPSCLOCK.tick(30)


if __name__ == '__main__':
    main()
