
import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 10
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nokia Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (213, 50, 80)
BLACK = (0, 0, 0)

# Snake and food variables
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_pos = [random.randrange(1, (WIDTH // BLOCK_SIZE)) * BLOCK_SIZE,
            random.randrange(1, (HEIGHT // BLOCK_SIZE)) * BLOCK_SIZE]
food_spawn = True

# Direction
direction = 'RIGHT'
change_to = direction
speed = 15

clock = pygame.time.Clock()

def show_score(score):
    font = pygame.font.SysFont("arial", 20)
    score_surface = font.render(f"Score: {score}", True, RED)
    screen.blit(score_surface, (10, 10))

running = True
score = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'

    # Update direction
    direction = change_to
    
    # Move snake
    if direction == 'UP':
        snake_pos[1] -= BLOCK_SIZE
    elif direction == 'DOWN':
        snake_pos[1] += BLOCK_SIZE
    elif direction == 'LEFT':
        snake_pos[0] -= BLOCK_SIZE
    elif direction == 'RIGHT':
        snake_pos[0] += BLOCK_SIZE
    
    # Grow snake
    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        score += 10
        food_spawn = False
    else:
        snake_body.pop()
    
    if not food_spawn:
        food_pos = [random.randrange(1, (WIDTH // BLOCK_SIZE)) * BLOCK_SIZE,
                    random.randrange(1, (HEIGHT // BLOCK_SIZE)) * BLOCK_SIZE]
    food_spawn = True

    # Game over conditions
    if snake_pos[0] < 0 or snake_pos[0] >= WIDTH or snake_pos[1] < 0 or snake_pos[1] >= HEIGHT:
        running = False
    for block in snake_body[1:]:
        if snake_pos == block:
            running = False

    # Drawing
    screen.fill(BLACK)
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE))

    show_score(score)
    pygame.display.flip()

    clock.tick(speed)

pygame.quit()
