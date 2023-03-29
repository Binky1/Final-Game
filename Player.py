import pygame, os
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load(os.path.join("Assets", "y.jpg"))