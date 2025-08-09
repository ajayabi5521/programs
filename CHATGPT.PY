import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Window size
WIDTH = 800
HEIGHT = 800


# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 25)

# Snake block size and speed
block_size = 20
snake_speed = 10


def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], block_size, block_size])


def show_score(score):
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, [10, 10])


def game_loop():
    game_over = False
    game_close = False

    # Initial snake position
    x = WIDTH // 2
    y = HEIGHT // 2
    dx = 0
    dy = 0

    snake_list = []
    length_of_snake = 1

    # Initial food position
    food_x = round(random.randrange(0, WIDTH - block_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, HEIGHT - block_size) / 20.0) * 20.0

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            msg = font.render("Game Over! Press Q-Quit or R-Restart", True, RED)
            screen.blit(msg, [WIDTH // 6, HEIGHT // 3])
            show_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx = -block_size
                    dy = 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx = block_size
                    dy = 0
                elif event.key == pygame.K_UP and dy == 0:
                    dx = 0
                    dy = -block_size
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx = 0
                    dy = block_size

        # Update position
        x += dx
        y += dy

        # Check boundaries
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            game_close = True

        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [food_x, food_y, block_size, block_size])

        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check collision with itself
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_list)
        show_score(length_of_snake - 1)
        pygame.display.update()

        # Check if snake ate the food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - block_size) / 20.0) * 20.0
            food_y = round(random.randrange(0, HEIGHT - block_size) / 20.0) * 20.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


# Run the game
game_loop()
