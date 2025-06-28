import pygame
from settings import ASSET_PATH

class Enemy:
    def __init__(self):
        self.image = pygame.image.load(ASSET_PATH + "shadow.png")
        self.rect = self.image.get_rect(center=(400, 100))
        self.speed = 2
        self.active = False

    def activate(self, player_pos):
        self.active = True
        self.rect.center = (player_pos[0], 0)  # Spawn above the player

    def update(self, player_rect):
        if not self.active:
            return

        # Move toward player on both X and Y axes
        if self.rect.x < player_rect.x:
            self.rect.x += self.speed
        elif self.rect.x > player_rect.x:
            self.rect.x -= self.speed

        if self.rect.y < player_rect.y:
            self.rect.y += self.speed
        elif self.rect.y > player_rect.y:
            self.rect.y -= self.speed

    def draw(self, screen):
        if self.active:
            screen.blit(self.image, self.rect)
