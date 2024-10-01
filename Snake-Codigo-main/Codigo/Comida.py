# comida.py
import random
import pygame
from pygame.math import Vector2

cell_size = 30
number_of_cells = 25
OFFSET = 75

class Comida:
    def __init__(self, snake_body):
        self.position = self.generate_random_pos(snake_body)

    def draw(self, screen, food_surface):
        food_rect = pygame.Rect(
            OFFSET + self.position.x * cell_size,
            OFFSET + self.position.y * cell_size,
            cell_size,
            cell_size,
        )
        screen.blit(food_surface, food_rect)

    def generate_random_cell(self):
        x = random.randint(0, number_of_cells - 1)
        y = random.randint(0, number_of_cells - 1)
        return Vector2(x, y)

    def generate_random_pos(self, snake_body):
        position = self.generate_random_cell()
        while position in snake_body:
            position = self.generate_random_cell()
        return position
