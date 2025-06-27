import json
import os

SAVE_FILE = "savegame.json"

def save_game(data):
    with open(SAVE_FILE, 'w') as file:
        json.dump(data, file)
        
def load_game():
    if not os.path.exists(SAVE_FILE):
        return None
    with open(SAVE_FILE, 'r') as file:
        return json.load(file)
    