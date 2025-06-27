import pygame
from settings import ASSET_PATH, SCREEN_WIDTH
from events import maybe_trigger_event
import os

class RoomManager:
    def __init__(self):
        try:
            self.room_image = pygame.image.load(ASSET_PATH + 'room.png').convert()
        except (pygame.error, FileNotFoundError):
            print("Warning: 'room.png' not found. Using placeholder room image.")
            self.room_image = pygame.Surface((SCREEN_WIDTH, 600))
            self.room_image.fill((30, 30, 30))  # dark gray background

        self.rooms_passed = 0
        self.time_in_room = 0
        
    def update(self, player):
        if player.rect.left < 0:
            player.rect.left = 0
        if player.rect.right > SCREEN_WIDTH:
            player.rect.right = SCREEN_WIDTH
            
        self.time_in_room += 1
        if self.time_in_room == 301:
            maybe_trigger_event()
            
        if player.rect.right >= SCREEN_WIDTH:
            player.rect.right = 10
            self.rooms_passed += 1
            self.time_in_room = 0
            maybe_trigger_event()
            
    def get_current_room(self):
        return self.room_image
