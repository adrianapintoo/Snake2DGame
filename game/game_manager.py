'''GameManager class to handle the game logic, including snake movement,
 food spawning, and collision detection.'''

import pygame
from .snake import Snake
from .food import Food


class GameManager:
    '''GameManager class to handle the game logic, including snake movement,~
      food spawning, and collision detection.'''
    def __init__(self):
        self.snake = Snake()
        self.food = Food() 

    def handle_input(self, event):
        '''Handle user input for snake direction changes.'''
        if event.type == pygame.KEYDOWN: # pylint: disable=no-member
            if event.key == pygame.K_UP: # pylint: disable=no-member
                self.snake.change_direction((0, -1))
            elif event.key == pygame.K_DOWN: # pylint: disable=no-member
                self.snake.change_direction((0, 1))
            elif event.key == pygame.K_LEFT: # pylint: disable=no-member
                self.snake.change_direction((-1, 0))
            elif event.key == pygame.K_RIGHT: # pylint: disable=no-member
                self.snake.change_direction((1, 0))

    def update(self):
        '''Update the game state, including snake movement and food respawn.'''
        self.snake.move()
        if self.snake.body[0] == self.food.position:
            self.snake.grow()
            self.food.respawn(self.snake.body)
        if self.snake.collides_with_self():
            self.__init__()  # Restart the game

    def draw(self, screen):
        '''Draw the game elements on the screen.'''
        self.snake.draw(screen)
        self.food.draw(screen)
