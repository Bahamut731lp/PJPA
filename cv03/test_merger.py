# -*- coding: utf-8 -*-
"""
Py.test testy pro merger module

Pokud máte nainstalovaný program PyTest stačí ho spustit v adresáři s testem
příkazem py.test

PyTest si sám najde testy a postará se o jejich provedení.

PyTest si můžete nainstalovat přes pip a je také součástí distribuce Anaconda
"""

import merger


def test_merge_tuples():
    """
    test pro vyslednou funkci merge tuples
    """
    line_a = ((1, 3), (3, 4), (10, 2))
    line_b = ((1, 2), (2, 4), (5, 2))
    line_c = ((1, 5), (3, 2), (7, 3))

    expected_result = {1: [3, 2, 5],
                       2: [0, 4, 0],
                       3: [4, 0, 2],
                       5: [0, 2, 0],
                       7: [0, 0, 3],
                       10: [2, 0, 0]}

    assert expected_result == merger.merge_tuples(line_a, line_b, line_c)
