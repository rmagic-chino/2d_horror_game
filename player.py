import pygame
from settings import ASSET_PATH, SCREEN_WIDTH, SCREEN_HEIGHT

class Player:
    def __init__(self):
        self.image = pygame.image.load(ASSET_PATH + "player.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))
        self.speed = 5
        self.health = 3

    def handle_input(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        self.rect.clamp_ip(pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))

    def reset_position(self, exit_direction):
        if exit_direction == 'left':
            self.rect.right = SCREEN_WIDTH - 10
        elif exit_direction == 'right':
            self.rect.left = 10
        elif exit_direction == 'up':
            self.rect.bottom = SCREEN_HEIGHT - 10
        elif exit_direction == 'down':
            self.rect.top = 10
