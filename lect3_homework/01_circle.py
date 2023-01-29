#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import pi


def check_dot_in_circle(circle_rad: int, point_coord: tuple) -> bool:
    """Checks if dot with 2 coordinates(x, y) is in the circle with a center(0,0).
    Distance formula: sqrt(x**2 + y**2)"""
    distance = (point_coord[0] ** 2 + point_coord[1] ** 2) ** 0.5
    return distance <= circle_rad


# Есть значение радиуса круга
radius = 42

# Выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой
# подсказки:
#       формулу можно подсмотреть в интернете,
#       пи возьмите равным 3.1415926
#       точность указывается в функции round()
circle_area = round(pi * radius ** 2, 4)
print(circle_area)


# Далее, пусть есть координаты точки
point = (23, 34)
# где 23 - координата х, 34 - координата у

# Если точка point лежит внутри того самого круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
# подсказки:
#       нужно определить расстояние от этой точки до начала координат (0, 0)
#       формула так же есть в интернете
#       квадратный корень - это возведение в степень 0.5
#       операции сравнения дают булевы константы True и False
print(check_dot_in_circle(radius, point))

# Аналогично для другой точки
point_2 = (30, 30)
# Если точка point_2 лежит внутри круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
print(check_dot_in_circle(radius, point_2))

# Пример вывода на консоль:
#
# 77777.7777
# False
# False


