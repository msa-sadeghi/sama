from pygame.sprite import Sprite
import pygame
from constants import *
class Player(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.right_images = []
        self.left_images = []
        for i in range(1,5):
            img = pygame.image.load(f"assets/guy{i}.png")
            self.right_images.append(img)
            img = pygame.transform.flip(img, True, False)
            self.left_images.append(img)
        self.image_number = 0
        self.image = self.right_images[self.image_number]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.yVel = 0
    def update(self, tiles)    :
        dx = 0
        dy = 0
        dy += self.yVel
        self.yVel += 1
        
        for t in tiles:
            if t[1].colliderect(self.rect.x, self.rect.y + dy, self.rect.size[0], self.rect.size[1]):
                self.yVel = 0
                dy = t[1].top - self.rect.bottom
        
        
        self.rect.x += dx
        self.rect.y += dy
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    
        