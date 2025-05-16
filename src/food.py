import random
import pygame
from .constants import GRID_COUNT, GRID_SIZE, RED, BLACK, GAME_PADDING, WINDOW_SIZE, GAME_AREA_SIZE

class Food:
    def __init__(self):
        self.position = None
        self.spawn()

    def spawn(self, snake_positions=None):
        """Spawn food in a random position, avoiding snake's body"""
        snake_positions = snake_positions or []
        while True:
            position = (
                random.randint(0, GRID_COUNT - 1),
                random.randint(0, GRID_COUNT - 1)
            )
            if position not in snake_positions:
                self.position = position
                break

    def draw(self, surface):
        """Draw the food on the game surface"""
        game_area_x = (WINDOW_SIZE - GAME_AREA_SIZE) // 2
        game_area_y = (WINDOW_SIZE - GAME_AREA_SIZE) // 2
        
        food_rect = pygame.Rect(
            game_area_x + (self.position[0] * GRID_SIZE),
            game_area_y + (self.position[1] * GRID_SIZE),
            GRID_SIZE,
            GRID_SIZE
        )
        pygame.draw.rect(surface, RED, food_rect)
        pygame.draw.rect(surface, BLACK, food_rect, 1) 