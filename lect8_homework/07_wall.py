# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

for row in range(10):
    for col in range(30):
        if row % 2 == 0:
            shift = 0
        else:
            shift = -51
        sd.rectangle(sd.Point(col * 102 + shift, row * 52), sd.Point(100 + col * 102 + shift, 50 + row * 52),
                     sd.COLOR_RED)
        sd.rectangle(sd.Point(100 + 102 * col + shift, 52 * row), sd.Point(102 + 102 * col + shift, 52 + 52 * row),
                     sd.COLOR_WHITE)
    sd.rectangle(sd.Point(0, 50 + 52 * row), sd.Point(1000, 52 + 52 * row), sd.COLOR_WHITE)

sd.pause()
