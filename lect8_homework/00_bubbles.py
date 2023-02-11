# -*- coding: utf-8 -*-

import simple_draw as sd
from typing import Tuple

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
for i in range(3):
    sd.circle(sd.Point(100, 500), 5 + i * 5)


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def draw_bubbles(point: Tuple[int, int], step: int = 0, qty: int = 1) -> None:
    for i in range(qty):
        sd.circle(sd.Point(point[0], point[1]), 30+(step*i), sd.COLOR_BLUE,)


draw_bubbles((400, 500), 20, 3)

# Нарисовать 10 пузырьков в ряд
for i in range(10):
    sd.circle(sd.Point(100 + i * 100, 400), 15, sd.COLOR_GREEN)

# Нарисовать три ряда по 10 пузырьков
for row in range(3):
    for col in range(10):
        sd.circle(sd.Point(100 + col * 30, 200 + row * 50), 10, sd.COLOR_DARK_ORANGE)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for i in range(100):
    sd.circle(sd.random_point(), 2, sd.random_color())

sd.pause()
