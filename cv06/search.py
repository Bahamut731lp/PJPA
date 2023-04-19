# -*- coding: utf-8 -*-

""" 
Úkol 6.
Vaším dnešním úkolem je vytvořit program, který o zadaném textu zjistí některé
údaje a vypíše je na standardní výstup. Hlavním smyslem cvičení je procvičit
si práci s regulárními výrazy, takže pro plný bodový zisk je nutné použít k
řešení právě tento nástroj.

Program musí pracovat s obecným textem, který bude zadaný v souboru. Jméno
souboru bude zadáno jako vstupní parametr funkce main, která by měla být
vstupním bodem programu. Samozřejmě, že funkce main by neměla řešit problém
kompletně a měli byste si vytvořit další pomocné funkce. Můžete předpokládat,
že soubor bude mít vždy kódování utf-8 a že bude psaný anglicky, tedy jen
pomocí ASCII písmen, bez české (či jiné) diakritiky. 

Konkrétně musí program zjistit a vypsat:

1. Počet slov, která obsahují nejméně dvě samohlásky (aeiou) za sebou. Například
slovo bear.

2. Počet slov, která obsahují alespoň tři samohlásky - například slovo atomic.

3. Počet slov, která mají šest a více znaků - například slovo terrible.

4. Počet řádků, které obsahují nějaké slovo dvakrát. 

Podrobnější zadání včetně příkladu je jako obvykle na elearning.tul.cz
"""

import os
import re

regex_two_vowels = re.compile(r"[aeiyou]{2}",  re.IGNORECASE)
regex_three_vowels = re.compile(r"[aeiyou]", re.IGNORECASE)
regex_six_characters = re.compile(r".{6}", re.IGNORECASE)
regex_duplicate_words = re.compile(r"\b(\w+)\b(.*)\b\1\b", re.IGNORECASE)

def match_regexes(word: str, counter: dict):
    """
    Funkce najde hledané patterny ve slově
    """

    if word.strip() == "":
        pass

    two_vowels_result = regex_two_vowels.search(word)
    if two_vowels_result is not None:
        counter["two_vowels"] += 1

    three_vowels_result = regex_three_vowels.findall(word)
    if len(three_vowels_result) >= 3:
        counter["three_vowels"] += 1

    six_characters_result = regex_six_characters.search(word)
    if six_characters_result is not None:
        counter["six_characters"] += 1

def create_counter():
    """
    Funkce pro vytvoření čítače výsledků
    """
    return {
        "two_vowels": 0,
        "three_vowels": 0,
        "six_characters": 0,
        "duplicates_in_line": 0
    }

def main(file_name: str):
    """
    zpracujte soubor 
    """

    if not os.path.isfile(file_name):
        pass

    counter = create_counter()

    with open(file_name, "r", encoding="utf-8") as file:
        rows = file.readlines()
        # Ošetření new-line znaků a rozdělení podle mezery
        rows = list(map(lambda row: row.strip(), rows))
        for radek in rows:
            has_duplicates = regex_duplicate_words.search(radek)
            if has_duplicates is not None:
                counter["duplicates_in_line"] += 1

        rows = list(map(lambda x: x.split(" "), rows))
        # Z pole polí uděláme pole stringů

        words = set({re.sub(r"[^A-Za-z]+", '', word.lower()) for words in rows for word in words})
        words = list(words)

        for word in words:
            match_regexes(word, counter)

    for _, value in counter.items():
        print(value)


if __name__ == '__main__':
    main('cv06_test.txt')
