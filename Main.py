import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 10
TITLE = "Fart Snake"  # From Script 2, because... amazing
FPS = 10

# Colors
BG = (255, 255, 150)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BODY_INNER = (50, 175, 25)
BODY_OUTER = (100, 100, 200)
APPLE_COLOR = (255, 0, 0)
BUTTON_COLOR = (100, 100, 200)
TEXT_COLOR = (255, 255, 255)

# Sound effets
collect_sounds = [pygame.mixer.Sound("fart.mp3"), 
              pygame.mixer.Sound("dry-fart.mp3"), 
              pygame.mixer.Sound("lobotomy-sound-effect.mp3"), 
              pygame.mixer.Sound("rizz-sound-effect.mp3"), 
              pygame.mixer.Sound("smoke-detector-beep.mp3"), 
              pygame.mixer.Sound("vine-boom.mp3"), 
              pygame.mixer.Sound("taco-bell-bong-sfx.mp3"),
              pygame.mixer.Sound("flashbanggg.mp3")]

death_sound = pygame.mixer.Sound("yoda_death.mp3")

# Functions
def draw_snake(screen, snake_pos):
    for i, segment in enumerate(snake_pos):
        pygame.draw.rect(screen, BODY_OUTER, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
        inner_color = RED if i == 0 else BODY_INNER
        pygame.draw.rect(screen, inner_color, (segment[0]+1, segment[1]+1, CELL_SIZE-2, CELL_SIZE-2))

def draw_apple(screen, apple_pos):
    pygame.draw.rect(screen, APPLE_COLOR, (apple_pos[0], apple_pos[1], CELL_SIZE, CELL_SIZE))

def draw_score(screen, score, font):
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, [10, 10])

def run_snake_game():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 35)

    direction = 1
    score = 0
    snake_pos = [[int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)]]
    snake_pos.extend([[int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2) + CELL_SIZE * i] for i in range(1, 4)])
    apple_pos = [random.randint(0, SCREEN_WIDTH // CELL_SIZE - 1) * CELL_SIZE,
                 random.randint(0, SCREEN_HEIGHT // CELL_SIZE - 1) * CELL_SIZE]

    try:
        pygame.mixer.music.load('evil-type-beat.mp3')
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)
    except pygame.error as e:
        print(f"Error loading or playing music: {e}")

    running_game = True
    while running_game:
        screen.fill(BG)
        draw_apple(screen, apple_pos)
        draw_score(screen, score, font)
        draw_snake(screen, snake_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_game = False
            elif event.type == pygame.KEYDOWN:
                new_dir = direction
                if event.key == pygame.K_UP and direction != 3:
                    new_dir = 1
                elif event.key == pygame.K_RIGHT and direction != 4:
                    new_dir = 2
                elif event.key == pygame.K_DOWN and direction != 1:
                    new_dir = 3
                elif event.key == pygame.K_LEFT and direction != 2:
                    new_dir = 4
                direction = new_dir

        head_x, head_y = snake_pos[0]
        if direction == 1: head_y -= CELL_SIZE
        elif direction == 2: head_x += CELL_SIZE
        elif direction == 3: head_y += CELL_SIZE
        elif direction == 4: head_x -= CELL_SIZE

        snake_pos.insert(0, [head_x, head_y])

        if snake_pos[0] == apple_pos:
           
            # -- SOUND EFFECT PLAY --
            collect_sounds[random.randint(0, 7)].play()
           
            while apple_pos in snake_pos:
                apple_pos = [random.randint(0, SCREEN_WIDTH // CELL_SIZE - 1) * CELL_SIZE,
                             random.randint(0, SCREEN_HEIGHT // CELL_SIZE - 1) * CELL_SIZE]
            score += 1
        else:
            snake_pos.pop()

        if (head_x < 0 or head_x >= SCREEN_WIDTH or
            head_y < 0 or head_y >= SCREEN_HEIGHT or
            snake_pos[0] in snake_pos[1:]):
            death_sound.play()
            time.sleep(death_sound.get_length())
            running_game = False

        pygame.display.flip()
        clock.tick(FPS)

    pygame.mixer.music.stop()

def main_menu():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Main Menu")
    font = pygame.font.SysFont("Arial", 40)

    play_button = pygame.Rect(0, SCREEN_HEIGHT // 3, 200, 50)
    play_button.centerx = SCREEN_WIDTH // 2
    play_text = font.render("PLAY", True, TEXT_COLOR)
    play_text_rect = play_text.get_rect(center=play_button.center)

    exit_button = pygame.Rect(0, SCREEN_HEIGHT // 2 + 20, 200, 50)
    exit_button.centerx = SCREEN_WIDTH // 2
    exit_text = font.render("EXIT", True, TEXT_COLOR)
    exit_text_rect = exit_text.get_rect(center=exit_button.center)

    running_menu = True
    while running_menu:
        screen.fill((50, 50, 50))
        pygame.draw.rect(screen, BUTTON_COLOR, play_button)
        screen.blit(play_text, play_text_rect)
        pygame.draw.rect(screen, BUTTON_COLOR, exit_button)
        screen.blit(exit_text, exit_text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_menu = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if play_button.collidepoint(event.pos):
                    run_snake_game()
                elif exit_button.collidepoint(event.pos):
                    running_menu = False

        pygame.display.flip()

    pygame.quit()
    sys.exit()

# Entry point
if __name__ == "__main__":
    main_menu()
