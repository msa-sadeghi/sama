from pygame.sprite import Sprite
import pygame

class Grenade(Sprite):
    def __init__(self, x,y, group):
        super().__init__()
        