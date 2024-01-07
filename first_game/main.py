import pygame

pygame.init()


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
FPS = 60
c = pygame.time.Clock()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

wolf_image = pygame.image.load("assets/w.png")
wolf_rect = wolf_image.get_rect()
wolf_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        wolf_rect.y -= 5
    if keys[pygame.K_DOWN]:
        wolf_rect.y += 5
    
    if keys[pygame.K_LEFT]:
        wolf_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        wolf_rect.x += 5 
    SCREEN.fill((171, 80, 255))
    SCREEN.blit(wolf_image, wolf_rect)
    pygame.display.update()
    c.tick(FPS)



    