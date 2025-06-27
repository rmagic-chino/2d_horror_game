import pygame
from enemy import Enemy
from settings import ASSET_PATH

class ShadowEnemy(Enemy):
    def __init__(self):
        image = pygame.image.load(ASSET_PATH + "shadow.png")
        super().__init__(image, -100, 500)
        
    