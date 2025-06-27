from typing import Any
import pygame
from settings import ASSET_PATH, SCREEN_WIDTH
from game_object import GameObject

class Player(GameObject):
    def __init__(self):
        image = pygame.image.load(ASSET_PATH + "player.png")
        super().__init__(image, 400, 550)
        self.speed = 5
        
    def handle_input(self, keys: Any):
        if keys[pygame.K_LEFT]:
            self.rect.x = max(0, self.rect.x - self.speed)
        if keys[pygame.K_RIGHT]:
            self.rect.x = min(SCREEN_WIDTH - self.rect.width, self.rect.x + self.speed)
            
