import pygame
from castle import Castle
from enemy import Enemy
screen = pygame.display.set_mode()
clock = pygame.time.Clock()

screen_w  = screen.get_width()
screen_h = screen.get_height()
enemy_group = pygame.sprite.Group()
enemy1 = Enemy("goblin", 100, screen_h - 400, enemy_group, 1, 150)

bg = pygame.image.load("assets/bg.png")
bg = pygame.transform.scale(bg, (screen_w, screen_h))

my_castle = Castle(screen_w - 300, screen_h - 400)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    screen.blit(bg, (0,0)) 
    my_castle.draw(screen) 
    enemy_group.update()          
    enemy_group.draw(screen)
    pygame.display.update()
    clock.tick(60)