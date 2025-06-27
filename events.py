import pygame
import random
from settings import ASSET_PATH, ENEMY_TRIGGER_DISTANCE
from sounds import play_whisper, play_scream
from shadow_enemy import ShadowEnemy

jumpscare_img = None
jumpscare_timer = 0
current_event = None
enemy = None

def get_jumpscare_image():
    global jumpscare_img
    if jumpscare_img is None:
        jumpscare_img = pygame.image.load(ASSET_PATH + 'jumpscare.png').convert_alpha()
    return jumpscare_img

def maybe_trigger_event():
    global current_event, enemy, jumpscare_timer
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
        jumpscare_timer = 20
    else:
        current_event = None
        # keep previous enemy if it exists (don't reset)

def handle_events(screen, player):
    global enemy, current_event, jumpscare_timer

    if current_event == "enemy" and enemy:
        enemy.update(player)
        screen.blit(enemy.image, enemy.rect.topleft)
        if abs(player.rect.x - enemy.rect.x) < ENEMY_TRIGGER_DISTANCE:
            flicker_screen(screen, intensity=60)
            play_scream()
            # Don't destroy enemy — let it follow continuously

    elif current_event == "whisper":
        phantom = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        phantom.fill((0, 0, 0, 50))
        screen.blit(phantom, (0, 0))
        current_event = None

    elif current_event == "scream" and jumpscare_timer > 0:
        image = get_jumpscare_image()
        rect = image.get_rect(center=screen.get_rect().center)
        screen.blit(image, rect)
        jumpscare_timer -= 1
        if jumpscare_timer <= 0:
            current_event = None

def flicker_screen(screen, intensity=40):
    flicker = pygame.Surface(screen.get_size())
    flicker.fill((255, 255, 255))
    flicker.set_alpha(intensity)
    screen.blit(flicker, (0, 0))
