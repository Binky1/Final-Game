import os, sys, time
import pygame
from Player import Player
from pygame.locals import *
import socket
import tcp_by_size
import threading


pygame.init()
 
fps = 25
fpsClock = pygame.time.Clock()
 
width, height = 1000, 800
screen = pygame.display.set_mode((width, height))
screen.fill((255, 255, 255))

sock = socket.socket()
sock.connect(("127.0.0.1", 8001))



p = Player()
p2 = Player(300, 500, True)
#p2 = Player(800, 500, True)
queue = []


i = 0
x = 0

def send(state):
    tcp_by_size.send_with_size(sock, state)
    if state == 'punch':
        global i
        i += 1
        print(i)
    # if state == 'moveright':
    #     global i
    #     i += 1
        # print('++++++++++++++++ ' + str(i))
    data = tcp_by_size.recv_by_size(sock)
    # print(data)
    # if data == 'moveright':
    #     global x
    #     x += 1
        # print('++++++++++++++++ ' + str(x))
    
    parse_protocol(p2, data, screen)

def draw_health(p: Player):

    color = (0,255,0)
    if p.health < 70:
        color = (255,165,0)
    if p.health < 30:
        color = (255,0,0)
    if not p.enemy:
        pygame.draw.rect(screen, color, pygame.Rect(30, 30, p.health * 2, 20))
    else:
        pygame.draw.rect(screen, color, pygame.Rect(780, 30, p.health * 2, 20))
        
def draw_screen(screen, p, p2):
    p.draw_player_frame(screen)
    p2.draw_player_frame(screen)
    draw_health(p)
    draw_health(p2)
    pygame.display.flip()



def parse_protocol(p2, data, screen):
    if data == 'punch':
        p2.punchleft_sprite(screen, p)
    elif data == 'moveright':
        p2.walkright_sprite(screen)
    elif data == 'moveleft':
        p2.walk_back(screen)
    elif data == 'idle':
        p2.key_up()



def main():
    
    
    frames = 1
    state = 'idle'
    # Game loop.
    while True:
        # print(frames)
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
                    
                    p.punchleft_sprite(screen, p2)
                elif event.key == pygame.K_d:
                    state = 'moveright'
                    p.walkright_sprite(screen)
                elif event.key == pygame.K_a:
                    state = 'moveleft'
                    p.walk_back(screen)

            elif event.type == KEYUP:
                state = 'idle'
                p.key_up()

        send(state)
        if state == 'punch':
            state = 'idle'
        draw_screen(screen, p, p2)
        fpsClock.tick(fps)
        frames += 1
        
    


if __name__ == '__main__':
    main()