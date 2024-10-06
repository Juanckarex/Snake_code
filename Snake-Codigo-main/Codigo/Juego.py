# juego.py
from snake import Snake
from snake2 import Snake2
from comida import Comida
import pygame

number_of_cells = 25
OFFSET = 75

class Juego:
    def __init__(self):
        # Instancias de ambas serpientes
        self.snake1 = Snake()  # Primer jugador (flechas)
        self.snake2 = Snake2()  # Segundo jugador (WASD)
        self.food = Comida(self.snake1.body + self.snake2.body)  # Comida generada teniendo en cuenta ambas serpientes
        self.state = "RUNNING"
        self.score1 = 0
        self.score2 = 0

    def draw(self, screen, food_surface):
        self.food.draw(screen, food_surface)
        self.snake1.draw(screen)  # Dibujar la primera serpiente
        self.snake2.draw(screen)  # Dibujar la segunda serpiente

    def update(self):
        if self.state == "RUNNING":
            # Actualizar ambas serpientes
            self.snake1.update()
            self.snake2.update()
            self.check_collision_with_food()
            self.check_collision_with_bordes(self.snake1)
            self.check_collision_with_bordes(self.snake2)
            self.check_collision_with_tail(self.snake1)
            self.check_collision_with_tail(self.snake2)
            self.check_collision_between_snakes()  # Colisión entre las dos serpientes

    def check_collision_with_food(self):
        # Verificar si la primera serpiente come la comida
        if self.snake1.body[0] == self.food.position:
            self.food.position = self.food.generate_random_pos(self.snake1.body + self.snake2.body)
            self.snake1.add_segment = True
            self.score1 += 1

        # Verificar si la segunda serpiente come la comida
        if self.snake2.body[0] == self.food.position:
            self.food.position = self.food.generate_random_pos(self.snake1.body + self.snake2.body)
            self.snake2.add_segment = True
            self.score2 += 1

    def check_collision_with_bordes(self, snake):
        # Comprobar si alguna serpiente choca con los bordes
        if (snake.body[0].x >= number_of_cells or snake.body[0].x < 0 or
            snake.body[0].y >= number_of_cells or snake.body[0].y < 0):
            self.game_over()

    def check_collision_with_tail(self, snake):
        # Comprobar si una serpiente colisiona con su propio cuerpo
        if snake.body[0] in snake.body[1:]:
            self.game_over()

    def check_collision_between_snakes(self):
        # Comprobar si la cabeza de una serpiente choca con el cuerpo de la otra
        if self.snake1.body[0] in self.snake2.body:
            self.game_over()

        if self.snake2.body[0] in self.snake1.body:
            self.game_over()

    def game_over(self):
        # Resetear ambas serpientes y la comida
        self.snake1.reset()
        self.snake2.reset()
        self.food.position = self.food.generate_random_pos(self.snake1.body + self.snake2.body)
        self.state = "STOPPED"
        self.score1 = 0
        self.score2 = 0
