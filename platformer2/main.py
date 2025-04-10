from config import *
from character import Character
clock = pygame.time.Clock()
weapon_group = pygame.sprite.Group()
grenade_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()
moving_left = False
moving_right = False
jumped = False
shoot = False
grenade_shoot = False
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
            if event.key == pygame.K_SPACE:
                shoot = True
            if event.key == pygame.K_g:
                grenade_shoot = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_UP:
                jumped = False
            if event.key == pygame.K_SPACE:
                shoot = False
            if event.key == pygame.K_g:
                grenade_shoot = False
            
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
            
        if shoot:
            my_player.shoot("bullet",weapon_group)
            
        if grenade_shoot:
            my_player.shoot("grenade", grenade_group)
            
        
    screen.fill((0,0,0))
    weapon_group.update()
    weapon_group.draw(screen)
    grenade_group.update(explosion_group)
    grenade_group.draw(screen)
    explosion_group.update()
    explosion_group.draw(screen)
    my_player.draw(screen)        
    pygame.display.update()
    clock.tick(FPS)