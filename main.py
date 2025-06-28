import pygame
import sys
from settings import *
from player import Player
from room_manager import RoomManager
from sounds import init_sounds
from events import draw_event
from flashlight import render_flashlight

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Don't Open the Door")
clock = pygame.time.Clock()

player = Player()
room_manager = RoomManager()
init_sounds()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.handle_input(keys)

    room_manager.update(player)

    # Render
    screen.blit(room_manager.get_current_room(), (0, 0))
    screen.blit(player.image, player.rect.topleft)
    render_flashlight(screen, player.rect.center)
    draw_event(screen)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
