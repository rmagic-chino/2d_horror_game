import pygame

def render_flashlight(screen, center):
    overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))  # slightly dim the background

    radius = 80  # smaller radius
    pygame.draw.circle(overlay, (0, 0, 0, 0), center, radius)

    screen.blit(overlay, (0, 0))
