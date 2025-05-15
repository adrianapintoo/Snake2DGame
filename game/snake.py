import pygame
from config import CELL_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT

class Snake:
    def __init__(self, color=(0, 255, 0)):  # Default green
        self.body = [(5, 5)]
        self.direction = (1, 0)
        self.grow_segments = 0
        self.color = color

    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)  # NO wrapping here, just add direction
        self.body.insert(0, new_head)

        if self.grow_segments > 0:
            self.grow_segments -= 1
        else:
            self.body.pop()

    def grow(self, amount=1):
        self.grow_segments += amount

    def change_direction(self, new_dir):
        if (new_dir[0] != -self.direction[0] or new_dir[1] != -self.direction[1]):
            self.direction = new_dir

    def collides_with_self(self):
        return self.body[0] in self.body[1:]

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(
                screen,
                self.color,
                (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            )

    def set_color(self, color):
        self.color = color


