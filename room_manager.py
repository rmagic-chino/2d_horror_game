import pygame
import random
from settings import ASSET_PATH, SCREEN_WIDTH, SCREEN_HEIGHT
from events import maybe_trigger_event

class RoomManager:
    def __init__(self):
        self.room_image = pygame.image.load(ASSET_PATH + "room.png")
        self.rooms_passed = 0
        self.exit_side = random.choice(['left', 'right', 'up', 'down'])

    def update(self, player):
        room_changed = False

        if player.rect.left <= 0 and self.exit_side == 'left':
            room_changed = True
        elif player.rect.right >= SCREEN_WIDTH and self.exit_side == 'right':
            room_changed = True
        elif player.rect.top <= 0 and self.exit_side == 'up':
            room_changed = True
        elif player.rect.bottom >= SCREEN_HEIGHT and self.exit_side == 'down':
            room_changed = True

        if room_changed:
            self.rooms_passed += 1
            if self.rooms_passed < 20:
                maybe_trigger_event()
                self.exit_side = random.choice(['left', 'right', 'up', 'down'])
                player.reset_position(self.exit_side)
            else:
                self.end_game()

    def end_game(self):
        pygame.quit()
        print("You survived all 20 rooms!")
        exit()

    def get_current_room(self):
        return self.room_image
