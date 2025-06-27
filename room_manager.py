import pygame
from settings import ASSET_PATH, SCREEN_WIDTH, ROOM_TIME_LIMIT
from events import maybe_trigger_event

class RoomManager:
    def __init__(self):
        self.room_image = pygame.image.load(ASSET_PATH + 'room.png')
        self.rooms_passed = 0
        self.room_timer = 0
        
    