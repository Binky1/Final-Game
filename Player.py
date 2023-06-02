import pygame
from spritesheet import Spritesheet

class Player:

    def __init__(self, xpos=-120, ypos=500, enemy = False):
        # xy pos, sprites for movement
        self.size = 120
        self.timeout = 0

        self.maxxpos = 800

        self.xpos = xpos
        self.ypos = ypos
        self.health = 100
        # self.sprite = Spritesheet('idle.png')
        # self.idle = [self.sprite.parse_sprite('__Boxing04_Idle_000.png'), self.sprite.parse_sprite('__Boxing04_Idle_001.png'), self.sprite.parse_sprite('__Boxing04_Idle_002.png'),self.sprite.parse_sprite('__Boxing04_Idle_003.png'), self.sprite.parse_sprite('__Boxing04_Idle_004.png'),self.sprite.parse_sprite('__Boxing04_Idle_005.png'), self.sprite.parse_sprite('__Boxing04_Idle_006.png'),  self.sprite.parse_sprite('__Boxing04_Idle_007.png'), self.sprite.parse_sprite('__Boxing04_Idle_008.png'), self.sprite.parse_sprite('__Boxing04_Idle_009.png')]
        # self.sprite = Spritesheet('punchleft.png')
        # self.punchleft = [self.sprite.parse_sprite('__Boxing04_PunchLeft_000.png'), self.sprite.parse_sprite('__Boxing04_PunchLeft_001.png'), self.sprite.parse_sprite('__Boxing04_PunchLeft_002.png'),self.sprite.parse_sprite('__Boxing04_PunchLeft_003.png'), self.sprite.parse_sprite('__Boxing04_PunchLeft_004.png'),self.sprite.parse_sprite('__Boxing04_PunchLeft_005.png')]
        # self.sprite = Spritesheet('walk.png')
        # self.walkright = [self.sprite.parse_sprite('__Boxing04_Walk_000.png'), self.sprite.parse_sprite('__Boxing04_Walk_001.png'), self.sprite.parse_sprite('__Boxing04_Walk_002.png'),self.sprite.parse_sprite('__Boxing04_Walk_003.png'), self.sprite.parse_sprite('__Boxing04_Walk_004.png'),self.sprite.parse_sprite('__Boxing04_Walk_005.png'), self.sprite.parse_sprite('__Boxing04_Walk_006.png'), self.sprite.parse_sprite('__Boxing04_Walk_007.png'), self.sprite.parse_sprite('__Boxing04_Walk_008.png'),self.sprite.parse_sprite('__Boxing04_Walk_009.png')]
        # self.sprite = Spritesheet('walkback.png')
        # self.walkleft = [self.sprite.parse_sprite('__Boxing04_WalkBack_000.png'), self.sprite.parse_sprite('__Boxing04_WalkBack_001.png'), self.sprite.parse_sprite('__Boxing04_WalkBack_002.png'),self.sprite.parse_sprite('__Boxing04_WalkBack_003.png'), self.sprite.parse_sprite('__Boxing04_WalkBack_004.png'),self.sprite.parse_sprite('__Boxing04_WalkBack_005.png'), self.sprite.parse_sprite('__Boxing04_WalkBack_006.png'), self.sprite.parse_sprite('__Boxing04_WalkBack_007.png'), self.sprite.parse_sprite('__Boxing04_WalkBack_008.png'),self.sprite.parse_sprite('__Boxing04_WalkBack_009.png')]
        # self.sprite = Spritesheet('dizzy.png')
        # self.dizzy = [self.sprite.parse_sprite('__Boxing04_Dizzy_000.png'), self.sprite.parse_sprite('__Boxing04_Dizzy_001.png'), self.sprite.parse_sprite('__Boxing04_Dizzy_002.png'),self.sprite.parse_sprite('__Boxing04_Dizzy_003.png'), self.sprite.parse_sprite('__Boxing04_Dizzy_004.png'),self.sprite.parse_sprite('__Boxing04_Dizzy_005.png'), self.sprite.parse_sprite('__Boxing04_Dizzy_006.png'), self.sprite.parse_sprite('__Boxing04_Dizzy_007.png')]
        # self.sprite = Spritesheet('block.png')
        # self.block = [self.sprite.parse_sprite('__Boxing04_Blocking_000.png'), self.sprite.parse_sprite('__Boxing04_Blocking_001.png'), self.sprite.parse_sprite('__Boxing04_Blocking_002.png'),self.sprite.parse_sprite('__Boxing04_Blocking_003.png'), self.sprite.parse_sprite('__Boxing04_Blocking_004.png'),self.sprite.parse_sprite('__Boxing04_Blocking_005.png'), self.sprite.parse_sprite('__Boxing04_Blocking_006.png'), self.sprite.parse_sprite('__Boxing04_Blocking_007.png'), self.sprite.parse_sprite('__Boxing04_Blocking_008.png'), self.sprite.parse_sprite('__Boxing04_Blocking_009.png')]
        # self.sprite = Spritesheet('ko.png')
        # self.block = [self.sprite.parse_sprite('__Boxing04_KO_000.png'), self.sprite.parse_sprite('__Boxing04_KO_001.png'), self.sprite.parse_sprite('__Boxing04_KO_002.png'),self.sprite.parse_sprite('__Boxing04_KO_003.png'), self.sprite.parse_sprite('__Boxing04_KO_004.png'),self.sprite.parse_sprite('__Boxing04_KO_005.png'), self.sprite.parse_sprite('__Boxing04_KO_006.png'), self.sprite.parse_sprite('__Boxing04_KO_007.png'), self.sprite.parse_sprite('__Boxing04_KO_008.png'), self.sprite.parse_sprite('__Boxing04_KO_009.png')]
        self.idle = self.create_sprite_list('Idle', 10)
        self.punchleft = self.create_sprite_list('PunchLeft', 6)
        self.walkright = self.create_sprite_list('Walk', 10)
        self.walkback = self.create_sprite_list('WalkBack', 10)
        self.dizzy = self.create_sprite_list('Dizzy', 8)
        self.block = self.create_sprite_list('Blocking', 10)
        self.ko = self.create_sprite_list('KO', 10)


        self.runningL = False
        self.runningR = False

        self.enemy = enemy
        self.queue = []

        self.state = 'idle'


        # sprite generators for every movement
        self.walkright_generator = self.walkright_player()
        self.walkleft_generator = self.walkleft_player()
        self.idle_generator = self.idle_player()
        self.punchleft_generator = self.punchleft_player()
        self.dizzy_generator = self.dizzy_player()
        self.block_generator = self.block_player()



    def create_sprite_list(self, filename, frames) -> list:
        try:
            sheet = Spritesheet(f'{filename}.png')
            return [sheet.parse_sprite(f"__Boxing04_{filename}_{str(i).zfill(3)}.png") for i in range(frames)]
            # lst = []
            # for i in range(frames):
            #     try:
            #         print(f"__Boxing04_{filename}_{str(i).zfill(3)}")
            #         sheet.parse_sprite(f"__Boxing04_{filename}_{str(i).zfill(3)}")
            #     except:
            #         print("dang it")

        except Exception as e:
            print(e)
            return None
    def walk_back(self, screen):
        self.queue = []
        # image = self.get_next(self.walkleft_generator)
        # image = pygame.transform.scale(image, (299, 299))
        # if self.enemy:
        #     image = pygame.transform.flip(image,True, False)
        # screen.blit(image, (self.xpos, self.ypos))

        self.runningL = True
        self.runningR = False
        
    def key_up(self):
        self.runningL = False
        self.runningR = False
    
    def walkright_sprite(self, x):
        self.queue = []
        self.maxxpos = x
        self.runningR = True
        self.runningL = False

        # print(kwargs.values())
        # image = self.get_next(self.walkright_generator)
        # image = pygame.transform.scale(image, (299, 299))
        # if self.enemy:
        #     image = pygame.transform.flip(image,True, False)
        # screen.blit(image, (self.xpos, self.ypos))

    def punch(self, p):
        print(p.state)
        if (abs((self.xpos + self.size) - p.xpos) < 130) and not self.enemy and p.state != 'block':
            if p.health >= 0:
                print('ee')
                p.health -= 10
            if p.health > 0 and p.health <= 10:
                p.dizzy_sprite()

        elif (abs((self.xpos - self.size) - p.xpos) < 130) and self.enemy and p.state != 'block':
            if p.health >= 0:
                print('hh')
                p.health -= 10
            if p.health > 0 and p.health <= 10:
                p.dizzy_sprite()

    def punchleft_sprite(self, screen, p):
        if self.timeout < 0:
            self.queue = []
            self.punch(p)
            self.timeout = 35
            image = self.get_next(self.punchleft_generator)
            # image = pygame.transform.scale(image, (299, 299))
            # if self.enemy:
            #     image = pygame.transform.flip(image,True, False)
            #
            #screen.blit(image, (self.xpos, self.ypos))
            self.queue.append(self.get_next(self.punchleft_generator))
            self.queue.append(self.get_next(self.punchleft_generator))
            self.queue.append(self.get_next(self.punchleft_generator))
            self.queue.append(self.get_next(self.punchleft_generator))
            self.queue.append(self.get_next(self.punchleft_generator))


    def block_sprite(self):
        self.queue = []
        image = self.get_next(self.block_generator)
        # image = pygame.transform.scale(image, (299, 299))
        # if self.enemy:
        #     image = pygame.transform.flip(image,True, False)
        #
        # screen.blit(image, (self.xpos, self.ypos))
        self.queue.append(self.get_next(self.block_generator))
        self.queue.append(self.get_next(self.block_generator))
        self.queue.append(self.get_next(self.block_generator))
        self.queue.append(self.get_next(self.block_generator))
        self.queue.append(self.get_next(self.block_generator))
        self.queue.append(self.get_next(self.block_generator))
        self.queue.append(self.get_next(self.block_generator))
        self.queue.append(self.get_next(self.block_generator))

        self.queue.append(self.get_next(self.block_generator))
        self.queue.append(self.get_next(self.block_generator))
        self.queue.append(self.get_next(self.block_generator))
        self.queue.append(self.get_next(self.block_generator))
        self.queue.append(self.get_next(self.block_generator))
        self.queue.append(self.get_next(self.block_generator))
        self.queue.append(self.get_next(self.block_generator))
        self.queue.append(self.get_next(self.block_generator))
    
    def dizzy_sprite(self):
        self.queue = []
        
        image = self.get_next(self.dizzy_generator)
        # image = pygame.transform.scale(image, (299, 299))
        # if self.enemy:
        #     image = pygame.transform.flip(image,True, False)
        #
        #screen.blit(image, (self.xpos, self.ypos))
        self.queue.append(self.get_next(self.dizzy_generator))
        self.queue.append(self.get_next(self.dizzy_generator))
        self.queue.append(self.get_next(self.dizzy_generator))
        self.queue.append(self.get_next(self.dizzy_generator))
        self.queue.append(self.get_next(self.dizzy_generator))
        self.queue.append(self.get_next(self.dizzy_generator))
        self.queue.append(self.get_next(self.dizzy_generator))
        self.queue.append(self.get_next(self.dizzy_generator))
        self.queue.append(self.get_next(self.dizzy_generator))
        self.queue.append(self.get_next(self.dizzy_generator))
        self.queue.append(self.get_next(self.dizzy_generator))
        self.queue.append(self.get_next(self.dizzy_generator))
        self.queue.append(self.get_next(self.dizzy_generator))
        self.queue.append(self.get_next(self.dizzy_generator))
        self.queue.append(self.get_next(self.dizzy_generator))
        self.queue.append(self.get_next(self.dizzy_generator))
        self.queue.append(self.get_next(self.dizzy_generator))
        self.queue.append(self.get_next(self.dizzy_generator))
        self.queue.append(self.get_next(self.dizzy_generator))
        self.queue.append(self.get_next(self.dizzy_generator))
        

    def draw_player_frame(self, screen):

        self.timeout -= 1
        if self.runningR:
            if self.enemy:
                #print("enemy")
                pass
            else:
                #print("not")
                pass
            image = self.get_next(self.walkright_generator)
            image = pygame.transform.scale(image, (299, 299))        
            
        elif self.runningL:
            image = self.get_next(self.walkleft_generator)
            image = pygame.transform.scale(image, (299, 299))           
            
        elif len(self.queue) != 0:
            image = self.queue.pop(0)
            image = pygame.transform.scale(image, (299, 299))
            
        else:
            image = self.get_next(self.idle_generator)
            image = pygame.transform.scale(image, (299, 299))

        if self.enemy:
            image = pygame.transform.flip(image,True, False)   
        screen.blit(image, (self.xpos, self.ypos))

    
    def get_next(self, var):
        return next(var)


    def walkleft_player(self):
        i = 0
        while i < len(self.walkback):
            #screen.blit(self.idle[i], (100, 50))
            if self.xpos +120 - 3 > 0 and self.enemy == False:
                self.xpos -=3
            elif self.xpos + 3 < 800 and self.enemy == True:
                self.xpos +=3
            yield self.walkback[i]
            i = (i + 1) % len(self.walkback)

    def walkright_player(self):
        i = 0
        while i < len(self.walkright):
            #screen.blit(self.idle[i], (100, 50))
            if self.xpos + 6 < self.maxxpos - 100 and self.enemy == False:
                self.xpos +=4
            elif self.xpos - 3 > self.maxxpos + 100 and self.enemy == True:
                self.xpos -=4
            yield self.walkright[i]
            i = (i + 1) % len(self.walkright)
            #print(i)


    def punchleft_player(self):
        i = 0
        while i < len(self.punchleft):
            #screen.blit(self.idle[i], (100, 50))
            yield self.punchleft[i]
            i = (i + 1) % len(self.punchleft)
            #print(i)

    def dizzy_player(self):
        i = 0
        while i < len(self.dizzy):
            #screen.blit(self.idle[i], (100, 50))
            yield self.dizzy[i]
            i = (i + 1) % len(self.dizzy)
            #print(i)

    def block_player(self):
        i = 0
        while i < len(self.block):
            #screen.blit(self.idle[i], (100, 50))
            yield self.block[i]
            i = (i + 1) % len(self.block)
            #print(i)


    def idle_player(self):
        i = 0
        while i < len(self.idle):
            #screen.blit(self.idle[i], (100, 50))
            yield self.idle[i]
            i = (i + 1) % len(self.idle)