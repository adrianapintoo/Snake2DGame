import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, GRID_COLOR, CELL_SIZE

class Background:
    def __init__(self):
        self.grid_lines = True

    def toggle_grid(self):
        self.grid_lines = not self.grid_lines

    def draw(self, screen, bg_color):
        screen.fill(bg_color)
        if self.grid_lines:
            for x in range(0, SCREEN_WIDTH, CELL_SIZE):
                pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT))
            for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
                pygame.draw.line(screen, GRID_COLOR, (0, y), (SCREEN_WIDTH, y))