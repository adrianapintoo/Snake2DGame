import pygame
from .constants import WINDOW_SIZE, BLACK, WHITE, BLUE, LIGHT_BLUE, GameDifficulty

class DifficultyMenuItem:
    def __init__(self, text, position, is_selected=False, font_size=36, is_back_button=False):
        self.font = pygame.font.Font(None, font_size)
        self.text = text
        self.position = position
        self.is_hovered = False
        self.is_selected = is_selected
        self.is_back_button = is_back_button
        self._render()

    def _render(self):
        """Render the difficulty option with current state"""
        color = LIGHT_BLUE if self.is_hovered else BLUE
        if not self.is_back_button:
            text = f"● {self.text}" if self.is_selected else f"○ {self.text}"
        else:
            text = self.text
        self.surface = self.font.render(text, True, color)
        self.rect = self.surface.get_rect(center=self.position)

    def handle_event(self, event):
        """Handle mouse events and return True if clicked"""
        if event.type == pygame.MOUSEMOTION:
            old_hover = self.is_hovered
            self.is_hovered = self.rect.collidepoint(event.pos)
            if old_hover != self.is_hovered:
                self._render()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # Left click only
            if self.rect.collidepoint(event.pos):
                return True
        return False

    def draw(self, surface):
        """Draw the difficulty option"""
        surface.blit(self.surface, self.rect)
        
        if self.is_hovered:
            pygame.draw.line(surface, LIGHT_BLUE,
                           (self.rect.left, self.rect.bottom),
                           (self.rect.right, self.rect.bottom))

class DifficultyMenu:
    def __init__(self, current_difficulty=GameDifficulty.MEDIUM):
        self.title_font = pygame.font.Font(None, 74)
        self.title = self.title_font.render("Game Difficulty", True, BLACK)
        self.title_rect = self.title.get_rect(
            center=(WINDOW_SIZE // 2, WINDOW_SIZE // 4)
        )

        # Create difficulty options
        self.current_difficulty = current_difficulty
        self._create_difficulty_items()

        # Back button
        self.back_button = DifficultyMenuItem(
            "Back",
            (WINDOW_SIZE // 2, WINDOW_SIZE - 100),
            font_size=48,
            is_back_button=True
        )

    def _create_difficulty_items(self):
        """Create the difficulty selection items"""
        self.difficulty_items = []
        start_y = WINDOW_SIZE // 2 - 50
        spacing = 60

        for i, difficulty in enumerate(GameDifficulty):
            item = DifficultyMenuItem(
                difficulty.label,
                (WINDOW_SIZE // 2, start_y + (i * spacing)),
                is_selected=(difficulty == self.current_difficulty)
            )
            item.difficulty = difficulty  # Attach the difficulty to the item
            self.difficulty_items.append(item)

    def handle_event(self, event):
        """Handle menu events and return the selected difficulty or None"""
        # Check difficulty selections
        for item in self.difficulty_items:
            if item.handle_event(event):
                # Update selection status
                self.current_difficulty = item.difficulty
                self._create_difficulty_items()
                return ('difficulty', item.difficulty)

        # Check back button
        if self.back_button.handle_event(event):
            return ('back', None)

        return (None, None)

    def draw(self, surface):
        """Draw the difficulty menu"""
        surface.fill(WHITE)
        
        # Draw title
        surface.blit(self.title, self.title_rect)
        
        # Draw difficulty options
        for item in self.difficulty_items:
            item.draw(surface)

        # Draw back button
        self.back_button.draw(surface) 