import pygame
import random
from settings import ASSET_PATH, SCREEN_HEIGHT
from sounds import play_whisper, play_scream, play_jumpscare_scream

shadow = pygame.image.load(ASSET_PATH + "shadow.png")
shadow_rect = shadow.get_rect(topleft=(-100, SCREEN_HEIGHT - 100))

current_event = None
jumpscare_img = pygame.image.load(ASSET_PATH + "jumpscare.png")

def init_events():
    global current_event
    current_event = None
    shadow_rect.x = -100

def maybe_trigger_event():
    global current_event
    roll = random.randint(1, 10)
    if roll == 1:
        current_event = "whisper"
    elif roll == 2:
        current_event = "shadow"
    else:
        current_event = None

def update_events(player, game_state):
    global current_event

    # --- Handle whisper event ---
    if current_event == "whisper":
        play_whisper()
        current_event = None  # Reset after playing

    # --- Handle shadow event ---
    if current_event == "shadow":
        if shadow_rect.x < player.rect.x:
            shadow_rect.x += 2
        elif shadow_rect.x > player.rect.x:
            shadow_rect.x -= 2
        if shadow_rect.y < player.rect.y:
            shadow_rect.y += 2
        elif shadow_rect.y > player.rect.y:
            shadow_rect.y -= 2

        # Check proximity to scream
        if abs(shadow_rect.x - player.rect.x) < 10 and abs(shadow_rect.y - player.rect.y) < 10:
            if not game_state['jumpscare_active']:
                play_scream()
            if shadow_rect.colliderect(player.rect) and not game_state['jumpscare_active']:
                play_jumpscare_scream()
                game_state['hearts'] -= 1
                game_state['jumpscare_active'] = True
                game_state['jumpscare_timer'] = pygame.time.get_ticks()

    # --- Handle jumpscare screen duration ---
    if game_state['jumpscare_active']:
        if pygame.time.get_ticks() - game_state['jumpscare_timer'] > 1500:
            game_state['jumpscare_active'] = False

def render_events(screen, game_state):
    if current_event == "shadow":
        screen.blit(shadow, shadow_rect)
    if game_state['jumpscare_active']:
        screen.blit(jumpscare_img, (0, 0))
