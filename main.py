''' Main entry point for the Snake Game. Initializes the game,
 handles events, and manages the game loop. '''

import pygame
from game.game_manager import GameManager
from Snake2DGame.config import SCREEN_WIDTH, SCREEN_HEIGHT, BG_COLOR, FPS


def main():
    '''Main function to initialize the game and start the game loop.'''
    pygame.init() # pylint: disable=no-member
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()
    manager = GameManager()

    running = True
    while running:
        screen.fill(BG_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # pylint: disable=no-member
                running = False
            manager.handle_input(event)

        manager.update()
        manager.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit() # pylint: disable=no-member

if __name__ == "__main__":
    main()
