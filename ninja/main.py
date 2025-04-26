import pygame
from ninja import Ninja
pygame.init()
WIDTH = 1000
HEIGTH = 600

bg_image = pygame.image.load("freegui/png/BG.png")
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGTH))
bg_image_rect = bg_image.get_rect()

screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("Ninja Game")

my_ninja = Ninja(100, 100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    screen.blit(bg_image, bg_image_rect)
    my_ninja.draw(screen)
    my_ninja.move_horizontal()
    pygame.display.update()
pygame.quit()