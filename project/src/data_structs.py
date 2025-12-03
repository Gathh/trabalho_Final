from dataclasses import dataclass
from datetime import datetime

@dataclass
class Team:
    name: str
    score: int   # gols marcados na partida


@dataclass
class Match:
    date: datetime
    home_team: Team
    away_team: Team
    tournament: str
    city: str
    country: str
    neutral: bool

    def total_goals(self) -> int:
        return self.home_team.score + self.away_team.score

    def to_list(self) -> list:
        """
        Retorna linha formatada para o CSV final matches_summary.csv.
        """
        return [
            self.date.year,
            self.country,
            self.home_team.name,
            self.away_team.name,
            f"{self.home_team.score}-{self.away_team.score}"
        ]