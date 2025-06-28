import pygame
import sys
from settings import *
from player import Player
from room_manager import RoomManager
from sounds import init_sounds
from events import init_events, update_events, render_events
from flashlight import render_flashlight

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Don't Open the Door")
clock = pygame.time.Clock()

player = Player()
room_manager = RoomManager()
init_sounds()
init_events()

font = pygame.font.SysFont(None, 64)
heart_img = pygame.image.load(ASSET_PATH + "heart.png")

game_state = {
    "running": True,
    "hearts": 3,
    "jumpscare_active": False,
    "jumpscare_timer": 0,
    "whisper_triggered": False
}

while game_state["running"]:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state["running"] = False

    keys = pygame.key.get_pressed()
    player.handle_input(keys)
    room_manager.update(player)
    update_events(player, game_state)

    screen.blit(room_manager.get_current_room(), (0, 0))
    screen.blit(player.image, player.rect.topleft)

    # Health bar
    for i in range(game_state["hearts"]):
        screen.blit(heart_img, (10 + i * 40, 10))

    # Room number
    room_text = font.render(f"Room: {room_manager.rooms_passed}", True, (255, 255, 255))
    screen.blit(room_text, (SCREEN_WIDTH//2 - room_text.get_width()//2, 10))

    render_flashlight(screen, player.rect.center)
    render_events(screen, game_state)

    if game_state["hearts"] <= 0:
        text = font.render("YOU DIED", True, (255, 0, 0))
        screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, SCREEN_HEIGHT//2))

    elif room_manager.rooms_passed >= 20:
        text = font.render("YOU ESCAPED", True, (0, 255, 0))
        screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, SCREEN_HEIGHT//2))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
