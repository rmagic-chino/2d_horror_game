import pygame
import random
from settings import ASSET_PATH
from sounds import play_whisper, play_scream

shadow_img = None
jumpscare_img = None
current_event = None

def load_event_assets():
    global shadow_img, jumpscare_img
    shadow_img = pygame.image.load(ASSET_PATH + "shadow.png").convert_alpha()
    jumpscare_img = pygame.image.load(ASSET_PATH + "jumpscare.png").convert_alpha()

def maybe_trigger_event():
    global current_event
    roll = random.randint(1, 10)
    if roll == 1:
        play_whisper()
        current_event = "whisper"
    elif roll == 2:
        current_event = "shadow"
    elif roll == 3:
        current_event = "jumpscare"
    else:
        current_event = None

def handle_events(screen, player, enemy):
    global current_event
    if current_event == "jumpscare" and player.rect.colliderect(enemy.rect):
        play_scream()
        screen.blit(jumpscare_img, (0, 0))
        pygame.display.update()
        pygame.time.delay(1500)
        player.health -= 1
        current_event = None
    elif current_event == "shadow":
        if screen.get_rect().colliderect(enemy.rect):
            play_whisper()
