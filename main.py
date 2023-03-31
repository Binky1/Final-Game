import os, sys, time
import pygame

from pygame.locals import *
from Player import Player


pygame.init()
 
fps = 30
fpsClock = pygame.time.Clock()
 
width, height = 1300, 800
screen = pygame.display.set_mode((width, height))
screen.fill((255, 255, 255))

p = Player()



queue = []

runningR = False # running right
runningL = False # running Left


def main():
    # Game loop.
    while True:
        screen.fill((255, 255, 255))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == pygame.K_k:
                    global queue
                    queue = []
                    image = p.get_next(p.punchleft_generator)
                    image = pygame.transform.scale(image, (299, 299))
                    screen.blit(image, (p.xpos, p.ypos))
                    queue.append(p.get_next(p.punchleft_generator))
                    queue.append(p.get_next(p.punchleft_generator))
                    queue.append(p.get_next(p.punchleft_generator))
                    queue.append(p.get_next(p.punchleft_generator))
                    queue.append(p.get_next(p.punchleft_generator))
                    pygame.display.flip()
                    fpsClock.tick(fps)
                    continue
                elif event.key == pygame.K_d:

                    print(queue)
                    queue = []
                    # image = next(walkright_generator)
                    image = p.get_next(p.walkright_generator)
                    image = pygame.transform.scale(image, (299, 299))
                    screen.blit(image, (p.xpos, p.ypos))
                    global runningR
                    global runningL
                    runningR = True
                    runningL = False
                    pygame.display.flip()
                    fpsClock.tick(fps)
                    continue
                elif event.key == pygame.K_a:
                    
                    queue = []
                    image = p.get_next(p.walkleft_generator)
                    image = pygame.transform.scale(image, (299, 299))
                    screen.blit(image, (p.xpos, p.ypos))

                    runningL = True
                    runningR = False
                    
                    pygame.display.flip()
                    fpsClock.tick(fps)
                    continue
            elif event.type == KEYUP:
                if event.key == K_d:
                    runningR = False
                elif event.key == K_a:
                    runningL = False

            # else:
            #     image = next(idle_generator)
            #     screen.blit(image, (100, 50))

        if runningR:
            image = p.get_next(p.walkright_generator)
            image = pygame.transform.scale(image, (299, 299))        
            screen.blit(image, (p.xpos, p.ypos))
        elif runningL:
            image = p.get_next(p.walkleft_generator)
            image = pygame.transform.scale(image, (299, 299))           
            screen.blit(image, (p.xpos, p.ypos))
        elif len(queue) != 0:
            image = queue.pop(0)
            image = pygame.transform.scale(image, (299, 299))
            screen.blit(image, (p.xpos, p.ypos))
        else:
            image = p.get_next(p.idle_generator)
            image = pygame.transform.scale(image, (299, 299))
            screen.blit(image, (p.xpos, p.ypos))

        pygame.display.flip()
        fpsClock.tick(fps)
        
    


if __name__ == '__main__':
    main()