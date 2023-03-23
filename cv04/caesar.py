"""
Vytvorte funkce encrypt a decrypt pro Caesarovu sifru.
Kompletni zadani v elearningu.
"""

ASCII_LETTERS = "abcdefghijklmnopqrstuvwxyz"
ALPHABET = list(ASCII_LETTERS)
INDEX_TO_LETTER = dict(enumerate(ALPHABET))
LETTER_TO_INDEX = {v: k for k, v in INDEX_TO_LETTER.items()}

def get_uppercase_mask(string: str):
    """
    Funkce pro konvertování stringu do pole boolů podle toho, zda jsou písmena
    """
    return [i.isupper() for i in string]

def capitalize_by_mask(string: list[str], mask: list[bool]):
    """
    Transformace pole znaků do pole znaků se správnou velikostí písmen

    True = Velké písmeno
    False = Malé písmeno
    """
    return [string[i].upper() if mask[i] else string[i] for i in range(len(string))]

def string_to_indices(string: str):
    """
    Funkce pro převod stringu do pole indexů podle abecedy
    """
    result = []
    # Pylint nemá rád dlouhé list comprehensions... chápu :(
    for letter in string:
        if letter.lower() not in LETTER_TO_INDEX:
            result.append(letter.lower())
            continue

        result.append(LETTER_TO_INDEX[letter.lower()])

    return result

def indices_to_string(array: list):
    """
    Funkce pro převod pole indexů do stringu podle abecedy
    """
    return [INDEX_TO_LETTER[i] if i in INDEX_TO_LETTER else i for i in array]

def offset_indices(indices: list[int], offset: int):
    """
    Funkce pro posunutí indexů v poli o offset.
    Posunutí je cyklické.
    """
    result = []

    for index in indices:
        if not isinstance(index, int):
            result.append(index)
            continue

        new_index = index + offset
        modulo = len(ALPHABET)
        cyclic_index = new_index % modulo

        result.append(cyclic_index)

    return result

def encrypt(word: str, offset: int):
    """
    :param word - slovo k zasifrovani
    :param offset - znakovy posun
    :return: zasifrovane slovo
    """
    uppercase_mask = get_uppercase_mask(word)
    indexes = string_to_indices(word)
    cyphered_indexes = offset_indices(indexes, offset)
    cyphered_letters = indices_to_string(cyphered_indexes)
    uppercases = capitalize_by_mask(cyphered_letters, uppercase_mask)
    print(indexes, cyphered_indexes, uppercases)
    result = "".join(uppercases)

    return result


def decrypt(word: str, offset: int):
    """
    :param word - zasifrovane slovo
    :param offset - znakovy posun
    :return: desifrovane slovo
    """
    uppercase_mask = get_uppercase_mask(word)
    indexes = string_to_indices(word)
    cyphered_indexes = offset_indices(indexes, -1 * offset)
    cyphered_letters = indices_to_string(cyphered_indexes)
    uppercases = capitalize_by_mask(cyphered_letters, uppercase_mask)
    result = "".join(uppercases)

    return result

if __name__ == "__main__":
    print(encrypt("to bolt or not to be", 7))
    print(decrypt("av ivsa vy uva av il", 7))
