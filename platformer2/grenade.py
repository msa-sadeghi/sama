from pygame.sprite import Sprite
import pygame

class Grenade(Sprite):
    def __init__(self, x,y, group, direction):
        super().__init__()
        self.image = pygame.image.load("./assets/images/icons/grenade.png")
        self.rect = self.image.get_rect(topleft=(x,y))
        self.direction = direction
        self.yspeed = 0
        group.add(self)
        
    def update(self):
        self.yspeed += 1
        self.rect.x += 4 * self.direction
        self.rect.y += self.yspeed
        
    
        