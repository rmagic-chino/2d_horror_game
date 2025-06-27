import pygame
import sys
from settings import *
from player import Player
from room_manager import RoomManager
from flashlight import render_flashlight
from sounds import init_sounds
from events import handle_events
from save_manager import save_game, load_game

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("dont open the door")
clock = pygame.time.Clock()

player = Player()
room_manager = RoomManager()
init_sounds()

saved = load_game()
if saved:
    player.rect.x = saved['player_x']
    room_manager.rooms_passed = saved['rooms_passed']

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_game({
                "player_x": player.rect.x,
                "rooms_passed": room_manager.rooms_passed
            })
            running = False
    
    keys = pygame.key.get_pressed()
    player.handle_input(keys)
    room_manager.update(player)
    
    screen.blit(room_manager.get_current_room(), (0, 0))
    screen.blit(player.image, player.rect.topleft)
    
    handle_events(screen, player)
    render_flashlight(screen, player.rect.center)
    
    pygame.display.update()
    clock.tick(FPS)
    
pygame.quit()
sys.exit()
