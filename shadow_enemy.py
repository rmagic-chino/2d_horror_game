import pygame
from enemy import Enemy
from settings import ASSET_PATH

class ShadowEnemy(Enemy):
    def __init__(self):
        try:
            self.image = pygame.image.load(ASSET_PATH + "shadow.png").convert_alpha()
        except pygame.error:
            print("Warning: Missing shadow.png, using placeholder.")
            self.image = pygame.Surface((50, 50))
            self.image.fill((0, 0, 0))
        super().__init__(self.image, -100, 500)

    def update(self, player):
        speed = 3  # Faster ghost
        if self.rect.x < player.rect.x:
            self.rect.x += speed
        elif self.rect.x > player.rect.x:
            self.rect.x -= speed
