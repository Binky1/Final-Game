import os, sys, time
import pygame

from pygame.locals import *
from Player import Player


pygame.init()
 
fps = 25
fpsClock = pygame.time.Clock()
 
width, height = 1300, 800
screen = pygame.display.set_mode((width, height))
screen.fill((255, 255, 255))

p = Player()

idle_generator = p.idle_player(screen)
punchleft_generator = p.punchleft_player()
walkright_generator = p.walkright_player()

queue = []

running = False


def main():
    # Game loop.
    while True:
        screen.fill((255, 255, 255))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == pygame.K_a:
                    global queue
                    queue = []
                    image = next(punchleft_generator)
                    image = pygame.transform.scale(image, (299, 299))
                    screen.blit(image, (p.xpos, p.ypos))
                    queue.append(next(punchleft_generator))
                    queue.append(next(punchleft_generator))
                    queue.append(next(punchleft_generator))
                    queue.append(next(punchleft_generator))
                    queue.append(next(punchleft_generator))
                    pygame.display.flip()
                    fpsClock.tick(fps)
                    continue
                elif event.key == pygame.K_d:
                    print(queue)
                    queue = []
                    image = next(walkright_generator)
                    image = pygame.transform.scale(image, (299, 299))
                    screen.blit(image, (p.xpos, p.ypos))
                    global running
                    running = True
                    pygame.display.flip()
                    fpsClock.tick(fps)
                    continue
            elif event.type == KEYUP:
                if event.key == K_d:
                    running = False

            # else:
            #     image = next(idle_generator)
            #     screen.blit(image, (100, 50))

        if running:
            image = next(walkright_generator)
            image = pygame.transform.scale(image, (299, 299))           
            screen.blit(image, (p.xpos, p.ypos))
        elif len(queue) != 0:
            image = queue.pop(0)
            image = pygame.transform.scale(image, (299, 299))
            screen.blit(image, (p.xpos, p.ypos))
        else:
            image = next(idle_generator)
            image = pygame.transform.scale(image, (299, 299))
            screen.blit(image, (p.xpos, p.ypos))

        pygame.display.flip()
        fpsClock.tick(fps)
        
    


if __name__ == '__main__':
    main()