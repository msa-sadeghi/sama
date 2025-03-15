import pygame
from player import Player
from world import map
tile_image = pygame.image.load("./images/icons/tile.png")
def create_world():
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 1:
                screen.blit(tile_image, (j * 32 , i *32))

pygame.init()
width = 1024
height = 640
clock = pygame.time.Clock()
fps = 60
screen = pygame.display.set_mode((width, height))

my_player = Player(100, 300)

running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("lightgreen")
    create_world()
    my_player.draw(screen)
    my_player.move()
    pygame.display.update()
    clock.tick(fps)