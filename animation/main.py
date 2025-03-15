import pygame
from player import Player
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
    my_player.draw(screen)
    my_player.move()
    pygame.display.update()
    clock.tick(fps)