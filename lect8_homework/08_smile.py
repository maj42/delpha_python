# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


def draw_smile(coord_x, coord_y, color):
    # Face
    sd.circle(sd.Point(coord_x, coord_y), 50, color, 0)
    # Eyes
    sd.circle(sd.Point(coord_x - 20, coord_y + 10), 10, sd.COLOR_BLACK, 0)
    sd.circle(sd.Point(coord_x + 20, coord_y + 10), 10, sd.COLOR_BLACK, 0)
    # Smile
    for angle in range(200, 330):
        sd.circle(sd.Point(coord_x + sd.cos(angle) * 30, coord_y + sd.sin(angle) * 30), 1, sd.COLOR_BLACK, 0)


for smile in range(10):
    point = sd.random_point()
    draw_smile(point.x, point.y, sd.random_color())

sd.pause()
