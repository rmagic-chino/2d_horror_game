from game_object import GameObject

class Enemy(GameObject):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        
    def update(self, player):
        pass