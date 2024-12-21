from pygame.sprite import Sprite

class Character(Sprite):
    def __init__(self, type_ ,x,y, ammo, grenades):
        super().__init__()
        self.alive  = True
        self.health = 100
        self.max_health = 100
        self.type = type_
        self.ammo = ammo
        self.grenades = grenades


import os
print(len(os.listdir("assets/images/player/Death")))
        

        
        