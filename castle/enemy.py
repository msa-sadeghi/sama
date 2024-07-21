from pygame.sprite import Sprite
import pygame

class Enemy(Sprite):
    def __init__(self, type, x,y, group, speed, health):
        
        super().__init__()
        self.type = type
        self.animation_types = ("walk", "attack", "death")
        self.all_images = []
        
        for animation in self.animation_types:
            images = []
            for i in range(20):
                img = pygame.image.load(f"assets/enemies/{type}/{animation}/{i}.png")
                img_w = img.get_width()
                img_h = img.get_height()
                img = pygame.transform.scale(img, (img_w * 0.2, img_h * 0.2))
                images.append(img)
            self.all_images.append(images)
            
            
        self.image = self.all_images[0][0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.action = 0
        self.image_number = 0
        self.speed = speed
        self.health = health
        self.max_health = health
        self.alive = True
        group.add(self)
                
        
        