import pygame
import random
pygame.init()
WIDTH, HEIGHT = 400, 400

#Each snake segment and food item will use this block size
BLOCK = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)
#SNAKE DATA 
# I store the snake as a list of coordinate pairs,the first element is always the head
snake = [(200, 200)]

#The snake starts by moving to the right.
# Since BLOCK = 20, each move shifts the head by one cell
direction = (BLOCK, 0)

#Basic game values
score = 0
level = 1
speed = 5

#  FOOD FUNCTION
# This function creates food in a random grid position,The important part is that food should not appear inside the snake.
# So I keep generating positions until I find a free cell.
def spawn_food():
    while True:
        x = random.randrange(0, WIDTH, BLOCK)
        y = random.randrange(0, HEIGHT, BLOCK)

        if (x, y) not in snake:
            return (x, y)

#First food item
food = spawn_food()

running = True
while running:
    #EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #I change direction with arrow keys,these extra checks prevent the snake from reversing directly
        # into itself in one move.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, BLOCK):
                direction = (0, -BLOCK)
            elif event.key == pygame.K_DOWN and direction != (0, -BLOCK):
                direction = (0, BLOCK)
            elif event.key == pygame.K_LEFT and direction != (BLOCK, 0):
                direction = (-BLOCK, 0)
            elif event.key == pygame.K_RIGHT and direction != (-BLOCK, 0):
                direction = (BLOCK, 0)

    # MOVE SNAKE
    # The new head position is based on the current head and the current direction
    new_head = (
        snake[0][0] + direction[0],
        snake[0][1] + direction[1]
    )

    # WALL COLLISION
    # If the new head leaves the playing area, the game ends
    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
        running = False
        continue

    #SELF COLLISION
    #If the head enters a cell that already belongs to the snake,that means the snake collided with itself.
    if new_head in snake:
        running = False
        continue

    #Add the new head at the beginning of the list.
    snake.insert(0, new_head)

    #EATING FOOD 
    if new_head == food:
        score += 1
        food = spawn_food()
    else:
        snake.pop()

    level = score // 3 + 1

    speed = 5 + level * 2

    screen.fill((0, 0, 0))

    # Draw each part of the snake.
    for part in snake:
        pygame.draw.rect(screen, (0, 200, 0), (part[0], part[1], BLOCK, BLOCK))

    # Draw food as a red square.
    pygame.draw.rect(screen, (255, 0, 0), (food[0], food[1], BLOCK, BLOCK))

    # Practice 10 also asks to show score and level.
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    level_text = font.render(f"Level: {level}", True, (255, 255, 255))

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 35))

    pygame.display.flip()

    # Faster speed at higher levels
    clock.tick(speed)

pygame.quit()