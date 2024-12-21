from config import *

clock = pygame.time.Clock()

running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.update()
    clock.tick(FPS)