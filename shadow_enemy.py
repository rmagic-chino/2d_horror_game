import pygame
from enemy import Enemy
from settings import ASSET_PATH

class ShadowEnemy(Enemy):
    def __init__(self):
        try:
            image = pygame.image.load(ASSET_PATH + "shadow.png").convert_alpha()
        except pygame.error:
            image = pygame.Surface((40, 60))
            image.fill((0, 0, 0))
        super().__init__(image, -100, 300)

    def update(self, player):
        speed = 2
        if self.rect.x < player.rect.x:
            self.rect.x += speed
        elif self.rect.x > player.rect.x:
            self.rect.x -= speed

        if self.rect.y < player.rect.y:
            self.rect.y += speed
        elif self.rect.y > player.rect.y:
            self.rect.y -= speed
