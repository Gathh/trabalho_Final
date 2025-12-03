import csv
import os
from datetime import datetime
from collections import defaultdict

from bst import BST
from avl import AVL
from sorting import merge_sort


class Match:
    def __init__(self, date, home, away, home_g, away_g, country):
        self.date = date
        self.home = home
        self.away = away
        self.home_g = int(home_g)
        self.away_g = int(away_g)
        self.country = country

    def to_row(self):
        return [
            self.date.year,
            self.country,
            self.home,
            self.away,
            f"{self.home_g}-{self.away_g}"
        ]


def read_matches(path):
    matches = []

    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            # filtro simples de linhas inválidas (pode explicar no relatório)
            if not row["date"] or not row["home_team"] or not row["away_team"]:
                continue

            date = datetime.strptime(row["date"], "%Y-%m-%d")
            home = row["home_team"]
            away = row["away_team"]
            home_g = int(row["home_score"])
            away_g = int(row["away_score"])
            country = row["country"]

            matches.append(
                Match(date, home, away, home_g, away_g, country)
            )

    return matches


def save_summary(matches, output_path="output/matches_summary.csv"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["year", "country", "home_team", "away_team", "score"])
        for m in matches:
            w.writerow(m.to_row())


def calc_goals(matches):
    goals = defaultdict(int)
    for m in matches:
        goals[m.home] += m.home_g
        goals[m.away] += m.away_g
    return list(goals.items())


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
    return list(pts.items())


def main():
    matches = read_matches("../data/results.csv")
    print("Total de partidas lidas:", len(matches))

    # ETAPA 6 - Geração do CSV de resumo
    save_summary(matches)
    print("Arquivo output/matches_summary.csv gerado!")

    # BST por nome
    goals = calc_goals(matches)
    bst_name = BST()
    for team, total in goals:
        bst_name.insert(team, total)
    print("\nBST por nome:", bst_name.inorder()[:10])

    # BST por gols
    bst_goals = BST()
    for team, total in goals:
        bst_goals.insert(total, team)
    print("\nBST por gols (top 10):", bst_goals.inorder()[-10:])

    # Ranking por pontos
    pts = calc_points(matches)
    ranking = merge_sort(pts, key=lambda x: x[1])
    ranking.reverse()
    print("\nTop 10 por pontos:", ranking[:10])

    # AVL
    avl = AVL()
    for team, p in pts:
        avl.insert(p, team)

    print("\nAltura da AVL:", avl.height())


if __name__ == "__main__":
    main()