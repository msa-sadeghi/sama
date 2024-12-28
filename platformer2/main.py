from config import *
from character import Character
clock = pygame.time.Clock()


my_player = Character("player", 100, 300, 100, 10)
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    my_player.draw(screen)        
    pygame.display.update()
    clock.tick(FPS)