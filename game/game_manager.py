'''GameManager class to handle the game logic, including snake movement,
 food spawning, and collision detection.'''
"""
import pygame
from .snake import Snake
from .food import Food
"""
"""
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
        """
        
import pygame
from .snake import Snake  # pylint:disable=import-error
from .food import Food
from .score_track import ScoreTracker  # pylint:disable=import-error
from config import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, CELL_SIZE  # pylint:disable=import-error

class GameManager:
    def __init__(self, difficulty="normal", snake_color=(0, 255, 0)):
        self.difficulty = difficulty  # keep as string: "easy", "normal", or "hard"
        self.speed = self.get_speed()
        self.snake_color = snake_color
        self.snake = Snake(color=self.snake_color)  # ✅ Pass color here
        self.food = Food()
        self.score_tracker = ScoreTracker()
        self.game_active = True
        self.paused = False

    def get_growth(self):
        """Return growth rate based on difficulty level"""
        if self.difficulty == "easy":
            return 1
        elif self.difficulty == "normal":
            return 2
        elif self.difficulty == "hard":
            return 3
        return 1  # default fallback
    
    def get_speed(self):
        if self.difficulty == "easy":
            return 5  # Slow
        elif self.difficulty == "normal":
            return 10
        elif self.difficulty == "hard":
            return 15  # Fast
        return 10  # default

    def handle_input(self, event):
        if not self.game_active or self.paused:
            return

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.snake.change_direction((0, -1))
            elif event.key == pygame.K_DOWN:
                self.snake.change_direction((0, 1))
            elif event.key == pygame.K_LEFT:
                self.snake.change_direction((-1, 0))
            elif event.key == pygame.K_RIGHT:
                self.snake.change_direction((1, 0))
            elif event.key == pygame.K_p:
                self.paused = not self.paused

    def update(self):
        if not self.game_active or self.paused:
            return

        self.snake.move()

        if self.difficulty in ("easy", "normal"):
            head_x, head_y = self.snake.body[0]
            grid_width = SCREEN_WIDTH // CELL_SIZE
            grid_height = SCREEN_HEIGHT // CELL_SIZE
            new_head = (head_x % grid_width, head_y % grid_height)
            self.snake.body[0] = new_head

        if self.snake.body[0] == self.food.position:
            self.snake.grow(self.get_growth())
            self.food.respawn(self.snake.body)
            self.score_tracker.increase(self.get_growth())

        if self.snake.collides_with_self():
            self.game_over()

        if self.difficulty == "hard":
            head_x, head_y = self.snake.body[0]
            grid_width = SCREEN_WIDTH // CELL_SIZE
            grid_height = SCREEN_HEIGHT // CELL_SIZE
            if head_x < 0 or head_x >= grid_width or head_y < 0 or head_y >= grid_height:
                self.game_over()


    def game_over(self):
        self.game_active = False

    def restart(self):
        self.__init__(difficulty=self.difficulty, snake_color=self.snake_color)

    def draw(self, screen):
        if not self.game_active:
            self.draw_game_over(screen)
            return

        self.snake.draw(screen)  # ✅ Don't pass color here anymore
        self.food.draw(screen)
        self.score_tracker.draw(screen)
        if self.paused:
            self.draw_paused(screen)

    def draw_game_over(self, screen):
        font = pygame.font.SysFont(None, 48)
        text = font.render("Game Over! Press R to restart", True, WHITE)
        screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, SCREEN_HEIGHT//2 - text.get_height()//2))

    def draw_paused(self, screen):
        font = pygame.font.SysFont(None, 48)
        text = font.render("Paused", True, WHITE)
        screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, SCREEN_HEIGHT//2 - text.get_height()//2))
