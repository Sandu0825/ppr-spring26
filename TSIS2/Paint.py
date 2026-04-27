import pygame
import datetime
from tools import draw_shape, flood_fill


pygame.init()
pygame.font.init()


WIDTH, HEIGHT = 1000, 700
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Application TSIS2")

clock = pygame.time.Clock()


COLORS = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
}


canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(COLORS["white"])


font = pygame.font.SysFont("Arial", 24)
ui_font = pygame.font.SysFont("Arial", 16)


current_tool = "pencil"
current_color = COLORS["black"]
current_color_name = "black"

current_size = 5
sizes = {
    pygame.K_1: 2,
    pygame.K_2: 5,
    pygame.K_3: 10
}


drawing = False
last_pos = None
start_pos = None


typing = False
text_input = ""
text_pos = (0, 0)


def draw_ui():
    """
    Draws the top bar.
    It shows current tool, color, brush size, and keyboard shortcuts.
    """

    pygame.draw.rect(screen, (220, 220, 220), (0, 0, WIDTH, 35))
    pygame.draw.line(screen, (120, 120, 120), (0, 35), (WIDTH, 35), 2)

    info = f"Tool: {current_tool.upper()} | Color: {current_color_name.upper()} | Size: {current_size}px"

    controls = (
        "P-pencil L-line R-rect C-circle Q-square "
        "7-right triangle 8-eq triangle 9-rhombus | "
        "F-fill T-text E-eraser | 1/2/3 size | Z/X/V/B colors | Ctrl+S save"
    )

    info_surface = ui_font.render(info, True, COLORS["black"])
    controls_surface = ui_font.render(controls, True, COLORS["black"])

    screen.blit(info_surface, (10, 3))
    screen.blit(controls_surface, (10, 18))


running = True

while running:
    screen.blit(canvas, (0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            # Text mode works separately.
            # While typing, keyboard input becomes text.
            if typing:
                if event.key == pygame.K_RETURN:
                    text_surface = font.render(text_input, True, current_color)
                    canvas.blit(text_surface, text_pos)
                    typing = False
                    text_input = ""

                elif event.key == pygame.K_ESCAPE:
                    typing = False
                    text_input = ""

                elif event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]

                else:
                    text_input += event.unicode

                continue

            # Save canvas with timestamp.
            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                filename = datetime.datetime.now().strftime("canvas_%Y%m%d_%H%M%S.png")
                pygame.image.save(canvas, filename)
                print("Saved:", filename)

            # Tool shortcuts.
            if event.key == pygame.K_p:
                current_tool = "pencil"

            elif event.key == pygame.K_l:
                current_tool = "line"

            elif event.key == pygame.K_r:
                current_tool = "rect"

            elif event.key == pygame.K_c:
                current_tool = "circle"

            elif event.key == pygame.K_q:
                current_tool = "square"

            elif event.key == pygame.K_7:
                current_tool = "right_tri"

            elif event.key == pygame.K_8:
                current_tool = "eq_tri"

            elif event.key == pygame.K_9:
                current_tool = "rhombus"

            elif event.key == pygame.K_f:
                current_tool = "fill"

            elif event.key == pygame.K_t:
                current_tool = "text"

            elif event.key == pygame.K_e:
                current_tool = "eraser"

            # Color shortcuts.
            if event.key == pygame.K_z:
                current_color = COLORS["black"]
                current_color_name = "black"

            elif event.key == pygame.K_x:
                current_color = COLORS["red"]
                current_color_name = "red"

            elif event.key == pygame.K_v:
                current_color = COLORS["green"]
                current_color_name = "green"

            elif event.key == pygame.K_b:
                current_color = COLORS["blue"]
                current_color_name = "blue"

            # Brush size shortcuts.
            if event.key in sizes:
                current_size = sizes[event.key]

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                # Prevent drawing on the UI bar.
                if event.pos[1] < 35:
                    continue

                if current_tool == "text":
                    typing = True
                    text_pos = event.pos
                    text_input = ""

                elif current_tool == "fill":
                    flood_fill(canvas, event.pos, current_color)

                else:
                    drawing = True
                    start_pos = event.pos
                    last_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and drawing:
                drawing = False

                if current_tool == "line":
                    pygame.draw.line(canvas, current_color, start_pos, event.pos, current_size)

                elif current_tool not in ["pencil", "eraser", "fill", "text"]:
                    draw_shape(canvas, current_color, start_pos, event.pos, current_tool, current_size)

        if event.type == pygame.MOUSEMOTION:
            if drawing:

                if current_tool == "pencil":
                    pygame.draw.line(canvas, current_color, last_pos, event.pos, current_size)
                    last_pos = event.pos

                elif current_tool == "eraser":
                    pygame.draw.line(canvas, COLORS["white"], last_pos, event.pos, current_size)
                    last_pos = event.pos

    # Live preview for line and shapes.
    # Preview is drawn on screen, not on canvas.
    if drawing and current_tool not in ["pencil", "eraser", "fill", "text"]:
        mouse_pos = pygame.mouse.get_pos()

        if current_tool == "line":
            pygame.draw.line(screen, current_color, start_pos, mouse_pos, current_size)

        else:
            draw_shape(screen, current_color, start_pos, mouse_pos, current_tool, current_size)

    # Live preview for text.
    if typing:
        text_surface = font.render(text_input + "|", True, current_color)
        screen.blit(text_surface, text_pos)

    draw_ui()

    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()