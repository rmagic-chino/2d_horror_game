import pygame
import random
from settings import ASSET_PATH
from sounds import play_whisper

shadow = pygame.image.load(ASSET_PATH + "shadow.png")
jumpscare_img = pygame.image.load(ASSET_PATH + "jumpscare.png")
current_event = None

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

def draw_event(screen):
    if current_event == "jumpscare":
        screen.blit(jumpscare_img, (0, 0))
        pygame.display.update()
        pygame.time.delay(1500)
