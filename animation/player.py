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

    def draw(self, screen):
        screen.blit(self.image, self.rect)



