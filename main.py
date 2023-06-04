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

SMALLFONT = pygame.font.SysFont('Corbel',35)
 
width, height = 1000, 800
screen = pygame.display.set_mode((width, height))
screen.fill((255, 255, 255))

sock = socket.socket()
sock.connect(("127.0.0.1", 8001))


print('in')
p = Player()
p2 = Player(800, 500, True)
queue = []


i = 0
x = 0

def reset_players(p, p2):
    p.initialize_all()
    p2.initialize_all(800, 500, True)

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
        p2.state = 'punch'
        p2.punchleft_sprite(screen, p)
    elif data == 'block':
        p2.state = 'block'
        p2.block_sprite()
    elif data == 'moveright':
        p2.state = 'moveright'
        p2.walkright_sprite(p.xpos)
    elif data == 'moveleft':
        p2.state = 'moveleft'
        p2.walk_back(screen)
    elif data == 'idle':
        p2.state = 'idle'
        p2.key_up()

def menu():

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == pygame.K_SPACE:
                    #TODO send server message that intialize the game in the server
                    main()

        screen.fill((0, 0, 0))
        text = SMALLFONT.render('Press SPACE To Start' , True , (255,255,255))
        screen.blit(text, (width/2-130, height/2-20))
        pygame.display.flip()




def GameOver():

    cont = True
    global p, p2
    if p.health == 0:
        text = SMALLFONT.render('You Lose!', True, (255, 255, 255))
    else:
        text = SMALLFONT.render('You Win!', True, (255, 255, 255))
    while cont:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == pygame.K_SPACE:
                    cont = False
        screen.fill((0,0,0))
        screen.blit(text, (width / 2 - 130, height / 2 - 20))
        pygame.display.flip()
    tcp_by_size.send_with_size(sock, 'NGME')
    reset_players(p,p2)



def main():


    frames = 1
    state = 'idle'
    # Game loop.
    tcp_by_size.send_with_size(sock, state)
    while not p.gameover:
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
                    p.state = state
                    p.punchleft_sprite(screen, p2)
                elif event.key == pygame.K_SPACE:
                    state = 'block'
                    p.state = state
                    p.block_sprite()
                elif event.key == pygame.K_d:
                    state = 'moveright'
                    p.state = state
                    p.walkright_sprite(p2.xpos)
                elif event.key == pygame.K_a:
                    state = 'moveleft'
                    p.state = state
                    p.walk_back(screen)
                else:
                    state = 'idle'
                    p.state = state
                    p.key_up()

            elif event.type == KEYUP:
                state = 'idle'
                p.state = state
                p.key_up()

        send(state)
        if state == 'punch':
            state = 'idle'
            p.state = state
        draw_screen(screen, p, p2)
        fpsClock.tick(fps)
        frames += 1
    print('end')
    GameOver()
    


if __name__ == '__main__':
    menu()