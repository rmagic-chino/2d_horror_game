import pygame

def render_flashlight(screen, player_center):
    overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 0))  # Fully transparent background

    radius = 100
    pygame.draw.circle(overlay, (0, 0, 0, 180), player_center, radius)

    screen.blit(overlay, (0, 0))
