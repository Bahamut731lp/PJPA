"""
Cvičení 7. - práce s daty

Vaším dnešním úkolem je spojit dohromady data, uložená ve dvou různých
souborech. První soubor obsahuje výsledky závodu - jména a časy závodníků. Druhý
pak obsahuje databázi závodníků uloženou jako JSON - mimo jiné jejich id. Cílem
je vytvořit  program, který tyto data propojí, tedy ke každému závodníkovi ve
štafetě najde jeho id. Případně také nenajde, data nejsou ideální. I tuto
situaci ale musí program korektně ošetřit.  Výsledky programu bude potřeba
zapsat do dvou souborů.

Kompletní zadání je jako vždy na https://elearning.tul.cz/
"""

import json
import re
from typing import Dict, List, TypedDict
from bs4 import BeautifulSoup

HTML_PATH = "./result.html"
JSON_PATH = "./competitors.json"


class DataStructureType(TypedDict):
    """
        Datový typ uložený v JSON souboru
    """
    id: int
    firstname: str
    lastname: str
    nationality: str
    birth: str
    gender: str


def parse_json():
    """
        Funkce pro preprocessing JSON souboru se závodníky
    """
    record: Dict[str, List[DataStructureType]] = {}

    with open(JSON_PATH, 'r', encoding="utf-8") as json_file:
        data: List[DataStructureType] = json.load(json_file)

        for racer in data:
            if racer.get("lastname") not in record:
                record[racer.get("lastname")] = []

            record[racer.get("lastname")].append(racer)

    return record


def transform_racers(string: str, gender: str) -> List[DataStructureType]:
    """
        Funkce pro parsování řádku výsledků štafety z HTML souboru
    """
    record = []
    rank_delimiter = string.find(")")

    rank = string[slice(0, rank_delimiter)]
    rest = string[slice(rank_delimiter + 1, len(string))].strip()

    country = re.compile(
        "^(.*?)(?=[0-9])", re.IGNORECASE).search(rest).group(0).strip()
    rest = rest[slice(len(country), len(rest))].strip()

    time = re.compile("[0-9]+:[[0-9]+:[0-9]+").search(rest).group(0)
    rest = rest[slice(len(time), len(rest))].strip()

    rest = rest.replace("(", "").replace(")", "").replace(".", "")
    names = [x.strip() for x in rest.split(",")]

    for racer_name in names:
        firstname, *lastname = re.compile(r"\s+").split(racer_name)
        record.append({"firstname": firstname,
                       "lastname": " ".join(lastname),
                       "result": rank,
                       "id": False,
                       "nationality": country,
                       "time": time,
                       "birth": "",
                       "gender": gender
                       })

    return record


def parse_html() -> List[DataStructureType]:
    """
        Funkce pro naparsování HTML souboru
    """
    with open(HTML_PATH, 'r', encoding="utf-8") as html_file:
        content = html_file.read()
        soup = BeautifulSoup(content, 'html.parser')
        relay_header = soup.find(
            'p', text=re.compile('Relay', flags=re.IGNORECASE))
        relay_lines = relay_header.fetchNextSiblings(limit=4)
        gender = None
        racers = []

        for line in relay_lines:
            text = line.text

            if "Women" == text.strip():
                gender = "F"
            elif "Men" == text.strip():
                gender = "M"
            else:
                participants = [x.strip() for x in text.split("),")]
                participants = [transform_racers(
                    x, gender) for x in participants]
                participants = [
                    item for sublist in participants for item in sublist]

                for participant in participants:
                    racers.append(participant)

        return racers


def output_json(result_list):
    """
    Uloží list slovníků do souboru output.json tak jak je požadováno 
    v zadání.
    """

    with open('output.json', 'w', encoding="utf-8") as output:
        output.write(json.dumps(result_list, indent=4, sort_keys=True))


def main():
    """
        Hlavní metoda programu
    """
    json_data = parse_json()
    html_data = parse_html()
    result = []

    for racer in html_data:
        # Víme, že tam je příjmení, ale ještě musíme zjistit, jestli tam je i to jméno
        # (abychom někoho nezapočítali 2x jenom kvůli stejnému příjmení)

        if racer["lastname"] in json_data:
            candidates = json_data.get(racer["lastname"])
            is_in_list = False
            racer_from_db = None

            for candidate in candidates:
                if candidate.get("firstname") == racer.get("firstname"):
                    is_in_list = True
                    racer_from_db = candidate
                    break

            if is_in_list:
                result.append({
                    "id": racer_from_db.get("id"),
                    "result": racer.get("result"),
                    "time": racer.get("time")
                })
            else:
                result.append({
                    "id": False,
                    "result": racer.get("result"),
                    "time": racer.get("time"),
                    "no_match": " ".join([racer.get("firstname"), racer.get("lastname")])
                })
        else:
            result.append({
                "id": False,
                "result": racer.get("result"),
                "time": racer.get("time"),
                "no_match": " ".join([racer.get("firstname"), racer.get("lastname")])
            })

    output_json(result)

    with open('compare.txt', 'w', encoding="utf-8") as compare,\
         open("errors.txt", "w", encoding="utf-8") as errors:

        sorted_results = sorted(result, key=lambda x: x["id"])
        for racer in sorted_results:
            if racer.get("id") is False:
                name = racer.get("no_match")
                errors.write(f"{name}\n")
            else:
                r_id = racer["id"]
                r_res = racer["result"]
                compare.write(f"{r_id} {r_res}\n")

if __name__ == '__main__':
    main()
