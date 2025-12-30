import argparse


DATA = [
    {"user": "alice", "team": "alpha", "role": "api", "active": True},
    {"user": "bob", "team": "alpha", "role": "api", "active": False},
    {"user": "cory", "team": "beta", "role": "web", "active": True},
    {"user": "dana", "team": "beta", "role": "web", "active": True},
    {"user": "erin", "team": "gamma", "role": "ops", "active": True},
]


def _parse_filter(expr: str) -> dict:
    if not expr or "=" not in expr:
        return {}
    key, value = expr.split("=", 1)
    return {key.strip(): value.strip()}


def _filter_rows(rows, expr: str):
    criteria = _parse_filter(expr)
    if not criteria:
        return rows
    key, value = next(iter(criteria.items()))
    return [row for row in rows if str(row.get(key)) == value]


def _filter_by_team(rows, team: str):
    return [row for row in rows if row.get("team") == team]


def calculate_percentage(rows, team: str) -> float:
    team_rows = _filter_by_team(rows, team)
    numerator_rows = [row for row in team_rows if row.get("active") is True]
    denominator_rows = team_rows
    numerator = len(numerator_rows)
    denominator = len(denominator_rows)
    if denominator == 0:
        raise ValueError(f"Invalid team argument: '{team}' not found in data")
    return (numerator / denominator) * 100


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute a filtered percentage.")
    parser.add_argument("--team", default="alpha", help="Team name, e.g. alpha")
    args = parser.parse_args()

    percentage = calculate_percentage(DATA, args.team)
    print(
        f"percentage(team={args.team}) = {percentage:.2f}%"
    )


if __name__ == "__main__":
    main()
