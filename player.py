import pygame
from settings import ASSET_PATH, SCREEN_WIDTH, SCREEN_HEIGHT

class Player:
    def __init__(self):
        self.image = pygame.image.load(ASSET_PATH + "player.png")
        self.rect = self.image.get_rect(midbottom=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))
        self.speed = 5
        
    def handle_input(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x = max(0, self.rect.x - self.speed)
        if keys[pygame.K_RIGHT]:
            self.rect.x = min(SCREEN_WIDTH - self.rect.width, self.rect.x + self.speed)