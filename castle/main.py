import pygame

screen = pygame.display.set_mode()
clock = pygame.time.Clock()

screen_w  = screen.get_width()
screen_h = screen.get_height()

bg = pygame.image.load("assets/bg.png")
bg = pygame.transform.scale(bg, (screen_w, screen_h))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    screen.blit(bg, (0,0))            
    pygame.display.update()
    clock.tick(60)