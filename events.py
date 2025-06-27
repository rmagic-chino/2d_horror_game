import pygame
import random
from settings import ASSET_PATH, ENEMY_TRIGGER_DISTANCE
from sounds import play_whisper, play_scream
from shadow_enemy import ShadowEnemy

jumpscare_img = pygame.image.load(ASSET_PATH + 'jumpscare.png')
current_event = None
enemy = None

