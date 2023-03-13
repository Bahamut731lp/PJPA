# -*- coding: utf-8 -*-

"""
Py.test testy pro quad module

Pokud máte nainstalovaný program PyTest stačí ho spustit v adresáři s testem
příkazem py.test 

PyTest si sám najde testy a postará se o jejich provedení.

PyTest si můžete nainstalovat přes pip a je také součástí distribuce Anaconda
"""

import quad

def test_convex_is_true():
    """
    Test convex quad
    """
    assert quad.is_convex((0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0)) == True

def test_another_convex_is_true():
    """
    Test another convex quad
    """
    assert quad.is_convex((-1.0, -1.0), (1.0, -1.0), (1.0, 1.0), (-1.0, 1.0)) == True

def test_deformed_convex_is_true():
    """
    Test deformed convex quad
    """
    assert quad.is_convex((0.0, 0.0), (1.1, 0.1), (0.9, 0.8), (0.1, 0.9)) == True

def test_non_convex_0_is_false():
    """
    Test non-convex quad
    """
    assert quad.is_convex((0.0, 0.0), (1.0, 0.0), (0.3, 0.3), (0.0, 1.0)) == False

def test_non_convex_0_is_false():
    """
    Test non-convex quad
    """
    assert quad.is_convex((0.0, 0.0), (0.2, 0.7), (1.0, 1.0), (0.0, 1.0)) == False

def test_non_convex_2_is_false():
    """
    Test rotated non-convex quad
    """
    assert quad.is_convex((0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.7, 0.3)) == False

def test_non_convex_3_is_false():
    """
    Test non-convex quad
    """
    assert quad.is_convex((0.7, 0.8), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0)) == False

def test_triangle_is_false():
    """
    Test triangle does not pass
    """
    assert quad.is_convex((0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 0.0)) == False

def test_line_is_false():
    """
    Test line does not pass
    """
    assert quad.is_convex((0.0, 0.0), (1.0, 0.0), (1.0, 0.0), (0.0, 0.0)) == False

def test_point_is_false():
    """
    Test point does not pass
    """
    assert quad.is_convex((1.0, 0.0), (1.0, 0.0), (1.0, 0.0), (1.0, 0.0)) == False
