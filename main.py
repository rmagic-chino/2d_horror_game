import pygame
import sys
import random
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
jumpscare_img = pygame.image.load(ASSET_PATH + "jumpscare.png")

game_state = {
    "running": True,
    "hearts": 3,
    "jumpscare_active": False,
    "jumpscare_timer": 0
}

def draw_end_screen(message, color):
    screen.fill((0, 0, 0))
    msg = font.render(message, True, color)
    screen.blit(msg, (SCREEN_WIDTH//2 - msg.get_width()//2, SCREEN_HEIGHT//2 - 60))

    try_again = font.render("Press R to Retry or Q to Quit", True, (255, 255, 255))
    screen.blit(try_again, (SCREEN_WIDTH//2 - try_again.get_width()//2, SCREEN_HEIGHT//2 + 10))
    pygame.display.update()

def reset_game():
    player.rect.midbottom = (SCREEN_WIDTH//2, SCREEN_HEIGHT - 50)
    room_manager.rooms_passed = 0
    room_manager.exit_side = random.choice(['left', 'right', 'up', 'down'])
    game_state["hearts"] = 3
    game_state["jumpscare_active"] = False

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

    # Draw health
    for i in range(game_state["hearts"]):
        screen.blit(heart_img, (10 + i * 40, 10))

    render_flashlight(screen, player.rect.center)
    render_events(screen, game_state)

    pygame.display.update()
    clock.tick(FPS)

    if game_state["hearts"] <= 0:
        pygame.time.wait(1500)
        draw_end_screen("YOU DIED", (255, 0, 0))
    elif room_manager.rooms_passed >= 20:
        pygame.time.wait(1500)
        draw_end_screen("YOU ESCAPED", (0, 255, 0))

    if game_state["hearts"] <= 0 or room_manager.rooms_passed >= 20:
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_state["running"] = False
                    waiting = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_state["running"] = False
                        waiting = False
                    elif event.key == pygame.K_r:
                        reset_game()
                        waiting = False

pygame.quit()
sys.exit()
