import pygame
import random
from settings import ASSET_PATH, ENEMY_TRIGGER_DISTANCE
from sounds import play_whisper, play_scream
from shadow_enemy import ShadowEnemy

jumpscare_img = pygame.image.load(ASSET_PATH + 'jumpscare.png')
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
    global enemy
    if current_event == "enemy" and enemy:
        enemy.update(player)
        screen.blit(enemy.image, enemy.rect.topleft)
        if abs(player.rect.x - enemy.rect.x) < ENEMY_TRIGGER_DISTANCE:
            flicker_screen(screen)
            
    