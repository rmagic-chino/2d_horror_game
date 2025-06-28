import pygame
import random
from settings import ASSET_PATH, SCREEN_HEIGHT
from sounds import play_whisper, play_scream

shadow = pygame.image.load(ASSET_PATH + "shadow.png")
shadow_rect = shadow.get_rect(topleft=(-100, SCREEN_HEIGHT - 100))

current_event = None
jumpscare_img = pygame.image.load(ASSET_PATH + "jumpscare.png")

def init_events():
    global current_event
    current_event = None
    shadow_rect.x = -100
    shadow_rect.y = SCREEN_HEIGHT - 100

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
    if current_event == "shadow":
        # Move ghost toward player
        dx = player.rect.x - shadow_rect.x
        dy = player.rect.y - shadow_rect.y
        dist = (dx ** 2 + dy ** 2) ** 0.5
        if dist != 0:
            shadow_rect.x += int(2 * dx / dist)
            shadow_rect.y += int(2 * dy / dist)

        # Whisper if ghost is on screen
        if screen_visible(player.rect, shadow_rect):
            play_whisper()

        # Jumpscare and damage
        if shadow_rect.colliderect(player.rect):
            if not game_state['jumpscare_active']:
                play_scream()
                game_state['hearts'] -= 1
                game_state['jumpscare_active'] = True
                game_state['jumpscare_timer'] = pygame.time.get_ticks()

    if game_state['jumpscare_active']:
        if pygame.time.get_ticks() - game_state['jumpscare_timer'] > 1500:
            game_state['jumpscare_active'] = False

def screen_visible(player_rect, ghost_rect):
    area = player_rect.inflate(200, 200)
    return area.colliderect(ghost_rect)

def render_events(screen, game_state):
    if current_event == "shadow":
        screen.blit(shadow, shadow_rect)
    if game_state['jumpscare_active']:
        screen.blit(jumpscare_img, (0, 0))
