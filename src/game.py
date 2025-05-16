import pygame
import sys
from .constants import (
    WINDOW_SIZE, BASE_FPS, Direction, WHITE, BLACK, GRAY, DARK_GRAY,
    GAME_PADDING, GAME_AREA_SIZE, GRID_SIZE, GameState, SnakeSkin,
    GRID_COUNT, GameDifficulty
)
from .snake import Snake
from .food import Food
from .menu import Menu
from .skins_menu import SkinsMenu
from .difficulty_menu import DifficultyMenu

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
        self.current_skin = SnakeSkin.GREEN
        self.current_difficulty = GameDifficulty.MEDIUM
        self.snake = Snake(self.current_skin)
        self.food = Food()
        self.menu = Menu()
        self.skins_menu = SkinsMenu(self.current_skin)
        self.difficulty_menu = DifficultyMenu(self.current_difficulty)
        self.state = GameState.MENU
        self.running = True
        self.high_score = 0

    def handle_menu_input(self):
        """Handle input in menu state"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return
            
            action = self.menu.handle_event(event)
            if action is not None:
                if action == 0:  # Play button clicked
                    self.state = GameState.PLAYING
                    self.snake.reset()
                    self.food.spawn()
                elif action == 1:  # Skins button clicked
                    self.state = GameState.SKINS
                elif action == 2:  # Difficulty button clicked
                    self.state = GameState.DIFFICULTY
                elif action == 3:  # Quit button clicked
                    self.running = False

    def handle_skins_input(self):
        """Handle input in skins menu state"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return
            
            action, skin = self.skins_menu.handle_event(event)
            if action == 'back':
                self.state = GameState.MENU
            elif action == 'skin':
                self.current_skin = skin
                self.snake.set_skin(skin)

    def handle_difficulty_input(self):
        """Handle input in difficulty menu state"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return
            
            action, difficulty = self.difficulty_menu.handle_event(event)
            if action == 'back':
                self.state = GameState.MENU
            elif action == 'difficulty':
                self.current_difficulty = difficulty

    def handle_game_input(self):
        """Handle input in game state"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if self.snake.dead:
                    if event.key == pygame.K_SPACE:
                        self.snake.reset()
                        self.food.spawn()
                    elif event.key == pygame.K_ESCAPE:
                        self.state = GameState.MENU
                elif event.key == pygame.K_UP and self.snake.direction != Direction.DOWN:
                    self.snake.direction = Direction.UP
                elif event.key == pygame.K_DOWN and self.snake.direction != Direction.UP:
                    self.snake.direction = Direction.DOWN
                elif event.key == pygame.K_LEFT and self.snake.direction != Direction.RIGHT:
                    self.snake.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT and self.snake.direction != Direction.LEFT:
                    self.snake.direction = Direction.RIGHT
                elif event.key == pygame.K_ESCAPE:
                    self.state = GameState.MENU

    def handle_input(self):
        """Handle input based on game state"""
        if self.state == GameState.MENU:
            self.handle_menu_input()
        elif self.state == GameState.SKINS:
            self.handle_skins_input()
        elif self.state == GameState.DIFFICULTY:
            self.handle_difficulty_input()
        else:
            self.handle_game_input()

    def update(self):
        """Update game state"""
        if self.state == GameState.PLAYING:
            self.snake.move(self.food)
            if self.snake.score > self.high_score:
                self.high_score = self.snake.score

    def draw_game_area(self):
        """Draw the main game area and border"""
        # Calculate the centered position for the game area
        game_area_x = (WINDOW_SIZE - GAME_AREA_SIZE) // 2
        game_area_y = (WINDOW_SIZE - GAME_AREA_SIZE) // 2
        
        # Draw outer border
        outer_rect = pygame.Rect(
            game_area_x - 10,
            game_area_y - 10,
            GAME_AREA_SIZE + 20,
            GAME_AREA_SIZE + 20
        )
        pygame.draw.rect(self.screen, DARK_GRAY, outer_rect)
        
        # Draw inner game area
        game_rect = pygame.Rect(
            game_area_x,
            game_area_y,
            GAME_AREA_SIZE,
            GAME_AREA_SIZE
        )
        pygame.draw.rect(self.screen, WHITE, game_rect)

        # Draw grid
        for i in range(GRID_COUNT + 1):  # +1 to draw the last line
            # Vertical lines
            pygame.draw.line(
                self.screen,
                GRAY,
                (game_area_x + i * GRID_SIZE, game_area_y),
                (game_area_x + i * GRID_SIZE, game_area_y + GAME_AREA_SIZE),
                1
            )
            # Horizontal lines
            pygame.draw.line(
                self.screen,
                GRAY,
                (game_area_x, game_area_y + i * GRID_SIZE),
                (game_area_x + GAME_AREA_SIZE, game_area_y + i * GRID_SIZE),
                1
            )

    def draw_info(self):
        """Draw game information"""
        # Draw current score
        score_text = self.font.render(f"Score: {self.snake.score}", True, BLACK)
        self.screen.blit(score_text, (20, 10))

        # Draw high score
        high_score_text = self.font.render(f"High Score: {self.high_score}", True, BLACK)
        self.screen.blit(high_score_text, (WINDOW_SIZE - 200, 10))

        # Draw difficulty
        difficulty_text = self.small_font.render(f"Difficulty: {self.current_difficulty.label}", True, BLACK)
        self.screen.blit(difficulty_text, (20, 50))

        # Draw controls info
        controls_text = self.small_font.render("Controls: Arrow Keys | ESC for Menu", True, BLACK)
        self.screen.blit(controls_text, (20, WINDOW_SIZE - 30))

    def draw_game(self):
        """Draw the game state"""
        self.screen.fill(WHITE)
        self.draw_game_area()
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        self.draw_info()

        if self.snake.dead:
            game_over_text = self.font.render(
                "Game Over! Press SPACE to restart or ESC for menu",
                True,
                BLACK
            )
            text_rect = game_over_text.get_rect(center=(WINDOW_SIZE // 2, WINDOW_SIZE // 2))
            self.screen.blit(game_over_text, text_rect)

    def draw(self):
        """Draw the current state"""
        if self.state == GameState.MENU:
            self.menu.draw(self.screen)
        elif self.state == GameState.SKINS:
            self.skins_menu.draw(self.screen)
        elif self.state == GameState.DIFFICULTY:
            self.difficulty_menu.draw(self.screen)
        else:
            self.draw_game()
        
        pygame.display.flip()

    def run(self):
        """Main game loop"""
        while self.running:
            self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(self.current_difficulty.speed)

        pygame.quit()
        sys.exit() 