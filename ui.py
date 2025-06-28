import pygame
from settings import ASSET_PATH

heart_img = pygame.image.load(ASSET_PATH + "heart.png").convert_alpha()

def draw_hearts(screen, health):
    for i in range(health):
        screen.blit(heart_img, (10 + i * 35, 10))
        
def draw_end_message(screen, message):
    font = pygame.font.Font("Arial", 48)
    text = font.render(message, True, (255, 0, 0))
    rect = text.get_rect(center=(400, 250))
    screen.blit(text, rect)
    
    font_small = pygame.font.SysFont("Arial", 32)
    try_again = font_small.render("Press R to try again", True, (255, 255, 255))
    rect2 = try_again.get_rect(center=(400, 300))
    screen.blit(try_again, rect2)
    