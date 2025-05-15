import pygame
from config import SCREEN_WIDTH, CELL_SIZE, WHITE, FONT_SIZE

class ScoreTracker:
    def __init__(self):
        self.score = 0
        self.high_score = 0
        self.font = pygame.font.SysFont(None, FONT_SIZE)

    def increase(self, points=1):
        self.score += points
        if self.score > self.high_score:
            self.high_score = self.score

    def reset(self):
        self.score = 0

    def draw(self, screen):
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        high_score_text = self.font.render(f"High Score: {self.high_score}", True, WHITE)
        screen.blit(score_text, (CELL_SIZE, CELL_SIZE))
        screen.blit(high_score_text, (CELL_SIZE, CELL_SIZE * 2))