from config import *
from character import Character
clock = pygame.time.Clock()

moving_left = False
moving_right = False
jumped = False
my_player = Character("player", 100, 300, 100, 10)
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_UP:
                jumped = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_UP:
                jumped = False
            
    if my_player.alive:
        if moving_left or moving_right:
            my_player.change_animation("Run")
        else:
            my_player.change_animation("Idle")
        if jumped == True and my_player.on_ground:
            my_player.on_ground = False
            my_player.gravity = -13
        my_player.move(moving_left, moving_right)
        if not my_player.on_ground:
            my_player.change_animation("Jump")
            
        
    screen.fill((0,0,0))
    my_player.draw(screen)        
    pygame.display.update()
    clock.tick(FPS)