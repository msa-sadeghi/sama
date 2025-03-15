from pygame.sprite import Sprite
import pygame
import os
class Player(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.all_images = {}
        self.animation_types = ('Idle', 'Run')
        for animation in self.animation_types:
            temp = []
            num_of_images = len(os.listdir(f"./images/{animation}"))
            for i in range(1,num_of_images):
                img = pygame.image.load(f"./images/{animation}/{animation}{i}.png")
                img = pygame.transform.scale_by(img, 0.5)
                temp.append(img)

            self.all_images[animation] = temp

        self.frame_index = 0
        self.action = "Idle"
        self.image = self.all_images[self.action][self.frame_index]
        self.rect = self.image.get_rect(topleft=(x,y))
        self.animation_time = pygame.time.get_ticks()
        self.flip = False
        self.moving = False
        self.yspeed = 0

    def draw(self, screen):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
        self.animation()
        if self.moving == True:
            self.change_animation("Run")
        else:
            self.change_animation("Idle")

    def animation(self):
        self.image = self.all_images[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.animation_time >= 100:
            self.frame_index += 1
            if self.frame_index >= len(self.all_images[self.action]):
                self.frame_index = 0
            self.animation_time = pygame.time.get_ticks()

    def move(self):
        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.moving = True
            self.flip = True
            dx -= 5
        if keys[pygame.K_RIGHT]:
            self.moving = True
            self.flip = False
            dx += 5
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.moving = False
        if keys[pygame.K_UP]:
            self.yspeed =  -14
        self.yspeed += 1
        dy += self.yspeed
        
        if self.rect.bottom + dy >= 400:
            dy = 400 -self.rect.bottom
            self.yspeed = 0
        
        self.rect.x += dx
        self.rect.y += dy
    def change_animation(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0



