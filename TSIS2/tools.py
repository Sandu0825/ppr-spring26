import pygame


def draw_shape(surface, color, start_pos, end_pos, shape, size):
    """
    Draws shapes on the given surface.
    The same function is used for live preview and final drawing.
    """

    x1, y1 = start_pos
    x2, y2 = end_pos

    width = x2 - x1
    height = y2 - y1

    if shape == "rect":
        pygame.draw.rect(surface, color, (x1, y1, width, height), size)

    elif shape == "square":
        side = min(abs(width), abs(height))
        pygame.draw.rect(surface, color, (x1, y1, side, side), size)

    elif shape == "circle":
        radius = int((width ** 2 + height ** 2) ** 0.5 / 2)
        pygame.draw.circle(surface, color, start_pos, radius, size)

    elif shape == "right_tri":
        pygame.draw.polygon(surface, color, [
            (x1, y1),
            (x1, y2),
            (x2, y2)
        ], size)

    elif shape == "eq_tri":
        pygame.draw.polygon(surface, color, [
            (x1, y2),
            ((x1 + x2) // 2, y1),
            (x2, y2)
        ], size)

    elif shape == "rhombus":
        pygame.draw.polygon(surface, color, [
            ((x1 + x2) // 2, y1),
            (x2, (y1 + y2) // 2),
            ((x1 + x2) // 2, y2),
            (x1, (y1 + y2) // 2)
        ], size)


def flood_fill(surface, start_pos, new_color):
    """
    Flood fill algorithm.
    It fills connected pixels with the same color.
    It uses get_at() and set_at(), as required in the task.
    """

    width, height = surface.get_size()
    target_color = surface.get_at(start_pos)

    if target_color == new_color:
        return

    stack = [start_pos]

    while stack:
        x, y = stack.pop()

        if x < 0 or x >= width or y < 0 or y >= height:
            continue

        if surface.get_at((x, y)) != target_color:
            continue

        surface.set_at((x, y), new_color)

        stack.append((x + 1, y))
        stack.append((x - 1, y))
        stack.append((x, y + 1))
        stack.append((x, y - 1))