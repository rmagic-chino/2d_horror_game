import pygame

def render_flashlight(screen, player_center):
    overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 0))  # Fully transparent
    pygame.draw.circle(overlay, (0, 0, 0, 180), player_center, 100)
    screen.blit(overlay, (0, 0))
