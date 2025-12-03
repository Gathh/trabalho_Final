import csv
from datetime import datetime
from pathlib import Path
from data_structs import Match, Team

BASE_DIR = Path(__file__).resolve().parent.parent

RESULTS_PATH = BASE_DIR / "data" / "results.csv"

def linha_valida(row: dict) -> bool:
    """Filtra linhas com dados faltantes ou inválidos."""
    campos_obrigatorios = [
        "date", "home_team", "away_team", "home_score", "away_score",
        "tournament", "city", "country", "neutral"
    ]

    # Checar campos vazios
    for campo in campos_obrigatorios:
        if campo not in row or row[campo] is None or row[campo].strip() == "":
            return False

    # Checar se scores são inteiros
    try:
        int(row["home_score"])
        int(row["away_score"])
    except ValueError:
        return False

    return True


def carregar_matches() -> list:
    """Lê o CSV, cria objetos Match e armazena em uma lista."""
    matches = []

    with open(RESULTS_PATH, encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for row in leitor:
            if not linha_valida(row):
                continue

            # converter dados
            date_obj = datetime.strptime(row["date"], "%Y-%m-%d")

            home = Team(
                name=row["home_team"],
                score=int(row["home_score"])
            )

            away = Team(
                name=row["away_team"],
                score=int(row["away_score"])
            )

            match = Match(
                date=date_obj,
                home_team=home,
                away_team=away,
                tournament=row["tournament"],
                city=row["city"],
                country=row["country"],
                neutral=row["neutral"].lower() == "true"
            )

            matches.append(match)

    return matches


def main():
    matches = carregar_matches()

    print("===================================")
    print(f"Total de partidas lidas e válidas: {len(matches)}")
    print("===================================")

    # Retorna para uso em outras etapas (BST, AVL, Sorting...)
    return matches


if __name__ == "__main__":
    main()
