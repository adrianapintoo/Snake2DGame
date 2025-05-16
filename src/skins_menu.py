import pygame
from .constants import WINDOW_SIZE, BLACK, WHITE, BLUE, LIGHT_BLUE, SnakeSkin

class SkinMenuItem:
    def __init__(self, text, position, is_selected=False, font_size=36, is_back_button=False):
        self.font = pygame.font.Font(None, font_size)
        self.text = text
        self.position = position
        self.is_hovered = False
        self.is_selected = is_selected
        self.is_back_button = is_back_button
        self._render()

    def _render(self):
        """Render the skin option with current state"""
        # Create the text surface
        color = LIGHT_BLUE if self.is_hovered else BLUE
        if not self.is_back_button:
            text = f"● {self.text}" if self.is_selected else f"○ {self.text}"
        else:
            text = self.text
        self.surface = self.font.render(text, True, color)
        self.rect = self.surface.get_rect(center=self.position)

        if not self.is_back_button:
            # Create the color preview
            self.preview_rect = pygame.Rect(
                self.rect.right + 20,  # Position it after the text
                self.rect.centery - 10,  # Center vertically
                40,  # Width of preview
                20   # Height of preview
            )

    def handle_event(self, event):
        """Handle mouse events and return True if clicked"""
        if event.type == pygame.MOUSEMOTION:
            old_hover = self.is_hovered
            if self.is_back_button:
                self.is_hovered = self.rect.collidepoint(event.pos)
            else:
                self.is_hovered = self.rect.collidepoint(event.pos) or self.preview_rect.collidepoint(event.pos)
            if old_hover != self.is_hovered:
                self._render()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # Left click only
            if self.is_back_button:
                if self.rect.collidepoint(event.pos):
                    return True
            else:
                if self.rect.collidepoint(event.pos) or self.preview_rect.collidepoint(event.pos):
                    return True
        return False

    def draw(self, surface):
        """Draw the skin option"""
        surface.blit(self.surface, self.rect)
        
        if not self.is_back_button:
            # Draw color preview
            pygame.draw.rect(surface, self.skin.main_color, self.preview_rect)
            pygame.draw.rect(surface, BLACK, self.preview_rect, 1)

        if self.is_hovered:
            if self.is_back_button:
                pygame.draw.line(surface, LIGHT_BLUE,
                               (self.rect.left, self.rect.bottom),
                               (self.rect.right, self.rect.bottom))
            else:
                pygame.draw.line(surface, LIGHT_BLUE,
                               (self.rect.left, self.rect.bottom),
                               (self.preview_rect.right, self.rect.bottom))

class SkinsMenu:
    def __init__(self, current_skin=SnakeSkin.GREEN):
        self.title_font = pygame.font.Font(None, 74)
        self.title = self.title_font.render("Snake Skins", True, BLACK)
        self.title_rect = self.title.get_rect(
            center=(WINDOW_SIZE // 2, WINDOW_SIZE // 4)
        )

        # Create skin options
        self.current_skin = current_skin
        self._create_skin_items()

        # Back button
        self.back_button = SkinMenuItem(
            "Back",
            (WINDOW_SIZE // 2, WINDOW_SIZE - 100),
            font_size=48,
            is_back_button=True
        )

    def _create_skin_items(self):
        """Create the skin selection items"""
        self.skin_items = []
        start_y = WINDOW_SIZE // 2 - 100
        spacing = 60

        for i, skin in enumerate(SnakeSkin):
            item = SkinMenuItem(
                skin.label,
                (WINDOW_SIZE // 2 - 50, start_y + (i * spacing)),
                is_selected=(skin == self.current_skin)
            )
            item.skin = skin  # Attach the skin to the item
            self.skin_items.append(item)

    def handle_event(self, event):
        """Handle menu events and return the selected skin or None"""
        # Check skin selections
        for item in self.skin_items:
            if item.handle_event(event):
                # Update selection status
                self.current_skin = item.skin
                self._create_skin_items()
                return ('skin', item.skin)

        # Check back button
        if self.back_button.handle_event(event):
            return ('back', None)

        return (None, None)

    def draw(self, surface):
        """Draw the skins menu"""
        surface.fill(WHITE)
        
        # Draw title
        surface.blit(self.title, self.title_rect)
        
        # Draw skin options
        for item in self.skin_items:
            item.draw(surface)

        # Draw back button
        self.back_button.draw(surface) 