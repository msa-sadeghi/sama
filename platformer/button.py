import pygame
class Button:
    def __init__(self, image, x,y):
        self.image = image
        self.rect = self.image.get_rect(center=(x,y))
        
    def draw(self, screen):
        click = False
        screen.blit(self.image, self.rect)
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                click = True
        return click
                