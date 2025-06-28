import pygame
from enemy import Enemy
from settings import ASSET_PATH
from sounds import play_scream

class ShadowEnemy(Enemy):
    def __init__(self):
        image = pygame.image.load(ASSET_PATH + "shadow.png").convert_alpha()
        super().__init__(image, -100, -100)
        self.active = False

    def update(self, player):
        if not self.active:
            self.rect.topleft = (player.rect.x - 200, player.rect.y)
            self.active = True

        speed = 2
        if self.rect.x < player.rect.x:
            self.rect.x += speed
        if self.rect.x > player.rect.x:
            self.rect.x -= speed
        if self.rect.y < player.rect.y:
            self.rect.y += speed
        if self.rect.y > player.rect.y:
            self.rect.y -= speed

        if self.distance_to(player) < 10:
            play_scream()

    def distance_to(self, player):
        dx = self.rect.centerx - player.rect.centerx
        dy = self.rect.centery - player.rect.centery
        return (dx**2 + dy**2) ** 0.5
