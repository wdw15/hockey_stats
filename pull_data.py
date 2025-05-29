from app.utilities import nhl_api, data_ingest
from dotenv import load_dotenv
import os

# pull_data.py
load_dotenv()  # Ensure environment variables are loaded

def main():
    db_path = os.getenv("DATABASE_PATH", "data/nhl_stats.db")
    base_url = os.getenv("NHL_API_BASE_URL", "https://statsapi.web.nhl.com/api/v1")
    data_ingest.init_db(db_path)
    teams = nhl_api.get_teams(base_url)
    data_ingest.insert_teams(teams, db_path)

    print("✅ NHL teams pulled and inserted into DB.")

if __name__ == "__main__":
    main()
