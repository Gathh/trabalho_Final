import csv
from datetime import datetime
from data_structs import Team, Match


def load_matches(csv_path="data/results.csv"):
    matches = []

    with open(csv_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            home_team = Team(
                name=row["home_team"],
                score=int(row["home_score"])
            )

            away_team = Team(
                name=row["away_team"],
                score=int(row["away_score"])
            )

            match = Match(
                date=datetime.strptime(row["date"], "%Y-%m-%d"),
                home_team=home_team,
                away_team=away_team,
                tournament=row["tournament"],
                city=row["city"],
                country=row["country"],
                neutral=row["neutral"].lower() == "true"
            )

            matches.append(match)

    return matches


def main():
    matches = load_matches()

    for match in matches:
        print(match.to_list())


if __name__ == "__main__":
    main()
