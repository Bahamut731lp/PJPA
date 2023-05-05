"""
Testy pro modul card a třídu Card ze cvičení 8.

Ke spuštění je potřeba modul pytest

https://docs.pytest.org/en/latest/

pip install pytest
"""

import card
import pytest


@pytest.mark.parametrize('rank, suit', [
    (1, "s"),
    (18, "s"),
    (5, "x"),
    (17, "x"),
])
def test_bad_card_raises(rank, suit):
    """
    Pokud karta vytvořit nejde - například proto, že je špatná barva či hodnota,
    musí třída vyhodit výjimku TypeError.
    """

    with pytest.raises(TypeError):
        card.Card(rank, suit)


def test_rank():
    """
    Test metody vracejici hodnost karty
    """
    t_card = card.Card(3, "s")
    result = 3
    assert result == t_card.rank


def test_suit():
    """
    Test metody vracejici barvu karty
    """
    t_card = card.Card(3, "t")
    result = "t"
    assert result == t_card.suit


@pytest.mark.parametrize('rank, suit, expected', [
    (3, "s", 3),
    (5, "t", 5),
    (10, "s", 10),
    (11, "s", 10),
    (12, "s", 10),
    (13, "s", 10),
    (14, "s", 11)
])
def test_black_jack_rank(rank, suit, expected):
    """
    Test metody vracejici hodnotu karty dle pravidel pro Black Jack
    """
    t_card = card.Card(rank, suit)
    assert expected == t_card.black_jack_rank()


@pytest.mark.parametrize('rank, suit, expected', [
    (3, "s", "srdcová trojka"),
    (10, "s", "srdcová desítka"),
    (11, "s", "srdcový spodek"),
    (12, "s", "srdcová královna"),
    (13, "s", "srdcový král"),
    (14, "s", "srdcové eso")
])
def test_str(rank, suit, expected):
    """
    Test metody pro vypis karty 
    """
    t_card = card.Card(rank, suit)

    assert expected == str(t_card)


@pytest.mark.parametrize('rank, suit', [
    (3, "s"),
    (7, "t"),
    (10, "s"),
    (14, "k")
])
def test_card_equals(rank, suit):
    """
    Test porovnani, karty jsou si rovny
    """
    t_card1 = card.Card(rank, suit)
    t_card2 = card.Card(rank, suit)
    assert t_card1 == t_card2


def test_greater_then():
    """
    Test porovnani, prvni karta je větší než druhá
    """
    t_card1 = card.Card(3, "s")
    t_card2 = card.Card(2, "k")
    assert t_card1 > t_card2


def test_less_then():
    """
    Test porovnání, první karta je menší než druhá
    """
    t_card1 = card.Card(2, "s")
    t_card2 = card.Card(5, "k")
    assert t_card1 < t_card2


@pytest.mark.parametrize('rank, suit, expected', [
    (3, "s", True),
    (7, "t", True),
    (10, "s", False)
])
def test_less_equal_then(rank, suit, expected):
    """
    Test porovnání, první karta je menší nebo rovna než druhá
    """
    t_card1 = card.Card(rank, suit)
    t_card2 = card.Card(7, "s")
    assert (t_card1 <= t_card2) == expected


@pytest.mark.parametrize('rank, suit, expected', [
    (3, "s", False),
    (7, "t", True),
    (10, "s", True)
])
def test_greater_equal_then(rank, suit, expected):
    """
    Test porovnání, první karta je větší nebo rovna než druhá
    """
    t_card1 = card.Card(rank, suit)
    t_card2 = card.Card(7, "s")
    assert (t_card1 >= t_card2) == expected
