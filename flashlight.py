import pygame

def render_flashlight(screen, player_center):
    overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 200))
    
    radius = 100
    pygame.draw.circle(overlay, (0, 0, 0, 0), player_center, radius)
    
    screen.blit(overlay, (0, 0))
    