import pygame
from settings import ASSET_PATH

whisper_sound = None
scream_sound = None
jumpscare_scream = None  # NEW

def init_sounds():
    global whisper_sound, scream_sound, jumpscare_scream
    pygame.mixer.init()
    whisper_sound = pygame.mixer.Sound(ASSET_PATH + "whisper.wav")
    scream_sound = pygame.mixer.Sound(ASSET_PATH + "scream.wav")
    jumpscare_scream = pygame.mixer.Sound(ASSET_PATH + "jumpscare_scream.wav")  # NEW

def play_whisper():
    if whisper_sound:
        whisper_sound.play()

def play_scream():
    if scream_sound:
        scream_sound.play()

def play_jumpscare_scream():
    if jumpscare_scream:
        jumpscare_scream.play()
