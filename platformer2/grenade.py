from pygame.sprite import Sprite
import pygame

class Grenade(Sprite):
    def __init__(self, x,y, group, direction):
        super().__init__()
        self.image = pygame.image.load("./assets/images/icons/grenade.png")
        self.rect = self.image.get_rect(topleft=(x,y))
        self.direction = direction
        self.yspeed = -15
        self.xspeed = 4
        group.add(self)
        
    def update(self):
        self.yspeed += 1
        self.rect.x += self.xspeed * self.direction
        
        if self.rect.bottom + self.yspeed >= 300:
            self.yspeed = 0
            self.xspeed = 0
        
        self.rect.y += self.yspeed
        
    
        