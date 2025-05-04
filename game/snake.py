import pygame
from Snake2DGame.config import CELL_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, SNAKE_COLOR

class Snake:
    def __init__(self):
        self.body = [(5, 5)]
        self.direction = (1, 0)
        self.grow_next = False

    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = ((head_x + dx) % (SCREEN_WIDTH // CELL_SIZE), 
                    (head_y + dy) % (SCREEN_HEIGHT // CELL_SIZE))
        self.body.insert(0, new_head)
        if not self.grow_next:
            self.body.pop()
        else:
            self.grow_next = False

    def grow(self):
        self.grow_next = True

    def change_direction(self, new_dir):
        if (new_dir[0] != -self.direction[0] or new_dir[1] != -self.direction[1]):
            self.direction = new_dir

    def collides_with_self(self):
        return self.body[0] in self.body[1:]

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(
                screen,
                SNAKE_COLOR,
                (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            )
