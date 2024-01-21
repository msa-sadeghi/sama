import random
import pygame

pygame.init()


def game_over():
    pygame.mixer.music.stop()
    global running, lives, score
    game_over_text = font.render("Game Over, Press Enter to continue", True, (178, 10, 189))
    game_over_rect = game_over_text.get_rect()
    game_over_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    SCREEN.fill((0, 0, 0))
    SCREEN.blit(game_over_text, game_over_rect)
    pygame.display.update()
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                paused = False
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    paused = False
                    pygame.mixer.music.play()
                    score = 0
                    lives = 3


pygame.mixer.music.load("assets/bg.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

pick_sound = pygame.mixer.Sound("assets/p.wav")

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
FPS = 60
c = pygame.time.Clock()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

wolf_image = pygame.image.load("assets/w.png")
wolf_rect = wolf_image.get_rect()
wolf_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

sheep_image = pygame.image.load("assets/m.png")
sheep_rect = sheep_image.get_rect()
sheep_rect.bottom = SCREEN_HEIGHT
sheep_rect.centerx = SCREEN_WIDTH / 2

bomb_image = pygame.image.load("assets/bomp.png")
bomb_rect = bomb_image.get_rect()
bomb_rect.bottom = SCREEN_HEIGHT
bomb_rect.centerx = SCREEN_WIDTH / 2

font = pygame.font.Font("assets/f.otf", 48)
score = 0
score_text = font.render(f"Score:{score}", True, (255, 0, 255))
score_rect = score_text.get_rect()
score_rect.top = 0
score_rect.centerx = random.randint(0, SCREEN_WIDTH)

lives = 3
lives_text = font.render(f"Lives: {lives}", True, (255, 0, 0))
lives_rect = lives_text.get_rect()
lives_rect.top = 0
lives_rect.left = 0

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

    sheep_rect.y -= 5
    if sheep_rect.bottom <= 0:
        sheep_rect.bottom = SCREEN_HEIGHT
        sheep_rect.centerx = random.randint(48, SCREEN_WIDTH - 48)
    if wolf_rect.colliderect(sheep_rect):
        pick_sound.play()
        score += 1
        sheep_rect.bottom = SCREEN_HEIGHT
        sheep_rect.centerx = random.randint(48, SCREEN_WIDTH - 48)

    bomb_rect.y -= 5
    if bomb_rect.bottom < 0:
        bomb_rect.bottom = SCREEN_HEIGHT
        bomb_rect.centerx = random.randint(0, SCREEN_WIDTH)

    if wolf_rect.colliderect(bomb_rect):
        lives -= 1
        bomb_rect.bottom = SCREEN_HEIGHT
        bomb_rect.centerx = random.randint(0, SCREEN_WIDTH)

        if lives <= 0:
            game_over()

    lives_text = font.render(f"Lives: {lives}", True, (255, 0, 0))
    score_text = font.render(f"Score:{score}", True, (255, 0, 255))
    SCREEN.fill((171, 80, 255))
    SCREEN.blit(wolf_image, wolf_rect)
    SCREEN.blit(sheep_image, sheep_rect)
    SCREEN.blit(score_text, score_rect)
    SCREEN.blit(bomb_image, bomb_rect)
    SCREEN.blit(lives_text, lives_rect)
    pygame.display.update()
    c.tick(FPS)

    pygame.display.update()
