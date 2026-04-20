import pygame
import math

pygame.init()

screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

screen.fill((255,255,255))  # white background

color = (255, 0, 0)
mode = "brush"

drawing = False
start_pos = None
last_pos = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #switching between tools
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                mode = "brush"
            elif event.key == pygame.K_r:
                mode = "rect"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_e:
                mode = "eraser"

            #simple color selection
            elif event.key == pygame.K_1:
                color = (255,0,0)
            elif event.key == pygame.K_2:
                color = (0,255,0)
            elif event.key == pygame.K_3:
                color = (0,0,255)
            elif event.key == pygame.K_4:
                color = (0,0,0)

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
            last_pos = event.pos

        elif event.type == pygame.MOUSEMOTION and drawing:
            #brush draws continuously
            if mode == "brush":
                pygame.draw.line(screen, color, last_pos, event.pos, 8)
                last_pos = event.pos

            #eraser just draws with white color
            elif mode == "eraser":
                pygame.draw.line(screen, (255,255,255), last_pos, event.pos, 20)
                last_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos

            #rectangle based on drag distance
            if mode == "rect":
                x = min(start_pos[0], end_pos[0])
                y = min(start_pos[1], end_pos[1])
                w = abs(end_pos[0] - start_pos[0])
                h = abs(end_pos[1] - start_pos[1])
                pygame.draw.rect(screen, color, (x,y,w,h), 2)

            # circle radius from distance between points
            elif mode == "circle":
                r = int(math.hypot(end_pos[0]-start_pos[0],
                                   end_pos[1]-start_pos[1]))
                pygame.draw.circle(screen, color, start_pos, r, 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()