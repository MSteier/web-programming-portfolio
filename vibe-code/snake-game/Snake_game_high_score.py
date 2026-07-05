# Snake game created with claude code

import pygame
import random
import sys
import json
import os
import math
from collections import deque

pygame.init()

WIDTH, HEIGHT = 800, 480
CELL = 20
COLS = WIDTH // CELL
ROWS = HEIGHT // CELL

BLACK   = (0,   0,   0)
WHITE   = (255, 255, 255)
GREEN   = (0,   200, 0)
DKGREEN = (0,   150, 0)
RED     = (220, 50,  50)
GRAY    = (40,  40,  40)
GOLD    = (255, 215, 0)
DIM     = (150, 150, 150)

FPS = 10

MILESTONE_MSGS = [
    "Good Job!", "You're Unstoppable!", "Way to Go!",
    "Keep It Up!", "On Fire!", "Incredible!", "Snake Master!",
]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wiggles the Snake - High Score Edition")
clock      = pygame.time.Clock()
font_big   = pygame.font.SysFont("consolas", 48, bold=True)
font_med   = pygame.font.SysFont("consolas", 30, bold=True)
font_small = pygame.font.SysFont("consolas", 24)
font_tiny  = pygame.font.SysFont("consolas", 20)

GRID_SURF = pygame.Surface((WIDTH, HEIGHT))
GRID_SURF.fill(BLACK)
for _gx in range(COLS):
    for _gy in range(ROWS):
        pygame.draw.rect(GRID_SURF, GRAY, (_gx * CELL, _gy * CELL, CELL, CELL), 1)

SCORES_FILE    = os.path.join(os.path.dirname(os.path.abspath(__file__)), "high_scores.json")
DEFAULT_SCORES = [{"initials": "CPU", "score": 100}]
MAX_ENTRIES    = 10


# ---------- persistence ----------

def load_scores():
    if os.path.exists(SCORES_FILE):
        try:
            with open(SCORES_FILE, "r") as f:
                data = json.load(f)
            if isinstance(data, list) and all("initials" in e and "score" in e for e in data):
                return sorted(data, key=lambda e: e["score"], reverse=True)
        except (json.JSONDecodeError, KeyError):
            pass
    return list(DEFAULT_SCORES)


def save_scores(scores):
    with open(SCORES_FILE, "w") as f:
        json.dump(scores[:MAX_ENTRIES], f, indent=2)


def add_score(scores, initials, score):
    scores.append({"initials": initials.upper()[:3], "score": score})
    scores.sort(key=lambda e: e["score"], reverse=True)
    scores = scores[:MAX_ENTRIES]
    save_scores(scores)
    return scores


def is_high_score(scores, score):
    if score <= 0 or any(e["score"] == score for e in scores):
        return False
    return len(scores) < MAX_ENTRIES or score > scores[-1]["score"]


# ---------- drawing helpers ----------

def quit_game():
    pygame.quit()
    sys.exit()


def make_particles(n=40):
    return [
        {'x': random.uniform(0, WIDTH), 'y': random.uniform(0, HEIGHT),
         'vy': random.uniform(0.3, 1.0), 'size': random.randint(2, 4),
         'phase': random.uniform(0, 6.28)}
        for _ in range(n)
    ]


def draw_particles(particles, elapsed):
    for p in particles:
        p['y'] -= p['vy']
        if p['y'] < 0:
            p['y'] = float(HEIGHT + p['size'])
            p['x'] = random.uniform(0, WIDTH)
        b = int(128 + 127 * math.sin(elapsed / 600.0 + p['phase']))
        pygame.draw.circle(screen, (b, int(b * 0.84), 0), (int(p['x']), int(p['y'])), p['size'])


def pulse_color(base, elapsed, period=600.0, lo=0.80, amp=0.20):
    t = lo + amp * math.sin(elapsed / period)
    return tuple(int(c * t) for c in base)


def random_food(snake_set):
    while True:
        pos = (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))
        if pos not in snake_set:
            return pos


def draw_cell(x, y, color, border=None):
    rect = pygame.Rect(x * CELL + 1, y * CELL + 1, CELL - 2, CELL - 2)
    pygame.draw.rect(screen, color, rect, border_radius=4)
    if border:
        pygame.draw.rect(screen, border, rect, width=1, border_radius=4)


