import pygame
import random
from settings import ASSET_PATH
from sounds import play_whisper, play_scream

shadow_img = pygame.image.load(ASSET_PATH + "shadow.png").convert_alpha()
jumpscare_img = pygame.image.load(ASSET_PATH + "jumpscare.png").convert()
current_event = None
jumpscare_triggered = False

def maybe_trigger_event():
    global current_event
    roll = random.randint(1, 4)
    if roll == 1:
        current_event = "whisper"
    elif roll == 2:
        current_event = "shadow"
    else:
        current_event = None

def handle_events(screen, player, enemy):
    global jumpscare_triggered

    if current_event == "whisper":
        play_whisper()

    if current_event == "shadow":
        if on_screen(enemy):
            play_whisper()

        if enemy.rect.colliderect(player.rect):
            jumpscare_triggered = True
            screen.blit(jumpscare_img, (0, 0))
            pygame.display.update()
            pygame.time.delay(2000)
            player.health = 0

        elif enemy.rect.colliderect(player.rect.inflate(20, 20)):
            distance = abs(enemy.rect.centerx - player.rect.centerx) + abs(enemy.rect.centery - player.rect.centery)
            if distance <= 10:
                play_scream()

def on_screen(enemy):
    return 0 <= enemy.rect.x <= 800 and 0 <= enemy.rect.y <= 600
