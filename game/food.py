import random
import pygame
from Snake2DGame.config import CELL_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, FOOD_COLOR

class Food:
    def __init__(self):
        self.position = self._random_position()

    def _random_position(self):
        cols = SCREEN_WIDTH // CELL_SIZE
        rows = SCREEN_HEIGHT // CELL_SIZE
        return (random.randint(0, cols - 1), random.randint(0, rows - 1))

    def respawn(self, snake_body):
        while True:
            pos = self._random_position()
            if pos not in snake_body:
                self.position = pos
                break

    def draw(self, screen):
        x, y = self.position
        pygame.draw.rect(
            screen,
            FOOD_COLOR,
            (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        )
