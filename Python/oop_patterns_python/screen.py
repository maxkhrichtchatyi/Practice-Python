#!/usr/bin/env python3

import pygame
import random
import math

SCREEN_DIM = (800, 600)


class Vec2d:
    """
    Функции для работы с векторами
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sub(self, other):
        """"возвращает разность двух векторов"""
        if not isinstance(other, Vec2d):
            raise TypeError('Vector can be added to a vector only!')

        return Vec2d(self.x - other.x, self.y - other.y)

    def add(self, other):
        """возвращает сумму двух векторов"""
        return Vec2d(self.x + other.x, self.y + other.y)

    def length(x):
        """возвращает длину вектора"""
        return math.sqrt(x[0] * x[0] + x[1] * x[1])

    def mul(v, k):
        """возвращает произведение вектора на число"""
        return v[0] * k, v[1] * k

    def int_pait(self):
        """возвращает пару координат, определяющих вектор (координаты точки конца вектора),
        координаты начальной точки вектора совпадают с началом системы координат (0, 0)"""
        return (self.y, self.x)


class Polyline:
    points = []
    speeds = []

    def add_points(self, point, speed):
        points.append(point)
        speeds.append(speed)

    def set_points(self):
        """функция перерасчета координат опорных точек"""
        for p in range(len(self.points)):
            self.points[p] = self.points[p] + self.speeds[p]
            if self.points[p][0] > SCREEN_DIM[0] or self.points[p][0] < 0:
                self.speeds[p] = (- self.speeds[p][0], self.speeds[p][1])
            if self.points[p][1] > SCREEN_DIM[1] or self.points[p][1] < 0:
                self.speeds[p] = (self.speeds[p][0], -self.speeds[p][1])

    def draw_points(self, points, style="points", width=3, color=(255, 255, 255)):
        """функция отрисовки точек на экране"""
        if style == "line":
            for p_n in range(-1, len(points) - 1):
                pygame.draw.line(gameDisplay, color,
                                 (int(points[p_n][0]), int(points[p_n][1])),
                                 (int(points[p_n + 1][0]), int(points[p_n + 1][1])), width)

        elif style == "points":
            for p in points:
                pygame.draw.circle(gameDisplay, color,
                                   (int(p[0]), int(p[1])), width)


class Knot(Polyline):
    def __init__(self, count):
        super().__init__()
        self.count = count

    def add_point(self, point, speed):
        super().add_point(point, speed)
        return self.get_knot()

    def set_points(self):
        super().set_points()
        return self.get_knot()

    @staticmethod
    def get_point(points, alpha, deg=None):
        if deg is None:
            deg = len(points) - 1

        if deg == 0:
            return points[0]

        point = Knot.get_point(points, alpha, deg - 1) \
                * (1 - alpha)

        return (points[deg] * alpha) + point

    @staticmethod
    def get_points(base_points, count):
        alpha = 1 / count
        res = []

        for i in range(count):
            res.append(Knot.get_point(base_points, i * alpha))

        return res

    def get_knot(self):
        if len(points) < 3:
            return []

        res = []

        for i in range(-2, len(points) - 2):
            ptn = []
            ptn.append((points[i] + points[i + 1]) * 0.5)
            ptn.append(points[i + 1])
            ptn.append((points[i + 1] + points[i + 2]) * 0.5)
            res.extend(self.get_points(ptn, self.count))

        return res


# =======================================================================================
# Функции для работы с векторами
# =======================================================================================
#
# def sub(x, y):
#     """"возвращает разность двух векторов"""
#     return x[0] - y[0], x[1] - y[1]
#
#
# def add(x, y):
#     """возвращает сумму двух векторов"""
#     return x[0] + y[0], x[1] + y[1]
#
#
# def length(x):
#     """возвращает длину вектора"""
#     return math.sqrt(x[0] * x[0] + x[1] * x[1])
#
#
# def mul(v, k):
#     """возвращает произведение вектора на число"""
#     return v[0] * k, v[1] * k
#
#
# def vec(x, y):
#     """возвращает пару координат, определяющих вектор (координаты точки конца вектора),
#     координаты начальной точки вектора совпадают с началом системы координат (0, 0)"""
#     return sub(y, x)


# =======================================================================================
# Функции отрисовки
# =======================================================================================


def draw_help():
    """функция отрисовки экрана справки программы"""
    gameDisplay.fill((50, 50, 50))
    font1 = pygame.font.SysFont("courier", 24)
    font2 = pygame.font.SysFont("serif", 24)
    data = []
    data.append(["F1", "Show Help"])
    data.append(["R", "Restart"])
    data.append(["P", "Pause/Play"])
    data.append(["Num+", "More points"])
    data.append(["Num-", "Less points"])
    data.append(["", ""])
    data.append([str(steps), "Current points"])

    pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
        (0, 0), (800, 0), (800, 600), (0, 600)], 5)
    for i, text in enumerate(data):
        gameDisplay.blit(font1.render(
            text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
        gameDisplay.blit(font2.render(
            text[1], True, (128, 128, 255)), (200, 100 + 30 * i))


# =======================================================================================
# Основная программа
# =======================================================================================
if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    steps = 35
    working = True
    polyline = Polyline()
    knot = Knot(steps)
    show_help = False
    pause = True

    hue = 0
    color = pygame.Color(0)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    points = []
                    speeds = []
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    steps += 1
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    steps -= 1 if steps > 1 else 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                points.append(event.pos)
                speeds.append((random.random() * 2, random.random() * 2))

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        # draw_points(points)
        polyline.draw_points()
        # draw_points(get_knot(points, steps), "line", 3, color)
        knot.draw_points("line", 3, color)

        if not pause:
            # set_points(points, speeds)
            polyline.set_points()
            knot.set_points()
        if show_help:
            draw_help()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
