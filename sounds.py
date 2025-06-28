import pygame
from settings import ASSET_PATH

whisper_sound = None
scream_sound = None

def init_sounds():
    global whisper_sound, scream_sound
    pygame.mixer.init()  #  ensure sound system is ready
    whisper_sound = pygame.mixer.Sound(ASSET_PATH + "whisper.wav")
    scream_sound = pygame.mixer.Sound(ASSET_PATH + "scream.wav")

    #  Optional: adjust volume if sounds are too quiet
    whisper_sound.set_volume(1.0)  # max volume
    scream_sound.set_volume(1.0)

def play_whisper():
    if whisper_sound:
        whisper_sound.play()

def play_scream():
    if scream_sound:
        scream_sound.play()
