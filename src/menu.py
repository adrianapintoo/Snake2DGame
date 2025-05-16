import pygame
from .constants import WINDOW_SIZE, BLACK, WHITE, BLUE, LIGHT_BLUE

class MenuItem:
    def __init__(self, text, position, font_size=48):
        self.font = pygame.font.Font(None, font_size)
        self.text = text
        self.position = position
        self.is_hovered = False
        self._render_text()

    def _render_text(self):
        """Render the text with the current state (hovered or not)"""
        color = LIGHT_BLUE if self.is_hovered else BLUE
        self.surface = self.font.render(self.text, True, color)
        self.rect = self.surface.get_rect(center=self.position)

    def handle_event(self, event):
        """Handle mouse events and return True if clicked"""
        if event.type == pygame.MOUSEMOTION:
            old_hover = self.is_hovered
            self.is_hovered = self.rect.collidepoint(event.pos)
            if old_hover != self.is_hovered:
                self._render_text()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # Left click only
            if self.rect.collidepoint(event.pos):
                return True
        return False

    def draw(self, surface):
        """Draw the menu item"""
        surface.blit(self.surface, self.rect)
        if self.is_hovered:
            pygame.draw.line(surface, LIGHT_BLUE,
                           (self.rect.left, self.rect.bottom),
                           (self.rect.right, self.rect.bottom))

class Menu:
    def __init__(self):
        self.title_font = pygame.font.Font(None, 74)
        self.title = self.title_font.render("Snake Game", True, BLACK)
        self.title_rect = self.title.get_rect(
            center=(WINDOW_SIZE // 2, WINDOW_SIZE // 4)
        )

        # Create menu items with proper spacing
        button_start_y = WINDOW_SIZE // 2
        button_spacing = 80
        
        # Store button names for reference
        self.button_names = ["Play", "Skins", "Difficulty", "Quit"]
        self.items = [
            MenuItem(name, (WINDOW_SIZE // 2, button_start_y + i * button_spacing))
            for i, name in enumerate(self.button_names)
        ]

    def handle_event(self, event):
        """Handle menu events and return the selected action"""
        if event.type in (pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION):
            for i, item in enumerate(self.items):
                if item.handle_event(event):
                    return i
        return None

    def draw(self, surface):
        """Draw the menu"""
        surface.fill(WHITE)
        
        # Draw title
        surface.blit(self.title, self.title_rect)
        
        # Draw menu items
        for item in self.items:
            item.draw(surface)

        # Draw version
        version_font = pygame.font.Font(None, 24)
        version_text = version_font.render("v1.0", True, BLUE)
        version_rect = version_text.get_rect(
            bottomright=(WINDOW_SIZE - 10, WINDOW_SIZE - 10)
        )
        surface.blit(version_text, version_rect) 