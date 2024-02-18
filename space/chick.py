from pygame.sprite import Sprite
import pygame
class Chick(Sprite):
    def __init__(self, x,y, group):
        super().__init__()
        self.image = pygame.image.load("assets/chick.png")
        self.rect = self.image.get_rect(topleft=(x,y))
        
        self.direction = 1
        self.speed = 5
        group.add(self)
        
    def update(self):
        self.rect.x += self.speed * self.direction
        
        