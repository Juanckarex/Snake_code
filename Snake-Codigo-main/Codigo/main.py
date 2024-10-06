# main.py
import pygame, sys
from pygame.math import Vector2
from juego import Juego

# Configuración inicial
pygame.init()

title_font = pygame.font.Font(None, 60)
score_font = pygame.font.Font(None, 40)
GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24)
cell_size = 30
number_of_cells = 25
OFFSET = 75

# Pantalla y comida
screen = pygame.display.set_mode((2*OFFSET + cell_size*number_of_cells, 2*OFFSET + cell_size*number_of_cells))
pygame.display.set_caption("Retro Snake")
food_surface = pygame.image.load("food.png")

clock = pygame.time.Clock()

# Instancia del juego
juego = Juego()

# Configurar el temporizador para actualizar la serpiente
SNAKE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_UPDATE, 200)

while True:
    for event in pygame.event.get():
        if event.type == SNAKE_UPDATE:
            juego.update()  # Actualiza ambas serpientes

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Controles de entrada del jugador 1 y jugador 2
        if event.type == pygame.KEYDOWN:
            if juego.state == "STOPPED":
                juego.state = "RUNNING"
            
            # Controles para la primera serpiente (Jugador 1 - Flechas)
            if event.key == pygame.K_UP and juego.snake1.direction != Vector2(0, 1):
                juego.snake1.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN and juego.snake1.direction != Vector2(0, -1):
                juego.snake1.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT and juego.snake1.direction != Vector2(1, 0):
                juego.snake1.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT and juego.snake1.direction != Vector2(-1, 0):
                juego.snake1.direction = Vector2(1, 0)

            # Controles para la segunda serpiente (Jugador 2 - W, A, S, D)
            juego.snake2.handle_input(event)

    # Graficar el tablero
    screen.fill(GREEN)
    pygame.draw.rect(screen, DARK_GREEN,
                     (OFFSET-5, OFFSET-5, cell_size*number_of_cells+10, cell_size*number_of_cells+10), 5)

    # Dibujar todo el juego
    juego.draw(screen, food_surface)

    # Mostrar título y puntuación para ambos jugadores
    title_surface = title_font.render("Retro Snake", True, DARK_GREEN)
    score_surface1 = score_font.render(f"Player 1: {juego.score1}", True, DARK_GREEN)
    score_surface2 = score_font.render(f"Player 2: {juego.score2}", True, DARK_GREEN)
    
    screen.blit(title_surface, (OFFSET-5, 20))
    screen.blit(score_surface1, (OFFSET-5, OFFSET + cell_size*number_of_cells + 10))
    screen.blit(score_surface2, (OFFSET + 200, OFFSET + cell_size*number_of_cells + 10))

    pygame.display.update()
    clock.tick(60)
