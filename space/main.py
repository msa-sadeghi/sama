from constants import *
from player import Player
from chick import Chick
my_player = Player()
chick_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
def spawn_chicks():
    for i in range(4):
        for j in range(8):
            Chick(j * 96, i * 96, chick_group)
spawn_chicks()

level = 1
def check_edge_collisions():
    on_edge = False
    for chick in chick_group:
        if chick.rect.left < 0 or chick.rect.right> SCREEN_WIDTH:
            on_edge = True
            break
    if on_edge:
        for chick in chick_group:
            chick.direction *= -1
            chick.rect.y += level * 10
            

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                my_player.fire(bullet_group)
    check_edge_collisions()
    screen.fill((0,0,0))
    chick_group.update()
    chick_group.draw(screen)
    bullet_group.update()
    bullet_group.draw(screen)
    my_player.draw()
    my_player.move()
    pygame.display.update()
    clock.tick(FPS)
            