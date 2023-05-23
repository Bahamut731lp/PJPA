"""
Implementujte program dle zadání úlohy 9. na elearning.tul.cz

Vytvořte program, který prohledá zadaný textový
soubor a nejde v něm řádky, na kterých se vyskytuje hledaný vzor. Případně více
vzorů. Tyto řádky pak vypíše na obrazovku a přidat k ním jejich čísla v původním
souboru. 

Tak trochu se toto chování podobá unixovému příkazu grep, přesněji
řečeno grep -n.  Ten můžete případně použít pro kontrolu. Nicméně váš program
toho bude umět v mnoha ohledech méně a v jednom více (vyhledávání více vzorů
najednou). Nejde tedy o to vytvářet 100% kopii příkazu grep.

Program musí jít  ovládat z příkazové řádky. Základním parametrem zadávaným
vždy, je jméno souboru. Pokud jméno souboru není zadané program nemůže pracovat
a měl by v takovém případě zobrazit nápovědu.

Druhý parametr  parametr -s --search bude volitelný. Může být následován
libovolným počtem n slov. Samozřejmě, pokud je tam parametr -s musí tam být to
slovo alespoň jedno (tedy n >= 1).  Pokud není zadané hledané slovo, musí
program opět vypsat chybu nebo nápovědu.
 """

import argparse
import os
from pathlib import Path

parser = argparse.ArgumentParser(
    prog='Hledac',
    description='Unixový GREP z Wishe.',
    exit_on_error=False
)
parser.add_argument("-f", "--filename", help="Jméno souboru k analýze")
parser.add_argument("-s", "--search", action="extend",
                    nargs="+", help="Hledané výrazy")


def readfile(filepath: Path):
    """
        Funkce pro přečtení souboru
    """

    if not os.path.isfile(filepath):
        return []

    with open(filepath, encoding="utf-8") as filehandle:
        lines = filehandle.readlines()
        return lines


def number_them_lines(lines: list[str]):
    """
        Funkce pro očíslování řádků seznamu
    """
    return [f"{i + 1}:{x}" for i, x in enumerate(lines)]


def filter_them_lines(lines: list[str], expressions: list[str]):
    """
        Funkce pro vyfiltrování řádků
    """

    return list(filter(lambda line: all(expr in line for expr in expressions), lines))


def main(cli_args = None):
    """
        Hlavní metoda programu
    """

    if cli_args is None:
        cli_args = []
    
    try:
        args = parser.parse_args(cli_args)

        if args.filename is None:
            raise ValueError()

        path_to_file = Path(args.filename)
        contents = readfile(path_to_file)
        numbered = number_them_lines(contents)

        if args.search is None:
            print("".join(numbered))
            return 0
        
        print("".join(filter_them_lines(numbered, args.search)))
        return 1

    except (ValueError, argparse.ArgumentError):
        parser.print_help()
        return -1

if __name__ == '__main__':
    main()
