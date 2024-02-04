from constants import *
from player import Player


my_player = Player()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    screen.fill((0,0,0))
    my_player.draw()
    my_player.move()
    pygame.display.update()
    clock.tick(FPS)
            