from pygame.sprite import Sprite
import pygame
import os
class Ninja(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.all_animations = os.listdir("./ninjagirlnew/png")
        self.all_images = {}
        for animation in self.all_animations:
            images = []
            for image in os.listdir(f"./ninjagirlnew/png/{animation}"):
                images.append(
                    pygame.transform.scale_by(
                    pygame.image.load(f"./ninjagirlnew/png/{animation}/{image}"),0.5

                    )
                    )

            self.all_images[animation] = images

        self.frame_index = 0
        self.animation = "Idle"
        self.image = self.all_images[self.animation][self.frame_index]
        self.rect  = self.image.get_rect(topleft= (x,y))
        self.last_update_time = pygame.time.get_ticks()
        self.direction = 1
        self.idle = True
        self.slide = False
        self.y_speed = 0
        self.in_air = False

    def next_costume(self):
        self.image = self.all_images[self.animation][self.frame_index]
        if pygame.time.get_ticks() - self.last_update_time > 100:
            self.last_update_time = pygame.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= len(self.all_images[self.animation]):
                self.frame_index = 0

    def draw(self, screen):
        self.next_costume()
        screen.blit(
            pygame.transform.flip(self.image, self.direction == -1, False)
            , self.rect)
    def change_animation(self, new_animation):
        if new_animation != self.animation:
            self.animation = new_animation
            self.frame_index = 0
    def move_horizontal(self):
        dx = 0
      
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.idle = False
            self.direction = -1
            dx -= 5
        
        if keys[pygame.K_RIGHT]:
            self.idle = False
            self.direction = 1
            dx += 5
       
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.idle = True

        if keys[pygame.K_DOWN] and self.idle == False:
            self.slide = True
        else:
            self.slide = False

        self.rect.x += dx
    

    def move_vertical(self):
        dy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y_speed = -15
            self.in_air = True

        dy += self.y_speed
        self.y_speed += 1

        if self.rect.bottom + dy > 500:
            self.y_speed = 0
            dy = 500 - self.rect.bottom
            self.in_air = False

        self.rect.y += dy

