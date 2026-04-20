import pygame
import random
pygame.init()

#These are the dimensions of the game window
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

#Clock helps control FPS,so the game runs smoothly at a stable speed
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

#Player
#The player is represented by a rectangle,I place it near the bottom because in racing games
player = pygame.Rect(180, 500, 40, 60)
player_speed = 5

#Enemy
#The x-position is random, so each enemy spawn is a little different
enemy = pygame.Rect(random.randint(0, WIDTH - 40), -100, 40, 60)
enemy_speed = 5

#COIN
#The coin falls from the top too,It appears at a random x-position so the player has to move and collect it
coin = pygame.Rect(random.randint(0, WIDTH - 30), -50, 30, 30)
coin_speed = 5

#This variable stores how many coins the player has collected
coins = 0

running = True
while running:
    # I repaint the whole background every frame.
    # This is a normal part of the game loop in Pygame.
    screen.fill((50, 50, 50))

    #Events
    #Here I handle all events, especially the close-window event.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #pygame.key.get_pressed() returns the current state of all keys.
    #This is useful for smooth movement while a key is being held down.
    keys = pygame.key.get_pressed()

    #Player movement
    #I let the player move left and right only inside the screen,Without these checks, the car could leave the visible area.
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player_speed

    if keys[pygame.K_RIGHT] and player.x < WIDTH - player.width:
        player.x += player_speed

    #Enemy movement
    enemy.y += enemy_speed

    # If the enemy goes below the screen, I respawn it at the top,I also choose a new random x-position to make the game less repetitive
    if enemy.y > HEIGHT:
        enemy.y = -100
        enemy.x = random.randint(0, WIDTH - enemy.width)

    #Coin movement
    coin.y += coin_speed
    if coin.y > HEIGHT:
        coin.y = -50
        coin.x = random.randint(0, WIDTH - coin.width)

    #Coin collision
    # colliderect() checks whether two rectangles overlap
    if player.colliderect(coin):
        coins += 1
        coin.y = -50
        coin.x = random.randint(0, WIDTH - coin.width)

    #Enemy collision
    #If the player touches the enemy, the game ends.
    #For this simple version, I just stop the loop and print a message.
    if player.colliderect(enemy):
        print("Game Over")
        running = False

    #Drawing
    # I draw everything after updating positions,Blue = player, Red = enemy, Yellow = coin
    pygame.draw.rect(screen, (0, 0, 255), player)
    pygame.draw.rect(screen, (255, 0, 0), enemy)
    pygame.draw.rect(screen, (255, 255, 0), coin)

    #The task asks to show collected coins in the top-right corner,so I render text and place it there.
    coins_text = font.render(f"Coins: {coins}", True, (255, 255, 255))
    screen.blit(coins_text, (WIDTH - 110, 10))

    # flip() updates the screen with everything drawn in this frame.
    pygame.display.flip()

    # 60 FPS keeps the game smooth and prevents it from running too fast.
    clock.tick(60)

pygame.quit()