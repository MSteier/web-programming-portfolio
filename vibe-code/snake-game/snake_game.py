import pygame
import random
import os

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Constants
WIDTH, HEIGHT = 600, 600
BLOCK_SIZE = 20
SPEED = 10

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
WHITE = (255, 255, 255)

# Load sounds (make sure these files exist)
def _load_sound(path):
    """Try to load a sound file, return a silent dummy if it fails."""
    try:
        if not os.path.isabs(path):
            # make path relative to this script
            base = os.path.dirname(__file__)
            path = os.path.join(base, path)
        if not os.path.exists(path):
            raise FileNotFoundError(path)
        return pygame.mixer.Sound(path)
    except Exception:
        # Create a dummy object with a play() method to avoid crashes
        class _Silent:
            def play(self, *a, **k):
                return None
        return _Silent()

# Use a raw string for the absolute path or, better, compute it from __file__
EAT_SOUND = _load_sound(os.path.join(os.path.dirname(__file__), "eat.wav"))
GAME_OVER_SOUND = _load_sound(os.path.join(os.path.dirname(__file__), "gameover.wav"))

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
large_font = pygame.font.SysFont(None, 72)

def draw_text(text, font, color, surface, x, y):
    render = font.render(text, True, color)
    rect = render.get_rect(center=(x, y))
    surface.blit(render, rect)

def random_food(snake):
    while True:
        x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        if (x, y) not in snake:
            return (x, y)

def game_over_screen(score):
    screen.fill(BLACK)
    draw_text("GAME OVER", large_font, RED, screen, WIDTH // 2, HEIGHT // 2 - 40)
    draw_text(f"Score: {score}", font, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 10)
    draw_text("Press R to restart or Q to quit", font, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 50)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return False
                elif event.key == pygame.K_r:
                    return True

def main():
    snake = [(100, 100)]
    direction = 'RIGHT'
    food = random_food(snake)
    score = 0
    running = True

    while running:
        clock.tick(SPEED)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    direction = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    direction = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    direction = 'RIGHT'

        # Move the snake
        head_x, head_y = snake[-1]
        if direction == 'UP':
            head_y -= BLOCK_SIZE
        elif direction == 'DOWN':
            head_y += BLOCK_SIZE
        elif direction == 'LEFT':
            head_x -= BLOCK_SIZE
        elif direction == 'RIGHT':
            head_x += BLOCK_SIZE

        new_head = (head_x, head_y)

        # Check collisions
        if (
            head_x < 0 or head_x >= WIDTH or
            head_y < 0 or head_y >= HEIGHT or
            new_head in snake
        ):
            GAME_OVER_SOUND.play()
            if game_over_screen(score):
                main()  # restart
            return  # exit

        snake.append(new_head)

        # Eat food
        if new_head == food:
            EAT_SOUND.play()
            score += 1
            food = random_food(snake)
        else:
            snake.pop(0)

        # Draw everything
        screen.fill(BLACK)
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (*segment, BLOCK_SIZE, BLOCK_SIZE))

        pygame.draw.rect(screen, RED, (*food, BLOCK_SIZE, BLOCK_SIZE))
        draw_text(f"Score: {score}", font, WHITE, screen, 80, 20)

        pygame.display.flip()

# Run the game
if __name__ == "__main__":
    main()
    pygame.quit()
