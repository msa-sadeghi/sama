from pygame.sprite import Sprite
import pygame
from constants import SCREEN_HEIGHT
class Egg(Sprite):
    def __init__(self, x,y, group):
        super().__init__()
        self.image = pygame.image.load("assets/egg.png")
        self.rect = self.image.get_rect(centerx = x, top = y)
        group.add(self)
        
    def update(self):
        self.rect.y += 5
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()