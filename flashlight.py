import pygame

def render_flashlight(screen, player_center):
    overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)

    # No dimming of background — fully transparent fill
    overlay.fill((0, 0, 0, 0))

    # Draw circular light beam (semi-transparent)
    radius = 100
    pygame.draw.circle(overlay, (0, 0, 0, 180), player_center, radius)

    screen.blit(overlay, (0, 0))
