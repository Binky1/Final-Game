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
 
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
screen.fill((255, 255, 255))

sock = socket.socket()
sock.connect(("127.0.0.1", 8000))

p = Player()
p2 = Player(300, 500, True)
queue = []



def draw_screen(screen, p, p2):
    p.draw_player_frame(screen)
    p2.draw_player_frame(screen)
    pygame.display.update()



def parse_protocol(p2, data, screen):
    if data == 'punch':
        p2.punchleft_sprite(screen)
    elif data == 'moveright':
        p2.walkright_sprite(screen)
    elif data == 'moveleft':
        p2.walk_back(screen)
    else:
        p2.key_up()


def main():
    state = 'idle'
    # Game loop.
    while True:
        screen.fill((0, 0, 0))
        #send_player(p)
        #p.do()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == pygame.K_k:
                    state = 'punch'
                    tcp_by_size.send_with_size(sock, "hello")
                    print(tcp_by_size.recv_by_size(sock))
                    p.punchleft_sprite(screen)
                elif event.key == pygame.K_d:
                    state = 'moveright'
                    p.walkright_sprite(screen)
                elif event.key == pygame.K_a:
                    state = 'moveleft'
                    p.walk_back(screen)

            elif event.type == KEYUP:
                state = 'idle'
                p.key_up()

        #send(p, p2)
        tcp_by_size.send_with_size(sock, state)
        data = tcp_by_size.recv_by_size(sock)
        parse_protocol(p2, data, screen)

        draw_screen(screen, p, p2)
        fpsClock.tick(fps)
        
    


if __name__ == '__main__':
    main()