import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

def render_flashlight(screen, player_center):
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    overlay.fill((0, 0, 0))
    
    radius = 100
    pygame.draw.circle(overlay, (255, 255, 255), player_center, radius)
    
    screen.blit(overlay, (0, 0))
    