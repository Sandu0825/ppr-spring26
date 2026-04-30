import pygame
import sys
import random
import json
import os
from pygame.locals import *

pygame.init()

WIDTH = 400
HEIGHT = 600
FPS = 60

SETTINGS_FILE = "settings.json"
LEADERBOARD_FILE = "leaderboard.json"

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

font_big = pygame.font.SysFont("Verdana", 50)
font_small = pygame.font.SysFont("Verdana", 18)
font_medium = pygame.font.SysFont("Verdana", 28)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSIS 3 Racer")

clock = pygame.time.Clock()
BASE_DIR = os.path.dirname(__file__)


# ================= SETTINGS =================

def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        return {"difficulty": "normal", "car_color": "red"}
    with open(SETTINGS_FILE, "r") as f:
        return json.load(f)


def save_settings(settings):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=4)


def load_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        return []
    with open(LEADERBOARD_FILE, "r") as f:
        return json.load(f)


def save_score(name, score, distance, coins):
    data = load_leaderboard()

    data.append({
        "name": name,
        "score": score,
        "distance": distance,
        "coins": coins
    })

    data = sorted(data, key=lambda x: x["score"], reverse=True)[:10]

    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(data, f, indent=4)


settings = load_settings()


# ================= IMAGES =================

background = pygame.image.load(os.path.join(BASE_DIR, "AnimatedStreet.png"))

player_img = pygame.transform.scale(
    pygame.image.load(os.path.join(BASE_DIR, "Player.png")), (60, 100)
)

enemy_img = pygame.transform.scale(
    pygame.image.load(os.path.join(BASE_DIR, "Enemy.png")), (60, 100)
)

coin_img = pygame.transform.scale(
    pygame.image.load(os.path.join(BASE_DIR, "coin.png")), (30, 30)
)


# 🔥 COLOR FUNCTION
def get_colored_car(color_name):
    img = player_img.copy()

    if color_name == "red":
        tint = (255, 0, 0)
    elif color_name == "blue":
        tint = (0, 0, 255)
    elif color_name == "green":
        tint = (0, 255, 0)
    else:
        return img

    img.fill(tint, special_flags=pygame.BLEND_MULT)
    return img


def draw_text(text, font, color, x, y):
    screen.blit(font.render(text, True, color), (x, y))


# ================= SCREENS =================

def leaderboard_screen():
    while True:
        screen.fill(WHITE)
        draw_text("TOP 10", font_big, BLACK, 100, 40)

        data = load_leaderboard()
        y = 120

        if not data:
            draw_text("No records yet", font_medium, BLACK, 90, 250)

        for i, item in enumerate(data):
            line = f"{i+1}. {item['name']} | S:{item['score']} D:{item['distance']} C:{item['coins']}"
            draw_text(line, font_small, BLACK, 10, y)
            y += 30

        draw_text("ESC - Back", font_small, RED, 130, 550)

        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit(); sys.exit()
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                return

        pygame.display.update()
        clock.tick(FPS)


def settings_screen():
    global settings

    while True:
        screen.fill(WHITE)
        draw_text("SETTINGS", font_big, BLACK, 70, 80)

        draw_text(f"1 - Difficulty: {settings['difficulty']}", font_medium, BLACK, 40, 250)
        draw_text(f"2 - Color: {settings['car_color']}", font_medium, BLACK, 40, 320)

        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit(); sys.exit()

            if e.type == KEYDOWN:
                if e.key == K_1:
                    settings["difficulty"] = (
                        "easy" if settings["difficulty"] == "hard"
                        else "normal" if settings["difficulty"] == "easy"
                        else "hard"
                    )
                    save_settings(settings)

                if e.key == K_2:
                    settings["car_color"] = (
                        "blue" if settings["car_color"] == "red"
                        else "green" if settings["car_color"] == "blue"
                        else "red"
                    )
                    save_settings(settings)

                if e.key == K_ESCAPE:
                    return

        pygame.display.update()
        clock.tick(FPS)


