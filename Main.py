import pygame
import sys
import random
from pygame.locals import *

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TITLE = "SNAKE"

# Create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)

# Game variables & constants
CELL_SIZE = 10
direction = 1
update_snake = 0
score = 0

snake_pos = [[int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)]] # head
snake_pos.append([int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2) + CELL_SIZE]) # segment
snake_pos.append([int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2) + CELL_SIZE * 2]) # segment
snake_pos.append([int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2) + CELL_SIZE * 3]) # segment

BG = (50, 160, 200)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BODY_INNER = (50, 175, 25)
BODY_OUTER = (100, 100, 200)
APPLE_COLOR = (180, 0, 0)

# Apple position
apple_pos = [random.randint(0, SCREEN_WIDTH // CELL_SIZE - 1) * CELL_SIZE, 
             random.randint(0, SCREEN_HEIGHT // CELL_SIZE - 1) * CELL_SIZE]

# font
font = pygame.font.SysFont(None, 35)

# Music
pygame.mixer.music.load('evil-type-beat.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

def draw_screen():
    screen.fill(BG)

def draw_apple():
    pygame.draw.rect(screen, APPLE_COLOR, (apple_pos[0], CELL_SIZE, CELL_SIZE))

def draw_score():
    score_text = font.render(f'Score: {score}', True, BLACK)
    screen.blit(score_text, [10, 10])

running = True
while running:
    draw_screen()
    draw_apple()
    draw_score()

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 3: # Up
                direction = 1
            elif event.key == pygame.K_RIGHT and direction != 4: # Right
                direction = 2 