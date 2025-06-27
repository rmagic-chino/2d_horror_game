import pygame
import random
from settings import ASSET_PATH, SCREEN_WIDTH
from events import maybe_trigger_event

class RoomManager:
    def __init__(self):
        self.room_image = pygame.image.load(ASSET_PATH + 'room.png')
        self.rooms_passed = 0
        self.time_in_room = 0
        self.exit_side = random.choice(["left", "right"])

    def update(self, player):
        if player.rect.left < 0:
            player.rect.left = 0
        if player.rect.right > SCREEN_WIDTH:
            player.rect.right = SCREEN_WIDTH

        self.time_in_room += 1
        if self.time_in_room == 301:
            maybe_trigger_event()

        if (self.exit_side == "right" and player.rect.right >= SCREEN_WIDTH) or \
           (self.exit_side == "left" and player.rect.left <= 0):
            self.rooms_passed += 1
            self.time_in_room = 0
            self.exit_side = random.choice(["left", "right"])
            # reposition player to opposite side of new room
            if self.exit_side == "right":
                player.rect.left = 10
            else:
                player.rect.right = SCREEN_WIDTH - 10
            maybe_trigger_event()

    def get_current_room(self):
        return self.room_image
