from pygame.sprite import Sprite
import pygame


class Explosion(Sprite):
    def __init__(self, x,y, group):
        super().__init__()
        self.all_images = []
        for i in range(1,6):
            img = pygame.image.load(f"./assets/images/explosion/exp{i}.png")
            self.all_images.append(img)
            
        self.frame_index = 0
        self.image = self.all_images[self.frame_index]
        self.rect = self.image.get_rect(center = (x,y))
        group.add(self)
        self.last_image_change_time = pygame.time.get_ticks()
        
    def update(self):
        if pygame.time.get_ticks() - self.last_image_change_time >= 100:
            self.last_image_change_time = pygame.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= len(self.all_images):
                self.kill()
            else:
                self.image = self.all_images[self.frame_index]
        