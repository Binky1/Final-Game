import pygame
import json


class Spritesheet:

    def __init__(self, filename):
        self.filename = filename
        self.sprite = pygame.image.load(filename).convert()
        self.jsonfile = self.filename.replace('.png', '.json')
        with open(self.jsonfile, 'r') as f:
            self.data = json.load(f)

    

    def get_sprite(self, x, y, w, h):
        sprite = pygame.Surface((w, h))
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.sprite,(0, 0),(x, y, w, h))
        return sprite

    def parse_sprite(self, name):
        sprite = self.data['frames'][name]['frame']
        x, y, w, h = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
        image = self.get_sprite(x, y, w, h)
        return image