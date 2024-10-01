# snake.py
import pygame
from pygame.math import Vector2

cell_size = 30
OFFSET = 75
DARK_GREEN = (43, 51, 24)

class Snake:
    def __init__(self):
        self.body = [Vector2(6, 9), Vector2(5, 9), Vector2(4, 9)]
        self.direction = Vector2(1, 0)
        self.add_segment = False

    def draw(self, screen):
        for segment in self.body:
            segment_rect = pygame.Rect(
                OFFSET + segment.x * cell_size,
                OFFSET + segment.y * cell_size,
                cell_size,
                cell_size
            )
            pygame.draw.rect(screen, DARK_GREEN, segment_rect, 0, 7)

    def update(self):
        self.body.insert(0, self.body[0] + self.direction)
        if self.add_segment == True:
            self.add_segment = False
        else:
            self.body = self.body[:-1]

    def reset(self):
        self.body = [Vector2(6, 9), Vector2(5, 9), Vector2(4, 9)]
        self.direction = Vector2(1, 0)
