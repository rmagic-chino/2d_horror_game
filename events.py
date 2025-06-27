import pygame
import random
from settings import ASSET_PATH, ENEMY_TRIGGER_DISTANCE
from sounds import play_whisper, play_scream
from shadow_enemy import ShadowEnemy

# Lazy-load jumpscare image only when needed
jumpscare_img = None
def get_jumpscare_image():
    global jumpscare_img
    if jumpscare_img is None:
        jumpscare_img = pygame.image.load(ASSET_PATH + 'jumpscare.png').convert_alpha()
    return jumpscare_img

current_event = None
enemy = None

def maybe_trigger_event():
    global current_event, enemy
    roll = random.randint(1, 10)
    if roll == 1:
        play_whisper()
        current_event = "whisper"
    elif roll == 2:
        enemy = ShadowEnemy()
        current_event = "enemy"
    elif roll == 3:
        play_scream()
        current_event = "scream"
    else:
        current_event = None
        enemy = None

def handle_events(screen, player):
    global enemy, current_event
    if current_event == "enemy" and enemy:
        enemy.update(player)
        screen.blit(enemy.image, enemy.rect.topleft)
        if abs(player.rect.x - enemy.rect.x) < ENEMY_TRIGGER_DISTANCE:
            flicker_screen(screen)
            enemy = None  # Reset after scare
            current_event = None

def flicker_screen(screen):
    flicker = pygame.Surface(screen.get_size())
    flicker.fill((255, 255, 255))
    flicker.set_alpha(40)
    screen.blit(flicker, (0, 0))
