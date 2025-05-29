import requests


def get_teams(BASE_URL):
    response = requests.get(f"{BASE_URL}/teams")
    response.raise_for_status()
    return response.json().get("teams", [])

def get_team_roster(team_id):
    response = requests.get(f"{BASE_URL}/teams/{team_id}/roster")
    response.raise_for_status()
    return response.json().get("roster", [])
