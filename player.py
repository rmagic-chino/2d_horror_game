import pygame
from settings import ASSET_PATH, SCREEN_WIDTH, SCREEN_HEIGHT

class Player:
    def __init__(self):
        self.image = pygame.image.load(ASSET_PATH + "player.png")
        self.rect = self.image.get_rect(midbottom=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))
        self.speed = 5