def draw_text_centered(text, font, color, cy):
    surf = font.render(text, True, color)
    screen.blit(surf, surf.get_rect(center=(WIDTH // 2, cy)))


def show_overlay(title, sub):
    screen.fill(BLACK)
    title_font = font_big if font_big.size(title)[0] <= WIDTH - 20 else font_med
    draw_text_centered(title, title_font, WHITE, HEIGHT // 2 - 30)
    draw_text_centered(sub,   font_small, WHITE, HEIGHT // 2 + 20)
    pygame.display.flip()


# ---------- screens ----------

def show_initials_screen(final_score):
    static_surfs = [
        (font_big.render("NEW HIGH SCORE!", True, GOLD),                          100),
        (font_med.render(f"Score: {final_score}", True, WHITE),                   165),
        (font_small.render("Enter your initials (3 chars)", True, DIM),           220),
        (font_tiny.render("BACKSPACE to delete  |  ENTER to confirm", True, DIM), 360),
    ]
    initials = ""
    while True:
        screen.fill(BLACK)
        for surf, cy in static_surfs:
            screen.blit(surf, surf.get_rect(center=(WIDTH // 2, cy)))
        draw_text_centered(initials + "_" * (3 - len(initials)), font_big, GOLD, 285)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and initials:
                    return initials.upper()
                elif event.key == pygame.K_BACKSPACE:
                    initials = initials[:-1]
                elif len(initials) < 3 and event.unicode.isalpha():
                    initials += event.unicode.upper()
        clock.tick(30)


def show_high_scores_screen(scores, highlight_score=None, timeout_ms=None):
    start_time  = pygame.time.get_ticks()
    particles   = make_particles()
    row_surfs   = [
        None if entry['score'] == highlight_score
        else font_small.render(f"{i+1:>2}.  {entry['initials']:<3}   {entry['score']:>5}", True, WHITE)
        for i, entry in enumerate(scores[:MAX_ENTRIES])
    ]
    footer_surf = font_tiny.render("Press any key to play again  |  Q to exit ", True, DIM)
    footer_rect = footer_surf.get_rect(center=(WIDTH // 2, HEIGHT - 30))

    while True:
        now     = pygame.time.get_ticks()
        elapsed = now - start_time

        screen.fill(BLACK)
        draw_particles(particles, elapsed)
        draw_text_centered("TOP SCORES", font_big, pulse_color(GOLD, elapsed), 40)

        left_x, row_y = 288, 110
        for i, entry in enumerate(scores[:MAX_ENTRIES]):
            t = elapsed - i * 100
            if t < 0:
                row_y += 30
                continue
            eased    = 1.0 - (1.0 - min(1.0, t / 350.0)) ** 3
            offset_x = int((1.0 - eased) * (WIDTH - left_x + 60))
            if row_surfs[i] is None:
                hl   = 0.60 + 0.40 * abs(math.sin(elapsed / 350.0))
                surf = font_small.render(
                    f"{i+1:>2}.  {entry['initials']:<3}   {entry['score']:>5}",
                    True, (int(255 * hl), int(215 * hl), 0))
            else:
                surf = row_surfs[i]
            screen.blit(surf, (left_x + offset_x, row_y - surf.get_height() // 2))
            row_y += 30

        screen.blit(footer_surf, footer_rect)
        pygame.display.flip()

        if timeout_ms is not None and elapsed >= timeout_ms:
            return None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.KEYDOWN:
                return event.key
        clock.tick(30)


def show_help_screen():
    start_time  = pygame.time.get_ticks()
    particles   = make_particles()
    instr_surfs = [
        (font_small.render(k, True, GOLD), font_small.render(d, True, WHITE))
        for k, d in [
            ("ARROW KEYS",   "Move the snake"),
            ("EAT RED FOOD", "Grow longer  (+10 pts each)"),
            ("AVOID WALLS",  "Don't hit the edges"),
            ("AVOID TAIL",   "Don't cross your own body"),
            ("Q",            "Quit the game"),
            ("H",            "Show this help screen"),
        ]
    ]
    footer_surf = font_tiny.render("Press any key to return", True, DIM)
    footer_rect = footer_surf.get_rect(center=(WIDTH // 2, HEIGHT - 30))

    while True:
        now     = pygame.time.get_ticks()
        elapsed = now - start_time

        screen.fill(BLACK)
        draw_particles(particles, elapsed)
        draw_text_centered("HOW TO PLAY", font_big, pulse_color(GOLD, elapsed), 45)

        y = 135
        for key_surf, desc_surf in instr_surfs:
            screen.blit(key_surf,  key_surf.get_rect(right=370, centery=y))
            screen.blit(desc_surf, desc_surf.get_rect(left=390,  centery=y))
            y += 40

        screen.blit(footer_surf, footer_rect)
        pygame.display.flip()

        if elapsed >= 60000:
            return
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.KEYDOWN:
                return
        clock.tick(30)


def show_game_over(final_score, scores):
    highlight = None
    if is_high_score(scores, final_score):
        initials  = show_initials_screen(final_score)
        scores    = add_score(scores, initials, final_score)
        highlight = final_score
    else:
        show_overlay("GAME OVER", f"Score: {final_score}  —  press any key")
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_game()
                if event.type == pygame.KEYDOWN:
                    waiting = False
            clock.tick(30)

    key = show_high_scores_screen(scores, highlight_score=highlight, timeout_ms=15000)
    if key is None:
        return None, scores
    return key != pygame.K_q, scores


# ---------- gameplay ----------

def run_game():
    start      = (COLS // 2, ROWS // 2)
    snake      = deque([start])
    snake_set  = {start}
    direction  = (1, 0)
    pending    = direction
    food       = random_food(snake_set)
    score      = 0
    score_surf = font_small.render("Score: 0", True, WHITE)
    msg_text   = ""
    msg_surf   = None
    msg_until  = 0
    msg_idx    = 0

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.KEYDOWN:
                if   event.key == pygame.K_UP    and direction != (0,  1): pending = (0, -1)
                elif event.key == pygame.K_DOWN  and direction != (0, -1): pending = (0,  1)
                elif event.key == pygame.K_LEFT  and direction != (1,  0): pending = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction != (-1, 0): pending = (1,  0)

        direction = pending
        head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

        if not (0 <= head[0] < COLS and 0 <= head[1] < ROWS) or head in snake_set:
            return score

        snake.appendleft(head)
        snake_set.add(head)

        now = pygame.time.get_ticks()
        if head == food:
            score += 10
            score_surf = font_small.render(f"Score: {score}", True, WHITE)
            food = random_food(snake_set)
            if score % 100 == 0:
                msg_text  = MILESTONE_MSGS[msg_idx % len(MILESTONE_MSGS)]
                msg_surf  = font_big.render(msg_text, True, GOLD)
                msg_until = now + 2500
                msg_idx  += 1
        else:
            snake_set.discard(snake.pop())

        screen.blit(GRID_SURF, (0, 0))
        for i, (x, y) in enumerate(snake):
            draw_cell(x, y, GREEN if i else (100, 255, 100), DKGREEN if i else None)
        draw_cell(food[0], food[1], RED)
        screen.blit(score_surf, (8, 6))

        if msg_surf and now < msg_until:
            remaining = msg_until - now
            surf = font_big.render(
                msg_text, True, (int(255 * remaining / 500), int(215 * remaining / 500), 0)
            ) if remaining < 500 else msg_surf
            screen.blit(surf, surf.get_rect(center=(WIDTH // 2, HEIGHT // 2)))

        pygame.display.flip()


# ---------- start screen ----------

def show_start_screen():
    DEMO_LEN  = 15
    DEMO_MS   = 110

    title      = "Wiggles the Snake - High Score Edition"
    title_font = font_big if font_big.size(title)[0] <= WIDTH - 20 else font_med
    title_surf = title_font.render(title, True, WHITE)
    title_rect = title_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30))
    sub_surf   = font_small.render("Press any key to start  |  H for help", True, WHITE)
    sub_rect   = sub_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))

    demo      = deque([(COLS // 2, ROWS // 2)])
    demo_set  = {(COLS // 2, ROWS // 2)}
    demo_dir  = (1, 0)
    last_move = pygame.time.get_ticks()
    start     = pygame.time.get_ticks()

    while True:
        now     = pygame.time.get_ticks()
        elapsed = now - start

        if elapsed >= 15000:
            return False

        if now - last_move >= DEMO_MS:
            last_move = now
            dx, dy    = demo_dir
            left, right = (-dy, dx), (dy, -dx)
            options = ([random.choice([left, right]), demo_dir, left, right]
                       if random.random() < 0.12 else [demo_dir, left, right])
            options.append((-dx, -dy))

            for d in options:
                nx, ny = demo[0][0] + d[0], demo[0][1] + d[1]
                if 0 <= nx < COLS and 0 <= ny < ROWS and (nx, ny) not in demo_set:
                    demo_dir = d
                    demo.appendleft((nx, ny))
                    demo_set.add((nx, ny))
                    if len(demo) > DEMO_LEN:
                        demo_set.discard(demo.pop())
                    break
            else:
                demo     = deque([(COLS // 2, ROWS // 2)])
                demo_set = {(COLS // 2, ROWS // 2)}
                demo_dir = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])

        screen.blit(GRID_SURF, (0, 0))
        for i, (x, y) in enumerate(demo):
            draw_cell(x, y, (0, 130, 0) if i == 0 else (0, 70, 0))
        screen.blit(title_surf, title_rect)
        screen.blit(sub_surf,   sub_rect)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    show_help_screen()
                    start = pygame.time.get_ticks()
                else:
                    return True
        clock.tick(30)


# ---------- main ----------

def main():
    scores = load_scores()
    while True:
        if not show_start_screen():
            key = show_high_scores_screen(scores, timeout_ms=15000)
            if key == pygame.K_q:
                quit_game()
            continue

        final_score = run_game()
        play_again, scores = show_game_over(final_score, scores)

        if play_again is None:
            continue
        if not play_again:
            quit_game()


if __name__ == "__main__":
    main()
