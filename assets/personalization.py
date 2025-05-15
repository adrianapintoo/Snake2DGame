import pygame
import sys

class PersonalizationMenu:    
    def __init__(self, screen, back_callback, current_color):
        self.screen = screen
        self.back_callback = back_callback
        self.current_color = current_color  # Store the initially passed color
        self.selected_color = current_color  # Actively selected color
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 48)
        
        # Available color options
        self.colors = {
            "Green": (0, 255, 0),
            "Red": (255, 0, 0),
            "Blue": (0, 0, 255),
            "Yellow": (255, 255, 0),
        }
        
        # UI colors
        self.BLACK = (0, 0, 0)
        self.GRAY = (100, 100, 100)
        self.HOVER = (170, 170, 170)
        self.WHITE = (255, 255, 255)
        self.SELECTED = (0, 200, 0)  # Color for selected option
        
        # Button layout
        self.button_width = 300
        self.button_height = 50
        self.start_x = 220
        self.start_y = 150
        self.spacing = 65
        
        # Create buttons
        self.color_buttons = []
        for i, color_name in enumerate(self.colors.keys()):
            rect = pygame.Rect(
                self.start_x, 
                self.start_y + i * self.spacing, 
                self.button_width, 
                self.button_height
            )
            self.color_buttons.append((color_name, rect))
        
        # Back button
        self.back_button = pygame.Rect(20, 140, 150, 40)

    def draw_button(self, text, rect, is_selected=False, is_back_button=False):
        mouse_pos = pygame.mouse.get_pos()
        
        # Determine button color
        if is_back_button:
            color = self.HOVER if rect.collidepoint(mouse_pos) else self.GRAY
        else:
            if is_selected:
                color = self.SELECTED
            else:
                color = self.HOVER if rect.collidepoint(mouse_pos) else self.GRAY
        
        # Draw button
        pygame.draw.rect(self.screen, color, rect, border_radius=10)
        pygame.draw.rect(self.screen, self.WHITE, rect, 2, border_radius=10)  # Border
        
        # Draw text
        text_surf = self.font.render(text, True, self.WHITE)
        text_rect = text_surf.get_rect(center=rect.center)
        self.screen.blit(text_surf, text_rect)
        
        # Return True if clicked
        if rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            pygame.time.delay(150)  # Small delay for better click feedback
            return True
        return False

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.screen.fill(self.BLACK)
            
            # Draw title
            title = self.font.render("Choose Snake Color", True, self.WHITE)
            self.screen.blit(title, (self.screen.get_width()//2 - title.get_width()//2, 80))
            
            # Draw color buttons and handle clicks
            for color_name, rect in self.color_buttons:
                if self.draw_button(color_name, rect, color_name == self.selected_color):
                    self.selected_color = color_name
            
            # Draw back button and handle click
            if self.draw_button("Back", self.back_button, is_back_button=True):
                # Return the RGB value of the selected color name
                return self.colors[self.selected_color]
            
            pygame.display.flip()
            self.clock.tick(60)