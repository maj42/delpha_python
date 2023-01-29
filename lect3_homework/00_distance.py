#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2



# TODO здесь заполнение словаря

msk = sites['Moscow']
lnd = sites['London']
prs = sites['Paris']

#Растояния
msk_lnd = ((msk[0] - lnd[0]) ** 2 + (msk[1] - lnd[1]) ** 2) ** .5
msk_prs = ((msk[0] - prs[0]) ** 2 + (msk[1] - prs[1]) ** 2) ** .5
lnd_prs = ((lnd[0] - prs[0]) ** 2 + (lnd[1] - prs[1]) ** 2) ** .5

distances = {
    "Мск-лнд": round(msk_lnd),
    "Мск-Париж": round(msk_prs),
    "Лнд-Париж": round(lnd_prs),

}



print(distances)




