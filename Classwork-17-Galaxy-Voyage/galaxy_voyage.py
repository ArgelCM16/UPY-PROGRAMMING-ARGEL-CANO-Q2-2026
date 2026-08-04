# galaxy_voyage.py
# Session 1 - Concept, planning, perspective math
# Deliverable: an animated perspective grid (vanishing point + non-linear spacing)
#
# Everything lives in one file on purpose (see the tutorial): don't organize
# what you don't understand yet. Modularization comes in Session 3.

import pygame


# CONFIGURATION

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
        print("galaxy_voyage: no se encontró config.txt, usando valores por defecto")
        config = {
            "width": 800, "height": 600,
            "bg_color": (30, 30, 30), "line_color": (255, 255, 255),
            "vertical_lines": 7, "space": 0.1,
            "horizon_ratio": 0.25, "num_rungs": 12,
            "curve_power": 2.0, "scroll_speed": 0.4,
        }
    return config


# FUNCTIONS

def calculate_x_positions(surface, vertical_lines, space):
    # Equally-spaced bottom positions for each converging line, centered on screen
    x_positions = []
    width = surface.get_width()
    spacing = space * width
    central_line = width / 2
    offset = -int(vertical_lines / 2)

    for _ in range(vertical_lines):
        x_positions.append(central_line + offset * spacing)
        offset += 1

    return x_positions


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


def draw_perspective_grid(surface, x_positions, vanishing_point, num_rungs, power, color, offset):
    width = surface.get_width()
    height = surface.get_height()
    vx, vy = vanishing_point
    available_height = height - vy

    # converging "vertical" lines: from each bottom position toward the vanishing point
    for x in x_positions:
        pygame.draw.line(surface, color, (x, height), (vx, vy), 2)

    # horizontal "rungs", spaced non-linearly, animated by shifting t with offset
    for i in range(num_rungs):
        t = ((i / num_rungs) + offset) % 1.0
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
            pygame.draw.lines(surface, color, False, points, 2)


# INITIALIZATION AND MAIN LOOP

if __name__ == "__main__":
    config = load_config("config.txt")

    pygame.init()
    screen = pygame.display.set_mode((config["width"], config["height"]))
    pygame.display.set_caption("Galaxy Voyage - Part 1: Perspective Grid")
    clock = pygame.time.Clock()

    vanishing_point = (config["width"] * 0.5, config["height"] * config["horizon_ratio"])
    x_positions = calculate_x_positions(screen, config["vertical_lines"], config["space"])
    print(x_positions)  # sanity check, same habit as the tutorial's main.py

    scroll_offset = 0.0
    running = True
    while running:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        scroll_offset = (scroll_offset + config["scroll_speed"] * dt) % 1.0

        screen.fill(config["bg_color"])
        draw_perspective_grid(
            screen, x_positions, vanishing_point,
            config["num_rungs"], config["curve_power"],
            config["line_color"], scroll_offset
        )
        pygame.display.flip()

    pygame.quit()
