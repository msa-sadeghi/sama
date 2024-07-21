from pygame.sprite import Sprite
import pygame

class Castle(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.image_100 = pygame.image.load("assets/castle/castle_100.png")
        self.image_100 = pygame.transform.scale(self.image_100, (200, 200))
        
        self.image_50 = pygame.image.load("assets/castle/castle_50.png")
        self.image_50 = pygame.transform.scale(self.image_50, (200, 200))
        
        self.image_25 = pygame.image.load("assets/castle/castle_25.png")
        self.image_25 = pygame.transform.scale(self.image_25, (200, 200))
        
        self.image = self.image_100
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)