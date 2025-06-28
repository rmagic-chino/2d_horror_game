import pygame
import sys
from settings import *
from player import Player
from shadow_enemy import ShadowEnemy
from room_manager import RoomManager
from ui import draw_hearts, draw_end_message
from sounds import init_sounds
from events import handle_events

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Don't Open the Door")
clock = pygame.time.Clock()

def game_loop():
    player = Player()
    enemy = ShadowEnemy()
    room_manager = RoomManager()
    init_sounds()

    running = True
    game_over = False
    escaped = False

    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if not game_over and not escaped:
            keys = pygame.key.get_pressed()
            player.handle_input(keys)
            enemy.update(player)

            result = room_manager.update(player)
            if result == "end":
                escaped = True

            screen.blit(room_manager.get_current_room(), (0, 0))
            screen.blit(player.image, player.rect)
            screen.blit(enemy.image, enemy.rect)

            handle_events(screen, player, enemy)
            draw_hearts(screen, player.health)

            if player.health <= 0:
                game_over = True

        elif game_over:
            draw_end_message(screen, "You Died")
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                return game_loop()
            elif keys[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()

        elif escaped:
            draw_end_message(screen, "You Escaped!")
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                return game_loop()
            elif keys[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(FPS)

game_loop()
