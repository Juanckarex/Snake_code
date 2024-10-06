# snake2.py
import pygame
from snake import Snake
from pygame.math import Vector2

class Snake2(Snake): #Herencia
    def __init__(self):
        super().__init__()

        self.body = [Vector2(18, 9), Vector2(17, 9), Vector2(16, 9)]
        # La dirección inicial puede permanecer igual (movimiento hacia la derecha)
        self.direction = Vector2(1, 0)

    def handle_input(self, event):
       
        if event.key == pygame.K_w and self.direction != Vector2(0, 1):
            self.direction = Vector2(0, -1)  
        elif event.key == pygame.K_s and self.direction != Vector2(0, -1):
            self.direction = Vector2(0, 1)   
        elif event.key == pygame.K_a and self.direction != Vector2(1, 0):
            self.direction = Vector2(-1, 0)  
        elif event.key == pygame.K_d and self.direction != Vector2(-1, 0):
            self.direction = Vector2(1, 0)   

    def reset(self):
        # Reiniciar la serpiente con una posición inicial diferente
        self.body = [Vector2(18, 9), Vector2(17, 9), Vector2(16, 9)]
        self.direction = Vector2(1, 0)