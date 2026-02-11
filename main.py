import pygame
import math
import random
import sys

# ---------------- INIT ----------------
pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("For You 💙")

clock = pygame.time.Clock()

# ---------------- COLORS ----------------
BLACK = (0, 0, 0)
NAVY = (10, 30, 120)
GLOW = (40, 80, 200)
WHITE = (255, 255, 255)

# ---------------- MUSIC ----------------
pygame.mixer.music.load("khat.mp3")
pygame.mixer.music.play()

start_time = pygame.time.get_ticks()

# ---------------- FONT ----------------
font = pygame.font.SysFont("arial", 28, bold=True)

lyrics = [
    "Tere liye ghar banaau",
    "Deewaarein neele rang se sajaau",
    "Pasand hai tumhe, maloom hai",
    "Tumne bataya tha ek dafe",
    "",
    "Neele phool laau tere liye",
    "Khat likhu tere liye",
    "Mai khuda me maanu nahi",
    "Par maangu dua tere liye"
]

# ⏱️ Timing for each line (milliseconds)
# Adjust these if needed to sync better
timings = [2000, 5000, 8000, 11000, 14000,
           17000, 20000, 23000, 26000]

# ---------------- STARS ----------------
stars = []
for _ in range(150):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    speed = random.uniform(0.5, 1.5)
    stars.append([x, y, speed])

# ---------------- HEART EQUATION ----------------
def heart_x(t):
    return 16 * math.sin(t) ** 3

def heart_y(t):
    return (
        13 * math.cos(t)
        - 5 * math.cos(2 * t)
        - 2 * math.cos(3 * t)
        - math.cos(4 * t)
    )

# ---------------- MAIN LOOP ----------------
running = True
scale = 18
beat = 0

while running:
    screen.fill(BLACK)

    # 🌌 Moving stars
    for star in stars:
        star[1] += star[2]
        if star[1] > HEIGHT:
            star[0] = random.randint(0, WIDTH)
            star[1] = 0
        pygame.draw.circle(screen, WHITE, (int(star[0]), int(star[1])), 2)

    # 💓 Beating heart
    beat += 0.05
    dynamic_scale = scale + math.sin(beat) * 1.5

    for i in range(0, 628):
        t = i * 0.01
        x = heart_x(t) * dynamic_scale + WIDTH // 2
        y = -heart_y(t) * dynamic_scale + HEIGHT // 2 - 50

        pygame.draw.circle(screen, GLOW, (int(x), int(y)), 3)
        pygame.draw.circle(screen, NAVY, (int(x), int(y)), 2)

    # 🤍 Lyrics appearing line-by-line
    current_time = pygame.time.get_ticks() - start_time

    y_offset = HEIGHT // 2 - 80
    for i, line in enumerate(lyrics):
        if i < len(timings) and current_time >= timings[i]:
            text = font.render(line, True, WHITE)
            text_rect = text.get_rect(center=(WIDTH // 2, y_offset))
            screen.blit(text, text_rect)
            y_offset += 35

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
