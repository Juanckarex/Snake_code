# obstaculo.py
from comida import Comida,OFFSET,cell_size
import pygame
from pygame.math import Vector2

class Obstaculo(Comida):
    def __init__(self, snake_body):
        
        super().__init__(snake_body)

    def draw(self, screen):
        # Aquí podemos cambiar el dibujo para que el obstáculo tenga una apariencia diferente
        obstacle_rect = pygame.Rect(
            OFFSET + self.position.x * cell_size,
            OFFSET + self.position.y * cell_size,
            cell_size,
            cell_size,
        )
        # Dibuja un obstáculo con un color diferente, por ejemplo gris oscuro
        pygame.draw.rect(screen, (100, 100, 100), obstacle_rect)
