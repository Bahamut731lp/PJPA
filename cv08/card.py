"""
@TODO implementujte dle zadání cvičení 8
"""


class Card:
    """
    Třída pro reprezentaci hracích karet
    """

    def __init__(self, given_rank: int, given_suit: str):
        self.rank = given_rank
        self.suit = given_suit


    @property
    def rank(self):
        """
            Getter pro hodnotu karty
        """
        return self._rank

    @property
    def suit(self):
        """
            Getter pro barvu karty
        """
        return self._suit

    @rank.setter
    def rank(self, value: int):
        """
            Setter pro hodnotu karty
        """

        if value < 2 or value > 14:
            raise TypeError()

        self._rank = value

    @suit.setter
    def suit(self, value: str):
        """
            Setter pro barvu karty
        """

        allowed_values = ["s", "k", "p", "t"]

        if value not in allowed_values:
            raise TypeError()

        self._suit = value

    def black_jack_rank(self):
        """
        Metoda vrací hodnotu karty dle pravidel pro Black Jack
        :return:
        """

        if self.rank <= 10:
            return self.rank

        if self.rank < 14:
            return 10

        return 11

    def __str__(self) -> str:

        # ANO, STAČILO BY AKORÁT MĚNIT KONCOVKY SLOV
        # ALE PAK BY URČITĚ NĚKDO PŘIŠEL, ŽE CHCE VÝJIMKU, A BYLO BY TO V P*ČI
        # TOHLE JE ROZHODNĚ MÉNĚ ELEGANTNÍ, ALE ZASE VÍCE ROZŠÍŘITELNÝ
        numbers = ["dvojka", "trojka", "čtyřka", "pětka", "šestka",
                   "sedmička", "osmička", "devítka", "desítka"]
        declension = {
            "s": {
                "muzsky": "srdcový",
                "zensky": "srdcová",
                "stredni": "srdcové"
            },
            "k": {
                "muzsky": "kárový",
                "zensky": "kárová",
                "stredni": "kárové"
            },
            "p": {
                "muzsky": "pikový",
                "zensky": "piková",
                "stredni": "pikové"
            },
            "t": {
                "muzsky": "trefový",
                "zensky": "trefová",
                "stredni": "trefové"
            }
        }

        if self.rank <= 10:
            return f'{declension[self.suit]["zensky"]} {numbers[self.rank - 2]}'

        higher_ups = [
            ("muzsky", "spodek"),
            ("zensky", "královna"),
            ("muzsky", "král"),
            ("stredni", "eso")
        ]
        higher_up_index = self.rank - 11
        voice, name = higher_ups[higher_up_index]

        return f'{declension[self.suit][voice]} {name}'

    def __lt__(self, other) -> bool:
        return self.black_jack_rank() < other.black_jack_rank()

    def __gt__(self, other) -> bool:
        return self.black_jack_rank() > other.black_jack_rank()

    def __eq__(self, other) -> bool:
        return self.black_jack_rank() == other.black_jack_rank()

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __ge__(self, other) -> bool:
        return self > other or self == other

    def __le__(self, other) -> bool:
        return self < other or self == other


if __name__ == '__main__':
    test = Card(15, "s")
    print(test.rank)
    print(test.suit)
    print(test)
