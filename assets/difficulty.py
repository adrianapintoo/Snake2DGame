import pygame
import sys

class DifficultyMenu:
    def __init__(self, screen, back_callback, current_difficulty="normal"):
        self.screen = screen
        self.back_callback = back_callback
        self.selected_difficulty = current_difficulty
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 48)

        # Colors
        self.WHITE = (255, 255, 255)
        self.GRAY = (100, 100, 100)
        self.BLACK = (0, 0, 0)
        self.HOVER = (170, 170, 170)
        self.SELECTED_COLOR = (0, 200, 0)

        # Define difficulty options
        self.difficulty_buttons = [
            ("easy", pygame.Rect(300, 150, 200, 60)),
            ("normal", pygame.Rect(300, 230, 200, 60)),
            ("hard", pygame.Rect(300, 310, 200, 60)),
        ]

        # Back button (positioned top-left like in PersonalizationMenu)
        self.back_button = pygame.Rect(20, 140, 150, 40)

    def draw_button(self, text, rect, is_selected=False, is_back_button=False):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if is_back_button:
            color = self.HOVER if rect.collidepoint(mouse) else self.GRAY
        else:
            color = self.SELECTED_COLOR if is_selected else (
                self.HOVER if rect.collidepoint(mouse) else self.GRAY
            )

        pygame.draw.rect(self.screen, color, rect, border_radius=10)
        pygame.draw.rect(self.screen, self.WHITE, rect, 2, border_radius=10)

        text_surf = self.font.render(text.capitalize(), True, self.WHITE)
        text_rect = text_surf.get_rect(center=rect.center)
        self.screen.blit(text_surf, text_rect)

        if rect.collidepoint(mouse) and click[0]:
            pygame.time.wait(200)
            return True
        return False

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill(self.BLACK)
            title = self.font.render("Select Difficulty", True, self.WHITE)
            self.screen.blit(title, (250, 80))

            # Draw difficulty buttons
            for text, rect in self.difficulty_buttons:
                is_selected = (text == self.selected_difficulty)
                if self.draw_button(text, rect, is_selected):
                    self.selected_difficulty = text

            # Draw back button
            if self.draw_button("Back", self.back_button, is_back_button=True):
                return self.selected_difficulty

            pygame.display.flip()
            self.clock.tick(60)
