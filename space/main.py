from constants import *
from player import Player
from chick import Chick
pygame.init()
my_player = Player()
chick_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
egg_group = pygame.sprite.Group()

def spawn_chicks():
    for i in range(4):
        for j in range(8):
            Chick(j * 96, i * 96, chick_group)
spawn_chicks()

fire_sound = pygame.mixer.Sound("assets/fire.wav")
fire_sound.set_volume(0.5)



def game_over():
    global running,level
    screen.fill((0,0,0))
    draw_text("Game Over, Press Enter to play again", f,(255,0,255), 300, 400)
    pygame.display.update()
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
                    running = False 
                if event.key == pygame.K_RETURN:
                    my_player.lives = 3
                    my_player.score = 0
                    paused = False
                    level = 1
                    chick_group.empty()
                    spawn_chicks()
            



def check_sprites_collisions():
    if pygame.sprite.groupcollide(bullet_group, chick_group, True, True):
        fire_sound.play()
        my_player.score += 1
        
    if pygame.sprite.spritecollide(my_player, egg_group, True):
        my_player.lives -= 1
        if my_player.lives <= 0:
            my_player.lives = 0
            game_over()
    
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
            

f = pygame.font.SysFont("arial", 32)
def draw_text(text, f, color, x,y):
    t = f.render(text, True, color)
    screen.blit(t, (x,y))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                my_player.fire(bullet_group)
    check_edge_collisions()
    check_sprites_collisions()
    screen.fill((0,0,0))
    draw_text(f"score {my_player.score}", f, (255, 0, 255), 100,SCREEN_HEIGHT - 100)
    draw_text(f"lives {my_player.lives}", f, (255, 120, 255), SCREEN_WIDTH - 200,SCREEN_HEIGHT - 100)
    chick_group.update(egg_group)
    chick_group.draw(screen)
    bullet_group.update()
    bullet_group.draw(screen)
    egg_group.update()
    egg_group.draw(screen)
    my_player.draw()
    my_player.move()
    pygame.display.update()
    clock.tick(FPS)
            