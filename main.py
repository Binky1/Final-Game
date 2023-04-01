import os, sys, time
import pygame
import pickle

from pygame.locals import *
from Player import Player

import socket
import tcp_by_size


pygame.init()
 
fps = 25
fpsClock = pygame.time.Clock()
 
width, height = 1300, 800
screen = pygame.display.set_mode((width, height))
screen.fill((255, 255, 255))

sock = socket.socket()
sock.connect(("127.0.0.1", 8000))

p = Player()
p2 = Player()
queue = []



def draw_screen(screen, p, p2):
    p.draw_player_frame(screen)
    p2.draw_player_frame(screen)
    pygame.display.update()



def main():
    # Game loop.
    while True:
        screen.fill((0, 0, 0))
        #send_player(p)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == pygame.K_k:
                    p.punchleft_sprite(screen)
                elif event.key == pygame.K_d:
                    p.walkright_sprite(screen)
                elif event.key == pygame.K_a:
                    p.walk_back(screen)

            elif event.type == KEYUP:
                p.key_up()

            
        draw_screen(screen, p, p2)
        fpsClock.tick(fps)
        
    


if __name__ == '__main__':
    main()