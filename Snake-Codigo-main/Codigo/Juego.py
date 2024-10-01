# juego.py
from snake import Snake
from comida import Comida
import pygame

number_of_cells = 25
OFFSET = 75

class Juego:
    def __init__(self):
        self.snake = Snake()
        self.food = Comida(self.snake.body)
        self.state = "RUNNING"
        self.score = 0

    def draw(self, screen, food_surface):
        self.food.draw(screen, food_surface)
        self.snake.draw(screen)

    def update(self):
        if self.state == "RUNNING":
            self.snake.update()
            self.check_collision_with_food()
            self.check_collision_with_bordes()
            self.check_collision_with_tail()

    def check_collision_with_food(self):
        if self.snake.body[0] == self.food.position:
            self.food.position = self.food.generate_random_pos(self.snake.body)
            self.snake.add_segment = True
            self.score += 1

    def check_collision_with_bordes(self):
        if (self.snake.body[0].x >= number_of_cells or self.snake.body[0].x < 0 or
            self.snake.body[0].y >= number_of_cells or self.snake.body[0].y < 0):
            self.game_over()

    def check_collision_with_tail(self):
        if self.snake.body[0] in self.snake.body[1:]:
            self.game_over()

    def game_over(self):
        self.snake.reset()
        self.food.position = self.food.generate_random_pos(self.snake.body)
        self.state = "STOPPED"
        self.score = 0
