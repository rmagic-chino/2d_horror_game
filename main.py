import pygame
import sys
from settings import *
from player import Player
from room_manager import RoomManager
from flashlight import render_flashlight
from sounds import init_sounds
from events import handle_events, load_event_assets
from shadow_enemy import ShadowEnemy

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Don't Open the Door")
clock = pygame.time.Clock()

load_event_assets()
init_sounds()

player = Player()
room_manager = RoomManager()
enemy = ShadowEnemy()

font = pygame.font.SysFont(None, 48)
game_over = False
escaped = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not game_over and not escaped:
        keys = pygame.key.get_pressed()
        player.handle_input(keys)
        room_manager.update(player)
        enemy.update(player)

        if player.health <= 0:
            game_over = True

        if room_manager.rooms_passed >= 20:
            escaped = True

        screen.blit(room_manager.get_current_room(), (0, 0))
        screen.blit(player.image, player.rect.topleft)
        screen.blit(enemy.image, enemy.rect.topleft)
        render_flashlight(screen, player.rect.center)
        handle_events(screen, player, enemy)

        # Draw health
        for i in range(player.health):
            heart = pygame.image.load(ASSET_PATH + "heart.png")
            screen.blit(heart, (10 + i * 40, 10))

    else:
        if game_over:
            text = font.render("You Died", True, (255, 0, 0))
        elif escaped:
            text = font.render("You Escaped!", True, (0, 255, 0))
        screen.fill((0, 0, 0))
        screen.blit(text, text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))

        # Buttons
        retry_btn = font.render("Try Again", True, (255, 255, 255))
        exit_btn = font.render("Exit", True, (255, 255, 255))
        screen.blit(retry_btn, (SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 + 50))
        screen.blit(exit_btn, (SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 + 100))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if click[0]:
            if SCREEN_WIDTH//2 - 100 <= mouse[0] <= SCREEN_WIDTH//2 + 100:
                if SCREEN_HEIGHT//2 + 50 <= mouse[1] <= SCREEN_HEIGHT//2 + 80:
                    player = Player()
                    room_manager = RoomManager()
                    enemy = ShadowEnemy()
                    game_over = False
                    escaped = False
                elif SCREEN_HEIGHT//2 + 100 <= mouse[1] <= SCREEN_HEIGHT//2 + 130:
                    pygame.quit()
                    sys.exit()

    pygame.display.update()
    clock.tick(FPS)
