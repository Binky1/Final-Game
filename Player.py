import pygame
from spritesheet import Spritesheet

class Player:

    def __init__(self):
        self.xpos = 80
        self.ypos = 500
        self.sprite = Spritesheet('idle.png')
        self.idle = [self.sprite.parse_sprite('__Boxing04_Idle_000.png'), self.sprite.parse_sprite('__Boxing04_Idle_001.png'), self.sprite.parse_sprite('__Boxing04_Idle_002.png'),self.sprite.parse_sprite('__Boxing04_Idle_003.png'), self.sprite.parse_sprite('__Boxing04_Idle_004.png'),self.sprite.parse_sprite('__Boxing04_Idle_005.png'), self.sprite.parse_sprite('__Boxing04_Idle_006.png'),  self.sprite.parse_sprite('__Boxing04_Idle_007.png'), self.sprite.parse_sprite('__Boxing04_Idle_008.png'), self.sprite.parse_sprite('__Boxing04_Idle_009.png')]
        self.sprite = Spritesheet('punchleft.png')
        self.punchleft = [self.sprite.parse_sprite('__Boxing04_PunchLeft_000.png'), self.sprite.parse_sprite('__Boxing04_PunchLeft_001.png'), self.sprite.parse_sprite('__Boxing04_PunchLeft_002.png'),self.sprite.parse_sprite('__Boxing04_PunchLeft_003.png'), self.sprite.parse_sprite('__Boxing04_PunchLeft_004.png'),self.sprite.parse_sprite('__Boxing04_PunchLeft_005.png')]
        self.sprite = Spritesheet('walk.png')
        self.walkright = [self.sprite.parse_sprite('__Boxing04_Walk_000.png'), self.sprite.parse_sprite('__Boxing04_Walk_001.png'), self.sprite.parse_sprite('__Boxing04_Walk_002.png'),self.sprite.parse_sprite('__Boxing04_Walk_003.png'), self.sprite.parse_sprite('__Boxing04_Walk_004.png'),self.sprite.parse_sprite('__Boxing04_Walk_005.png'), self.sprite.parse_sprite('__Boxing04_Walk_006.png'), self.sprite.parse_sprite('__Boxing04_Walk_007.png'), self.sprite.parse_sprite('__Boxing04_Walk_008.png'),self.sprite.parse_sprite('__Boxing04_Walk_009.png')]
        


    def walkright_player(self):
        i = 0
        while i < len(self.walkright):
            #screen.blit(self.idle[i], (100, 50))
            if self.xpos + 6 < 1064:
                self.xpos +=6
                print(self.xpos)
            yield self.walkright[i]
            i = (i + 1) % len(self.walkright)


    def punchleft_player(self):
        i = 0
        while i < len(self.punchleft):
            #screen.blit(self.idle[i], (100, 50))
            yield self.punchleft[i]
            i = (i + 1) % len(self.punchleft)

    def idle_player(self, screen):
        i = 0
        while i < len(self.idle):
            #screen.blit(self.idle[i], (100, 50))
            yield self.idle[i]
            i = (i + 1) % len(self.idle)
