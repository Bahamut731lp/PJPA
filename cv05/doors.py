""" 
    Úkol 5. 
    Napište program, který načte soubor large.txt a pro každé dveře vyhodnotí,
    zda je možné je otevřít nebo ne. Tedy vyhodnotí, zda lze danou množinu uspořádat
    požadovaným způsobem. Výstup z programu uložte do souboru vysledky.txt ve
    formátu 1 výsledek =  1 řádek. Na řádek napište vždy počet slov v množině a True
    nebo False, podle toho, zda řešení existuje nebo neexistuje. 

    Podrobnější zadání včetně příkladu je jako obvykle na elearning.tul.cz
"""
# -*- coding: utf-8 -*-
import os

def construct_vertex_weights(words):
    """
        Funkce pro vytvoření slovníku písmen s počtem výskytů na začátku a na konci slova.
    """

    dictionary = {}

    for word in words:
        safe_word = word.strip()

        leading_letter = safe_word[0]
        trailing_letter = safe_word[-1]

        if leading_letter not in dictionary:
            dictionary[leading_letter] = [0, 0]
        if trailing_letter not in dictionary:
            dictionary[trailing_letter] = [0, 0]

        dictionary[leading_letter][0] += 1
        dictionary[trailing_letter][1] += 1

    return dictionary

def is_eulerian_path(dictionary: dict):
    """
        Funkce pro analyzování textového dokumentu a vytvoření slovního řetězu
        podle pravidel slovního fotbalu.
    """

    # https://math.stackexchange.com/questions/1871065/euler-path-for-directed-graph
    # A directed graph has an Eulerian path if and only if the following conditions are satisfied:
    # At most one vertex in the graph has out-degree = 1 + in-degree,
    # and at most one vertex in the graph has in-degree = 1 + out-degree.
    # All the remaining vertices have in-degree == out-degree.

    found_dominant_out = False
    found_dominant_in = False

    for degrees in dictionary.values():
        in_degree, out_degree = degrees

        if abs(in_degree - out_degree) == 1:
            if found_dominant_out is False and in_degree + 1 == out_degree:
                found_dominant_out = True
            elif found_dominant_in is False and out_degree + 1 == in_degree:
                found_dominant_in = True
            else:
                return False
        elif in_degree == out_degree:
            continue
        else:
            return False

    return True

def find_solution(file_path: str):
    """
        Funkce pro analyzování textového dokumentu a vytvoření slovního řetězu
        podle pravidel slovního fotbalu.
    """
    if not os.path.isfile(file_path):
        return False

    radky = []
    with open(file_path, "r", encoding="utf-8") as soubor:
        radky = soubor.readlines()

    pocet_dveri = int(radky.pop(0))
    vysledky = []

    for _ in range(pocet_dveri):
        pocet_slov = int(radky.pop(0))
        slova = radky[slice(pocet_slov)]
        del radky[slice(pocet_slov)]

        slovnik = construct_vertex_weights(slova)
        vysledek = is_eulerian_path(slovnik)
        vysledky.append(f'{pocet_slov} {vysledek}')

    with open("./vysledky.txt", "w", encoding="utf-8") as soubor_vysledky:
        soubor_vysledky.write("\n".join(vysledky))

    return None

if __name__ == '__main__':
    find_solution("./large.txt")
