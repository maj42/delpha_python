#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from itertools import combinations


def calc_dist(city_1: str, city_2: str, precision=2) -> float:
    """Distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)"""
    return round(((sites[city_1][0] - sites[city_2][0]) ** 2 + (sites[city_1][1] - sites[city_2][1]) ** 2) ** 0.5,
                 precision)


sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480)}

distances = {}

for permutation in combinations(sites.keys(), 2):
    city_first, city_second = permutation
    route = f"{city_first} - {city_second}"
    distances[route] = calc_dist(city_first, city_second)

print(distances)
