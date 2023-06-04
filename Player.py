import pygame
from spritesheet import Spritesheet

class Player:

    def __init__(self, xpos=-120, ypos=500, enemy = False):
        # xy pos, sprites for movement
        self.enemy = enemy
        self.size = 120
        self.timeout = 0


        #temp
        self.gameover = False



        self.maxxpos = 800

        self.xpos = xpos
        self.ypos = ypos
        self.health = 100

        if self.enemy:
            self.idle = self.create_sprite_list('Idle', 10)
            self.punchleft = self.create_sprite_list('PunchLeft', 6)
            self.walkright = self.create_sprite_list('Walk', 10)
            self.walkback = self.create_sprite_list('WalkBack', 10)
            self.dizzy = self.create_sprite_list('Dizzy', 8)
            self.block = self.create_sprite_list('Blocking', 10)
            self.ko = self.create_sprite_list('KO', 10)
            self.hurt = self.create_sprite_list('Hurt', 8)
        else:
            self.idle = self.create_sprite_list('Idle2', 10)
            self.punchleft = self.create_sprite_list('PunchLeft2', 6)
            self.walkright = self.create_sprite_list('Walk2', 10)
            self.walkback = self.create_sprite_list('WalkBack2', 10)
            self.dizzy = self.create_sprite_list('Dizzy2', 8)
            self.block = self.create_sprite_list('Blocking2', 10)
            self.ko = self.create_sprite_list('KO2', 10)
            self.hurt = self.create_sprite_list('Hurt2', 8)

        self.runningL = False
        self.runningR = False


        self.queue = []

        self.state = 'idle'


        # sprite generators for every movement
        self.walkright_generator = self.walkright_player()
        self.walkleft_generator = self.walkleft_player()
        self.idle_generator = self.idle_player()
        self.punchleft_generator = self.punchleft_player()
        self.dizzy_generator = self.dizzy_player()
        self.block_generator = self.block_player()
        self.ko_generator = self.ko_player()
        self.hurt_generator = self.hurt_player()

    def initialize_all(self, xpos=-120, ypos=500, enemy = False):
        self.enemy = enemy
        self.size = 120
        self.timeout = 0

        # temp
        self.gameover = False

        self.maxxpos = 800

        self.xpos = xpos
        self.ypos = ypos
        self.health = 100

        if self.enemy:
            self.idle = self.create_sprite_list('Idle', 10)
            self.punchleft = self.create_sprite_list('PunchLeft', 6)
            self.walkright = self.create_sprite_list('Walk', 10)
            self.walkback = self.create_sprite_list('WalkBack', 10)
            self.dizzy = self.create_sprite_list('Dizzy', 8)
            self.block = self.create_sprite_list('Blocking', 10)
            self.ko = self.create_sprite_list('KO', 10)
        else:
            self.idle = self.create_sprite_list('Idle2', 10)
            self.punchleft = self.create_sprite_list('PunchLeft2', 6)
            self.walkright = self.create_sprite_list('Walk2', 10)
            self.walkback = self.create_sprite_list('WalkBack2', 10)
            self.dizzy = self.create_sprite_list('Dizzy2', 8)
            self.block = self.create_sprite_list('Blocking2', 10)
            self.ko = self.create_sprite_list('KO2', 10)

        self.runningL = False
        self.runningR = False

        self.queue = []

        self.state = 'idle'

        # sprite generators for every movement
        self.walkright_generator = self.walkright_player()
        self.walkleft_generator = self.walkleft_player()
        self.idle_generator = self.idle_player()
        self.punchleft_generator = self.punchleft_player()
        self.dizzy_generator = self.dizzy_player()
        self.block_generator = self.block_player()
        self.ko_generator = self.ko_player()


    def create_sprite_list(self, filename, frames) -> list:
        try:
            sheet = Spritesheet(f'{filename}.png')
            return [sheet.parse_sprite(f"__Boxing04_{filename.replace('2','')}_{str(i).zfill(3)}.png") for i in range(frames)]
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
                p.hurt_sprite()

            if p.health == 0:
                p.KO_sprite()
                self.gameover = True
                return True
            elif p.health > 0 and p.health <= 10:
                p.dizzy_sprite()

        elif (abs((self.xpos - self.size) - p.xpos) < 130) and self.enemy and p.state != 'block':
            if p.health >= 0:
                print('hh')
                p.health -= 10
                p.hurt_sprite()

            if p.health == 0:
                p.KO_sprite()
                p.gameover = True
                return True
            elif p.health > 0 and p.health <= 10:
                p.dizzy_sprite()

        return False

    def punchleft_sprite(self, screen, p) -> bool:
        # if self.timeout < 0:
        self.queue = []
        gameState = self.punch(p)
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
        return gameState
        # return False


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

    def hurt_sprite(self):
        self.queue = []
        image = self.get_next(self.hurt_generator)

        for i in range(7):
            self.queue.append(self.get_next(self.hurt_generator))

    def KO_sprite(self):
        self.queue = []
        image = self.get_next(self.ko_generator)

        self.queue.append(self.get_next(self.ko_generator))
        self.queue.append(self.get_next(self.ko_generator))
        self.queue.append(self.get_next(self.ko_generator))
        self.queue.append(self.get_next(self.ko_generator))
        self.queue.append(self.get_next(self.ko_generator))
        self.queue.append(self.get_next(self.ko_generator))
        self.queue.append(self.get_next(self.ko_generator))
        self.queue.append(self.get_next(self.ko_generator))

        image = self.get_next((self.ko_generator))
        for i in range(25*3):
            self.queue.append(image)

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


    def hurt_player(self):
        i = 0
        while i < len(self.hurt):
            #screen.blit(self.idle[i], (100, 50))
            yield self.hurt[i]
            i = (i + 1) % len(self.hurt)
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


    def ko_player(self):
        i = 0
        while i < len(self.ko):
            #screen.blit(self.idle[i], (100, 50))
            yield self.ko[i]
            i = (i + 1) % len(self.ko)
            #print(i)


    def idle_player(self):
        i = 0
        while i < len(self.idle):
            #screen.blit(self.idle[i], (100, 50))
            yield self.idle[i]
            i = (i + 1) % len(self.idle)