# -*- coding: utf8 -*-
"""
Zakladni sablona pro prvni cviceni
"""

def triangle(a: float, b: float, c: float):
    """
    Funkce vrací True nebo False, podle toho zda strany a, b, c mohou tvořit
    pravoúhlý trojúhelník

    Pro jednoduchost můžete předpokládat, že strany a, b jsou odvěsny, c je přepona. 
    Tak jako je to ve známé matematické poučce. 
    """

    if any(map(lambda x: x <= 0, [a, b, c])): return False

    return a ** 2 + b ** 2 == c ** 2