def main_menu():
    while True:
        screen.fill(WHITE)

        draw_text("RACER", font_big, BLACK, 100, 100)
        draw_text("1 - Play", font_medium, BLACK, 120, 250)
        draw_text("2 - Leaderboard", font_medium, BLACK, 80, 300)
        draw_text("3 - Settings", font_medium, BLACK, 100, 350)

        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit(); sys.exit()

            if e.type == KEYDOWN:
                if e.key == K_1:
                    return
                if e.key == K_2:
                    leaderboard_screen()
                if e.key == K_3:
                    settings_screen()

        pygame.display.update()
        clock.tick(FPS)


# ================= GAME =================

def run_game():
    speed = 5
    score = 0
    coins = 0
    distance = 0

    player = get_colored_car(settings["car_color"])
    player_rect = player.get_rect(center=(160, 520))

    enemy_rect = enemy_img.get_rect(center=(random.randint(40, WIDTH-40), 0))
    coin_rect = coin_img.get_rect(center=(random.randint(40, WIDTH-40), -100))

    # powerups
    nitro = pygame.Rect(random.randint(40, WIDTH-40), -300, 30, 30)
    shield = pygame.Rect(random.randint(40, WIDTH-40), -500, 30, 30)
    repair = pygame.Rect(random.randint(40, WIDTH-40), -700, 30, 30)

    active_power = None
    power_timer = 0
    spawn_timer = pygame.time.get_ticks()

    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit(); sys.exit()

        keys = pygame.key.get_pressed()
        if keys[K_LEFT] and player_rect.left > 0:
            player_rect.x -= 6
        if keys[K_RIGHT] and player_rect.right < WIDTH:
            player_rect.x += 6

        # movement
        enemy_rect.y += speed
        coin_rect.y += speed
        nitro.y += speed
        shield.y += speed
        repair.y += speed

        distance += 1

        # respawn
        if enemy_rect.top > HEIGHT:
            enemy_rect.y = -100
            enemy_rect.x = random.randint(40, WIDTH-40)
            score += 1

        if coin_rect.top > HEIGHT:
            coin_rect.y = -100
            coin_rect.x = random.randint(40, WIDTH-40)

        # powerups spawn every 7 sec
        if pygame.time.get_ticks() - spawn_timer > 7000:
            nitro.y = -300
            shield.y = -500
            repair.y = -700
            spawn_timer = pygame.time.get_ticks()

        # collect
        if player_rect.colliderect(coin_rect):
            coins += 1
            coin_rect.y = -100

        if player_rect.colliderect(nitro) and active_power is None:
            active_power = "Nitro"
            power_timer = pygame.time.get_ticks()
            speed += 3

        if player_rect.colliderect(shield) and active_power is None:
            active_power = "Shield"

        if player_rect.colliderect(repair) and active_power is None:
            active_power = "Repair"
            score += 5
            active_power = None

        # nitro timer
        if active_power == "Nitro":
            if pygame.time.get_ticks() - power_timer > 4000:
                speed -= 3
                active_power = None

        # collisions
        if player_rect.colliderect(enemy_rect):
            if active_power == "Shield":
                active_power = None
                enemy_rect.y = -100
            else:
                save_score(player_name, score, distance, coins)
                return

        # draw
        screen.blit(background, (0, 0))
        screen.blit(player, player_rect)
        screen.blit(enemy_img, enemy_rect)
        screen.blit(coin_img, coin_rect)

        pygame.draw.rect(screen, (0,255,255), nitro)
        pygame.draw.rect(screen, (255,255,0), shield)
        pygame.draw.rect(screen, (0,255,0), repair)

        draw_text(f"S:{score}", font_small, BLACK, 10, 10)
        draw_text(f"C:{coins}", font_small, BLACK, 300, 10)
        draw_text(f"D:{distance}", font_small, BLACK, 150, 40)

        if active_power:
            draw_text(f"{active_power}", font_small, BLUE, 150, 70)

        pygame.display.update()
        clock.tick(FPS)


# ================= RUN =================

player_name = "Player"

while True:
    main_menu()
    run_game()
