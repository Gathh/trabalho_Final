import csv
from datetime import datetime
from collections import defaultdict

from sorting import merge_sort
from avl import AVL


class Match:
    def __init__(self, date, home, away, home_g, away_g):
        self.date = date
        self.home = home
        self.away = away
        self.home_g = home_g
        self.away_g = away_g


def read_matches(path):
    grouped = defaultdict(lambda: {"home_g": 0, "away_g": 0})

    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            date = row["date"]
            home = row["home_team"]
            away = row["away_team"]
            scorer = row["team"]

            key = (date, home, away)

            if scorer == home:
                grouped[key]["home_g"] += 1
            else:
                grouped[key]["away_g"] += 1

    matches = []
    for (date, home, away), info in grouped.items():
        matches.append(
            Match(
                datetime.strptime(date, "%Y-%m-%d"),
                home,
                away,
                info["home_g"],
                info["away_g"]
            )
        )

    return matches


def calc_points(matches):
    pts = defaultdict(int)
    for m in matches:
        if m.home_g > m.away_g:
            pts[m.home] += 3
        elif m.away_g > m.home_g:
            pts[m.away] += 3
        else:
            pts[m.home] += 1
            pts[m.away] += 1
    return list(pts.items())  # [(time, pontos)]


def main():
    # leitura das partidas (reconstruídas a partir de goalscorers.csv)
    matches = read_matches("goalscorers.csv")

    # cálculo de pontos por seleção
    pts = calc_points(matches)

    # lista ordenada por pontos (maior -> menor), reaproveitando a etapa 4
    ranking = merge_sort(pts, key=lambda x: x[1])
    ranking.reverse()

    print("\n=== TOP 10 POR PONTOS ===")
    print(ranking[:10])

    # ============================
    # ETAPA 5 – AVL POR PONTOS
    # ============================
    avl = AVL()

    # insere na AVL usando pontos como chave
    for team, pontos in ranking:
        avl.insert(pontos, team)

    print("\nAVL construída com base nos pontos.")
    print("Altura da AVL:", avl.height())


if __name__ == "__main__":
    main()