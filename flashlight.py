import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

def render_flashlight(screen, player_rect):
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    overlay.fill((0, 0, 0))
    radius = 120
    pygame.draw.circle(overlay, (255, 255, 255), player_rect.center, radius)
    overlay.set_colorkey((255, 255, 255))
    overlay.set.alpha(230)
    screen.blit(overlay, (0, 0))
    