import pygame
from enemy import Enemy
from settings import ASSET_PATH

class ShadowEnemy(Enemy):
    def __init__(self):
        self.image = pygame.image.load(ASSET_PATH + "shadow.png").convert_alpha()
        super().__init__(self.image, -100, 500)
        
    def update(self, player):
        if self.rect.x < player.rect.x:
            self.rect.x += 1
        elif self.rect.x > player.rect.x:
            self.rect.x -= 1
            