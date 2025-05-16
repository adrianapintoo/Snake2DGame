from enum import Enum

# Window Settings
WINDOW_SIZE = 800
GAME_PADDING = 50  # Padding around the game area
SIDEBAR_WIDTH = 200  # Width of the sidebar
GRID_SIZE = 30  # Size of each grid cell
GRID_COUNT = 20  # Reduced from 46 to 30 for a smaller game area
GAME_AREA_SIZE = GRID_SIZE * GRID_COUNT  # This ensures perfect squares

# Game Speed
BASE_FPS = 12  # Base speed for medium difficulty

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
DARK_RED = (200, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 200, 0)
BLUE = (0, 100, 255)
DARK_BLUE = (0, 80, 200)
LIGHT_BLUE = (100, 200, 255)
YELLOW = (255, 255, 0)
DARK_YELLOW = (200, 200, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)

# Game States
class GameState(Enum):
    MENU = 1
    PLAYING = 2
    GAME_OVER = 3
    SKINS = 4
    DIFFICULTY = 5

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class GameDifficulty(Enum):
    EASY = ("Easy", 8)
    MEDIUM = ("Medium", 12)
    HARD = ("Hard", 16)

    def __init__(self, label, speed):
        self.label = label
        self.speed = speed

class SnakeSkin(Enum):
    GREEN = ("Green", GREEN, DARK_GREEN)
    RED = ("Red", RED, DARK_RED)
    YELLOW = ("Yellow", YELLOW, DARK_YELLOW)
    BLUE = ("Blue", BLUE, DARK_BLUE)

    def __init__(self, label, main_color, dark_color):
        self.label = label
        self.main_color = main_color
        self.dark_color = dark_color 