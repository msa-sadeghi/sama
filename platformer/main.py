import pygame
from constants import *
from world import World

from player import Player
from button import Button
import pickle
restart_image = pygame.image.load("assets/restart_btn.png")
restart_button = Button(restart_image, screen_width/2, screen_height/2)
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
level_number = 1

with open("level1", "rb") as file:
    world_data = pickle.load(file)

def change_level():
    player.next_level = False
    global level_number
    level_number += 1
    with open(f"level{level_number}", "rb")  as file:
        world_data = pickle.load(file)
        enemy_group.empty()
        door_group.empty()
        player.__init__(100, 300)
        world = World(world_data, enemy_group, door_group)
        return world
        


max_level = 2
game_font48 = pygame.font.Font("assets/AttackGraffiti.ttf", 48)
clock = pygame.time.Clock()
player = Player(100,screen_height-300)
enemy_group = pygame.sprite.Group()
door_group = pygame.sprite.Group()
world = World(world_data, enemy_group, door_group)
bg_img = pygame.image.load("assets/sky.png")
sun_img = pygame.image.load("assets/sun.png")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(bg_img, (0,0))
    world.draw(screen) 
            
    player.draw(screen)
    if player.alive == True:
        player.update(world.tile_list, enemy_group, door_group)
    else:
        player.ghost_move()
        if restart_button.draw(screen):
            player.__init__(100,screen_height-300)
            enemy_group.empty()
            world = World(world_data, enemy_group)
    if player.next_level:
        world = change_level()   
    enemy_group.update()
    enemy_group.draw(screen)

    door_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)

