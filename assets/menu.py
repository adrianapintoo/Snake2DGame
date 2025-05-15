import pygame
import sys
from .personalization import PersonalizationMenu #pylint:disable=import-error
from .difficulty import DifficultyMenu #pylint:disable=import-error


class MenuManager:
    def __init__(self, screen, start_callback, personalize_callback, difficulty_callback):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 48)
        self.start_callback = start_callback
        self.personalize_callback = personalize_callback
        self.difficulty_callback = difficulty_callback

        # Colors
        self.WHITE = (255, 255, 255)
        self.GRAY = (100, 100, 100)
        self.BLACK = (0, 0, 0)
        self.HOVER = (170, 170, 170)

    def draw_button(self, text, x, y, width, height, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        rect = pygame.Rect(x, y, width, height)
        if rect.collidepoint(mouse):
            pygame.draw.rect(self.screen, self.HOVER, rect)
            if click[0] == 1 and action:
                pygame.time.wait(200)
                action()
        else:
            pygame.draw.rect(self.screen, self.GRAY, rect)

        text_surf = self.font.render(text, True, self.BLACK)
        text_rect = text_surf.get_rect(center=rect.center)
        self.screen.blit(text_surf, text_rect)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()

            self.screen.fill(self.BLACK)
            self.draw_button("Start Game", 300, 120, 200, 60, self.start_callback)
            self.draw_button("Personalize", 300, 190, 200, 60, self.personalize_callback)
            self.draw_button("Difficulty", 300, 260, 200, 60, self.difficulty_callback)
            self.draw_button("Quit", 300, 330, 200, 60, self.quit_game)

            pygame.display.flip()
            self.clock.tick(60)

    def quit_game(self):
        pygame.quit()
        sys.exit()
