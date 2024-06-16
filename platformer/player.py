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
        self.moving_status = False
        self.direction = 1
        self.in_air = False
        self.alive = True
        self.ghost_image = pygame.image.load("assets/ghost.png")
    
    def ghost_move(self):
        if self.rect.y > 100:
            self.rect.y -= 3
    
    def update(self, tiles, enemy_group)    :
        if pygame.sprite.spritecollide(self, enemy_group, True):
            self.alive = False
        
        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction = -1
            self.moving_status = True
            dx -= 5
        if keys[pygame.K_RIGHT]:
            self.direction = 1
            self.moving_status = True
            dx += 5
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.moving_status = False
        if keys[pygame.K_SPACE]  and not self.in_air  :
            self.yVel = -15
            self.in_air = True
        dy += self.yVel
        self.yVel += 1
        for t in tiles:
            if t[1].colliderect(self.rect.x, self.rect.y + dy, self.rect.size[0], self.rect.size[1]):
                if self.yVel > 0:
                    self.yVel = 0
                    dy = t[1].top - self.rect.bottom
                    self.in_air = False
                else:
                    self.yVel = 0
                    dy = t[1].bottom - self.rect.top
            if t[1].colliderect(self.rect.x + dx, self.rect.y, self.rect.size[0], self.rect.size[1]):
                dx = 0    
        self.rect.x += dx
        self.rect.y += dy
        self.animation()
    def draw(self, screen):
        if self.alive == False:
            self.image = self.ghost_image
        screen.blit(self.image, self.rect)

    def animation(self):
        if pygame.time.get_ticks() - self.image_update_time > 100 and self.moving_status:
            self.image_number += 1
            self.image_update_time = pygame.time.get_ticks()
        if not self.moving_status:
            self.image_number = 0
        if self.image_number >= len(self.right_images):
            self.image_number = 0
        if self.direction == 1:
            self.image = self.right_images[self.image_number]
        elif self.direction == -1:
            self.image = self.left_images[self.image_number]
        
        
        