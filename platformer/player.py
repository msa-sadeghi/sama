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
        self.image_update_time = pygame.time.get_ticks()
    def update(self, tiles)    :
        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            dx -= 5
        if keys[pygame.K_RIGHT]:
            dx += 5
        dy += self.yVel
        self.yVel += 1
        for t in tiles:
            if t[1].colliderect(self.rect.x, self.rect.y + dy, self.rect.size[0], self.rect.size[1]):
                self.yVel = 0
                dy = t[1].top - self.rect.bottom
            if t[1].colliderect(self.rect.x + dx, self.rect.y, self.rect.size[0], self.rect.size[1]):
                dx = 0    
        self.rect.x += dx
        self.rect.y += dy
        self.animation()
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def animation(self):
        if pygame.time.get_ticks() - self.image_update_time > 100:
            self.image_number += 1
            self.image_update_time = pygame.time.get_ticks()
        if self.image_number >= len(self.right_images):
            self.image_number = 0
        self.image = self.right_images[self.image_number]
        
        
        