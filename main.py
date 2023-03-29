import os, sys
import pygame

from pygame.locals import *
from Player import Player

pygame.init()
 
fps = 60
fpsClock = pygame.time.Clock()
 
width, height = 1541, 540
screen = pygame.display.set_mode((width, height))

background = pygame.image.load(os.path.join("Assets", "bg.jpg"))

p1 = Player()

def main():
    # Game loop.
    while True:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


        screen.blit(background, (0,0))
        screen.blit(p1.image, (0,0))
        pygame.display.flip()
        fpsClock.tick(fps)
    


if __name__ == '__main__':
    main()