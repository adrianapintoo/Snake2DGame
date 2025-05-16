import pygame
from .constants import (
    Direction, GRID_COUNT, GRID_SIZE, GREEN, DARK_GREEN, BLACK,
    GAME_PADDING, SnakeSkin, WINDOW_SIZE, GAME_AREA_SIZE
)

class Snake:
    def __init__(self, skin=SnakeSkin.GREEN):
        self.skin = skin
        self.reset()

    def reset(self):
        """Reset snake to initial state"""
        self.length = 1
        self.positions = [(GRID_COUNT // 2, GRID_COUNT // 2)]
        self.direction = Direction.RIGHT
        self.score = 0
        self.dead = False

    def get_head_position(self):
        """Get the position of snake's head"""
        return self.positions[0]

    def move(self, food):
        """Move the snake and handle food collision"""
        if self.dead:
            return

        head = self.get_head_position()
        
        # Calculate new head position based on direction
        if self.direction == Direction.UP:
            new_head = (head[0], head[1] - 1)
        elif self.direction == Direction.DOWN:
            new_head = (head[0], head[1] + 1)
        elif self.direction == Direction.LEFT:
            new_head = (head[0] - 1, head[1])
        else:  # Direction.RIGHT
            new_head = (head[0] + 1, head[1])

        # Check for collisions with walls or self
        if (new_head[0] < 0 or new_head[0] >= GRID_COUNT or
            new_head[1] < 0 or new_head[1] >= GRID_COUNT or
            new_head in self.positions):
            self.dead = True
            return

        # Add new head
        self.positions.insert(0, new_head)
        
        # Check if food is eaten
        if new_head == food.position:
            self.score += 1
            food.spawn(self.positions)
        else:
            self.positions.pop()

    def set_skin(self, skin):
        """Change the snake's skin"""
        self.skin = skin

    def draw(self, surface):
        """Draw the snake on the game surface"""
        game_area_x = (WINDOW_SIZE - GAME_AREA_SIZE) // 2
        game_area_y = (WINDOW_SIZE - GAME_AREA_SIZE) // 2
        
        for i, pos in enumerate(self.positions):
            color = self.skin.dark_color if i == 0 else self.skin.main_color
            rect = pygame.Rect(
                game_area_x + (pos[0] * GRID_SIZE),
                game_area_y + (pos[1] * GRID_SIZE),
                GRID_SIZE,
                GRID_SIZE
            )
            pygame.draw.rect(surface, color, rect)
            pygame.draw.rect(surface, BLACK, rect, 1) 