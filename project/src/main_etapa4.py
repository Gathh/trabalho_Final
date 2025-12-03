import csv
from datetime import datetime
from collections import defaultdict

from sorting import merge_sort, insertion_sort


# ---------------------------
# MODELO DE PARTIDA
# ---------------------------
class Match:
    def __init__(self, date, home, away, home_g, away_g):
        self.date = date
        self.home = home
        self.away = away
        self.home_g = int(home_g)
        self.away_g = int(away_g)


# ---------------------------
# RECONSTRÓI AS PARTIDAS
# ---------------------------
def read_matches(path):
    grouped = defaultdict(lambda: {"home_g": 0, "away_g": 0})

    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            date = row["date"]
            home = row["home_team"]
            away = row["away_team"]
            scorer_team = row["team"]

            key = (date, home, away)

            if scorer_team == home:
                grouped[key]["home_g"] += 1
            elif scorer_team == away:
                grouped[key]["away_g"] += 1

    matches = []
    for (date, home, away), info in grouped.items():
        matches.append(
            Match(
                datetime.strptime(date, "%Y-%m-%d"),
                home, away,
                info["home_g"], info["away_g"]
            )
        )

    return matches


# ---------------------------
# CALCULA OS PONTOS
# ---------------------------
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


# ---------------------------
# MAIN ETAPA 4
# ---------------------------
def main():
    matches = read_matches("goalscorers.csv")
    pts = calc_points(matches)

    # Merge Sort (O(n log n))
    ordenado_merge = merge_sort(pts, key=lambda x: x[1])
    ordenado_merge.reverse()

    # Insertion Sort (O(n²))
    ordenado_insert = insertion_sort(pts, key=lambda x: x[1])
    ordenado_insert.reverse()

    print("\n=== ETAPA 4: ORDENANDO POR PONTOS ===")

    print("\nTop 10 (Merge Sort):")
    print(ordenado_merge[:10])

    print("\nBottom 10 (Merge Sort):")
    print(ordenado_merge[-10:])

    print("\nTop 10 (Insertion Sort):")
    print(ordenado_insert[:10])

    print("\nBottom 10 (Insertion Sort):")
    print(ordenado_insert[-10:])


if __name__ == "__main__":
    main()