#!/bin/env python
# -*- coding: utf-8 -*-
"""
PJP - cvičení číslo 2
"""

import math

Point = tuple[float, float]

def ccw(point_a: Point, point_b: Point, point_c: Point):
    ''' Counterclockwise Turn funkce, která pro "cestu" a -> b -> c:
        - Vrací 1, pokud body tvoří úhel proti směru hodinových ručiček
        - Vrací -1, pokud body tvoří úhel ve směru hodinovývých ručiček
        - Vrací 0, pokud jsou kolineární

        Přejato z Pricetonské univerzity (13.3.2023): https://algs4.cs.princeton.edu/91primitives/
    '''

    # U týhle funkce to může být o držku kvůli přesnosti desetinných čísel,
    # resp. nula nemusí být vždy nula, spíš nějaké okolí nuly
    cross_product_item_1 = (point_b[0] - point_a[0]) * (point_c[1] - point_a[1])
    cross_product_item_2 = (point_c[0] - point_a[0]) * (point_b[1] - point_a[1])

    return cross_product_item_1 - cross_product_item_2

def polar(origin: Point, destination: Point):
    ''' Funkce pro výpočet úhlu mezi dvěma body
    '''
    return math.atan2(destination[1] - origin[1], destination[0] - origin[0] ) * ( 180 / math.pi )

def remove_point(point: Point, list_of_points: list[Point]):
    ''' Funkce odstraní bod ze seznamu bodů'''
    return list(filter(lambda p: p != point, list_of_points))

def angle_from(origin, list_of_points):
    '''Funkce vypočítá úhel přímky procházející dvěma body'''
    return list(map(lambda p: (p[0], p[1], polar(origin, p)), list_of_points))

def is_convex(point_a: Point, point_b: Point, point_c: Point, point_d: Point):
    """
    Druhým úkolem je vytvořit funkci, která ze čtyř zadaných bodů určí, 
    zda tvoří konvexní čtyřúhelník.
    
    Body na vstupu jsou zadávány jako tuple (x, y) kde x a y mohou být
    libovolná reálná čísla, tedy i záporná. Body mohou vytvořit čtyřúhelník,
    ale není to pravidlem.

    Je potřeba aby funkce hlídala i extrémní situace, jako například,
    že body čtyřúhelník vůbec nevytváří. 
    """

    # Ošetření duplicitních bodů
    if len(set([point_a, point_b, point_c, point_d])) != 4:
        print("Není čtyřúhelník ffs")
        return False

    # Výpočet konvexního obalu
    # https://en.wikipedia.org/wiki/Graham_scan
    points = [point_a, point_b, point_c, point_d]

    lowest_y = min(map(lambda p: p[1], points))
    lowest_point = list(filter(lambda p: p[1] == lowest_y, points))

    # Ošetření, pokud máme více bodů se stejným nejnižším y
    if len(lowest_point) != 1:
        lowest_x = min(map(lambda p: p[0], lowest_point))
        lowest_point = [(lowest_x, lowest_y)]


    lowest_point = lowest_point.pop()

    # Seřazení bodů tak, aby vyhovovaly algoritmu
    vertices = angle_from(lowest_point, remove_point(lowest_point, points))
    sorted_by_angle = sorted(vertices, key = lambda x: x[2])

    for index in range(2, len(sorted_by_angle)):
        point_1 = sorted_by_angle[index - 2]
        point_2 = sorted_by_angle[index - 1]
        point_3 = sorted_by_angle[index]
        convexity = ccw(point_1, point_2, point_3)
        if convexity <= 0:
            return False

    return True

if __name__ == '__main__':
    print(is_convex((0.0, 0.0), (1.1, 0.1), (0.9, 0.8), (0.1, 0.9)))
