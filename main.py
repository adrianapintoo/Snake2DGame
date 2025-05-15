''' Main entry point for the Snake Game. Initializes the game,
 handles events, and manages the game loop. '''

import pygame
from game.game_manager import GameManager
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BG_COLOR, FPS
from assets.background import Background
from assets.menu import MenuManager
from assets.personalization import PersonalizationMenu
from assets.difficulty import DifficultyMenu

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

background = Background()

def main():
    # Put selected options inside main's scope
    selected_snake_color = (0, 255, 0)  # default green
    selected_difficulty = "normal"      # default difficulty

    def start_game():
        # Use nonlocal variables when creating manager
        nonlocal selected_snake_color, selected_difficulty
        manager = GameManager(difficulty=selected_difficulty, snake_color=selected_snake_color)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                manager.handle_input(event)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r and not manager.game_active:
                        manager.restart()
                    elif event.key == pygame.K_g:
                        background.toggle_grid()

            background.draw(screen, BG_COLOR)
            manager.update()
            manager.draw(screen)
            pygame.display.flip()
            clock.tick(manager.speed)
        pygame.quit()

    def open_menu():
        menu.run()

    def open_personalize():
        nonlocal selected_snake_color
        personalization = PersonalizationMenu(screen, open_menu, selected_snake_color)
        selected_snake_color = personalization.run()  # Assume run returns selected color

    def open_difficulty():
        nonlocal selected_difficulty
        difficulty_menu = DifficultyMenu(screen, open_menu, selected_difficulty)
        selected_difficulty = difficulty_menu.run()  # Assume run returns difficulty string

    menu = MenuManager(screen, start_game, open_personalize, open_difficulty)
    menu.run()

if __name__ == "__main__":
    main()
