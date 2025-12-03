import csv
import os
from datetime import datetime
from collections import defaultdict

from data_structs import Team, Match
from bst import BST
from avl import AVL
from sorting import merge_sort, insertion_sort


# -----------------------------------------------------
# ETAPA 2 — LEITURA DO CSV EM ESTRUTURAS DE DADOS
# -----------------------------------------------------
def read_matches(path):
    matches = []

    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            # filtragem simples
            if not row["date"] or not row["home_team"] or not row["away_team"]:
                continue

            date = datetime.strptime(row["date"], "%Y-%m-%d")
            home = Team(row["home_team"], int(row["home_score"]))
            away = Team(row["away_team"], int(row["away_score"]))

            m = Match(
                date=date,
                home_team=home,
                away_team=away,
                tournament=row["tournament"],
                city=row["city"],
                country=row["country"],
                neutral=row["neutral"].upper() == "TRUE"
            )

            matches.append(m)

    return matches


# -----------------------------------------------------
# CALCULA GOLS POR SELEÇÃO
# -----------------------------------------------------
def get_goals(matches):
    goals = defaultdict(int)
    for m in matches:
        goals[m.home_team.name] += m.home_team.score
        goals[m.away_team.name] += m.away_team.score
    return list(goals.items())  # [(time, gols)]


# -----------------------------------------------------
# CALCULA PONTOS POR SELEÇÃO
# -----------------------------------------------------
def get_points(matches):
    pts = defaultdict(int)
    for m in matches:
        if m.home_team.score > m.away_team.score:
            pts[m.home_team.name] += 3
        elif m.home_team.score < m.away_team.score:
            pts[m.away_team.name] += 3
        else:
            pts[m.home_team.name] += 1
            pts[m.away_team.name] += 1
    return list(pts.items())


# -----------------------------------------------------
# ETAPA 6 — GERA CSV matches_summary.csv
# -----------------------------------------------------
def save_summary(matches):
    os.makedirs("../output", exist_ok=True)
    out = "../output/matches_summary.csv"

    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["year", "country", "home_team", "away_team", "score"])
        for m in matches:
            w.writerow(m.to_list())

    print("Arquivo gerado:", out)


# -----------------------------------------------------
# MAIN — EXECUTA TODAS AS ETAPAS
# -----------------------------------------------------
def main():
    matches = read_matches("../data/results.csv")
    print("Total de partidas lidas:", len(matches))

    # Etapa 6
    save_summary(matches)

    # Etapa 3 — BSTs
    goals = get_goals(matches)

    bst_name = BST()
    for team, g in goals:
        bst_name.insert(team, g)

    print("\nBST ordenada por nome (primeiros 10):")
    print(bst_name.inorder()[:10])

    # BST ordenada por gols
    bst_goals = BST()
    for team, g in goals:
        bst_goals.insert(g, team)

    print("\nBST ordenada por gols (últimos 10):")
    print(bst_goals.inorder()[-10:])

    # Etapa 4 — Ordenação
    pts = get_points(matches)

    ordenado_merge = merge_sort(pts, key=lambda x: x[1])
    ordenado_merge.reverse()

    print("\nTop 10 por pontos (Merge Sort):")
    print(ordenado_merge[:10])

    ordenado_insert = insertion_sort(pts, key=lambda x: x[1])
    ordenado_insert.reverse()

    print("\nTop 10 por pontos (Insertion Sort):")
    print(ordenado_insert[:10])

    # Etapa 5 — AVL por pontos
    avl = AVL()
    for team, p in ordenado_merge:
        avl.insert(p, team)

    print("\nAltura da AVL:", avl.height())


if __name__ == "__main__":
    main()