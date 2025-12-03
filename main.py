import csv
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
    # dict com chave: (date, home_team, away_team)
    grouped = defaultdict(lambda: {"home_g": 0, "away_g": 0, "country": ""})

    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            date = row["date"]
            home = row["home_team"]
            away = row["away_team"]
            scoring_team = row["team"]  # time que fez o gol

            key = (date, home, away)

            # país = "home_team" normalmente, mas não tem no arquivo
            grouped[key]["country"] = home

            if scoring_team == home:
                grouped[key]["home_g"] += 1
            elif scoring_team == away:
                grouped[key]["away_g"] += 1

    matches = []
    for (date, home, away), info in grouped.items():
        matches.append(
            Match(
                datetime.strptime(date, "%Y-%m-%d"),
                home,
                away,
                info["home_g"],
                info["away_g"],
                info["country"]
            )
        )

    return matches


def save_summary(matches):
    with open("matches_summary.csv", "w", newline="", encoding="utf-8") as f:
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
    matches = read_matches("goalscorers.csv")
    print("Total de partidas reconstruídas:", len(matches))

    save_summary(matches)
    print("Arquivo matches_summary.csv gerado!")

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


main()