import pygame
import random
from settings import ASSET_PATH, SCREEN_HEIGHT
from sounds import play_whisper, play_scream

shadow = pygame.image.load(ASSET_PATH + "shadow.png").convert_alpha()
shadow.set_alpha(128)
shadow_rect = shadow.get_rect(topleft=(-100, SCREEN_HEIGHT - 100))

current_event = None
jumpscare_img = pygame.image.load(ASSET_PATH + "jumpscare.png")
room_count_since_last_shadow = 0

def init_events():
    global current_event, room_count_since_last_shadow
    current_event = None
    shadow_rect.x = -100
    room_count_since_last_shadow = 0

def maybe_trigger_event(rooms_passed):
    global current_event, room_count_since_last_shadow
    room_count_since_last_shadow += 1
    if room_count_since_last_shadow >= 3:
        current_event = "shadow"
        room_count_since_last_shadow = 0
    else:
        roll = random.randint(1, 10)
        if roll == 1:
            current_event = "whisper"
        else:
            current_event = None

def update_events(player, game_state):
    if current_event == "shadow":
        if shadow_rect.x < player.rect.x:
            shadow_rect.x += 2
        elif shadow_rect.x > player.rect.x:
            shadow_rect.x -= 2
        if shadow_rect.y < player.rect.y:
            shadow_rect.y += 2
        elif shadow_rect.y > player.rect.y:
            shadow_rect.y -= 2

        if 0 < shadow_rect.x < 800 and 0 < shadow_rect.y < 600 and not game_state.get("whisper_triggered"):
            play_whisper()
            game_state["whisper_triggered"] = True

        if abs(shadow_rect.x - player.rect.x) < 10 and abs(shadow_rect.y - player.rect.y) < 10:
            play_scream()
            if shadow_rect.colliderect(player.rect) and not game_state['jumpscare_active']:
                game_state['hearts'] -= 1
                game_state['jumpscare_active'] = True
                game_state['jumpscare_timer'] = pygame.time.get_ticks()

    if game_state['jumpscare_active']:
        if pygame.time.get_ticks() - game_state['jumpscare_timer'] > 1500:
            game_state['jumpscare_active'] = False

def render_events(screen, game_state):
    if current_event == "shadow":
        screen.blit(shadow, shadow_rect)
    if game_state['jumpscare_active']:
        screen.blit(jumpscare_img, (0, 0))
