# -*- coding: utf8 -*-
"""
Zakladni sablona pro prvni cviceni
"""

def triangle(strana_a: float, strana_b: float, strana_c: float):
    """
    Funkce vrací True nebo False, podle toho zda strany a, b, c mohou tvořit
    pravoúhlý trojúhelník

    Pro jednoduchost můžete předpokládat, že strany a, b jsou odvěsny, c je přepona. 
    Tak jako je to ve známé matematické poučce. 
    """

    if any(map(lambda x: x <= 0, [strana_a, strana_b, strana_c])):
        return False

    return strana_a ** 2 + strana_b ** 2 == strana_c ** 2
