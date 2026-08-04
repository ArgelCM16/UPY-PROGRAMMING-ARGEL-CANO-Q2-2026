# perspective.py
# Pure math layer: config loading and the perspective corridor.
# No game state lives here - only functions that take inputs and return
# outputs, plus a couple of "draw_" functions that are the one exception
# (rendering necessarily has the side effect of touching the screen).

import pygame


def load_config(path="config.txt"):
    config = {}
    try:
        with open(path, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parameter, value = line.split("=")
                if "," in value:
                    config[parameter] = tuple(int(c.strip()) for c in value.split(","))
                elif "." in value:
                    config[parameter] = float(value)
                else:
                    config[parameter] = int(value)
    except FileNotFoundError:
        print("perspective: no se encontró config.txt, usando valores por defecto")
        config = default_config()
    return config


def default_config():
    return {
        "width": 800, "height": 600,
        "bg_color": (15, 15, 25), "line_color": (140, 200, 255),
        "vertical_lines": 9, "space": 0.09,
        "horizon_ratio": 0.25, "num_rungs": 14, "curve_power": 2.0,
        "scroll_speed": 0.35, "path_width": 3, "row_seconds": 0.6,
        "ship_color": (255, 200, 60), "ship_width": 40, "ship_height": 34,
        "hud_color": (230, 230, 230), "victory_score": 300,
        "safe_color": (60, 200, 120), "unsafe_color": (60, 60, 70),
    }


def calculate_x_positions(surface, vertical_lines, space):
    # Equally-spaced BOTTOM positions for each converging lane, centered on screen
    x_positions = []
    width = surface.get_width()
    spacing = space * width
    central_line = width / 2
    offset = -int(vertical_lines / 2)

    for _ in range(vertical_lines):
        x_positions.append(central_line + offset * spacing)
        offset += 1

    return x_positions


def draw_vertical_lines(surface, x_positions, color, width=2):
    # The Session-1 sanity check: straight, parallel, no perspective yet
    height = surface.get_height()
    for x in x_positions:
        pygame.draw.line(surface, color, (x, 0), (x, height), width)


def line_intersection(line1, line2):
    # RETURNS the (x, y) point where line1 and line2 cross, or None if parallel
    (x1, y1), (x2, y2) = line1
    (x3, y3), (x4, y4) = line2

    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denom == 0:
        return None

    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denom
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denom
    return (px, py)


def curved_y(t, vanishing_y, available_height, power):
    # Non-linear spacing: bunches rungs near the horizon, spreads them near the bottom
    return vanishing_y + (t ** power) * available_height


def lane_position(lane_bottom_x, vanishing_point, available_height, t, power):
    # Closed-form point where lane `lane_bottom_x` sits at depth t (0=horizon, 1=bottom).
    # Same t**power curve as curved_y, applied to x too, so the point stays
    # exactly on the straight line from (lane_bottom_x, bottom) to the vanishing point.
    vx, vy = vanishing_point
    k = t ** power
    x = vx + k * (lane_bottom_x - vx)
    y = vy + k * available_height
    return (x, y)


def draw_perspective_grid(surface, x_positions, vanishing_point, num_rungs, power, color):
    # Static corridor lines (used as a backdrop; the animated track is drawn on top)
    width = surface.get_width()
    height = surface.get_height()
    vx, vy = vanishing_point
    available_height = height - vy

    for x in x_positions:
        pygame.draw.line(surface, color, (x, height), (vx, vy), 1)

    for i in range(num_rungs + 1):
        t = i / num_rungs
        y = curved_y(t, vy, available_height, power)
        horizontal_line = ((0, y), (width, y))
        points = []
        for x in x_positions:
            vertical_line = ((x, height), (vx, vy))
            point = line_intersection(vertical_line, horizontal_line)
            if point is not None:
                points.append(point)
        if len(points) >= 2:
            points.sort(key=lambda point: point[0])
            pygame.draw.lines(surface, color, False, points, 1)
