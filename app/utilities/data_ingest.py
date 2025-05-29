import sqlite3
from pathlib import Path
import os

def init_db(DB_PATH):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS teams (
        id INTEGER PRIMARY KEY,
        name TEXT,
        abbreviation TEXT,
        location TEXT
    )
    """)
    conn.commit()
    conn.close()

def insert_teams(teams):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    for team in teams:
        cur.execute("""
        INSERT OR REPLACE INTO teams (id, name, abbreviation, location)
        VALUES (?, ?, ?, ?)
        """, (team['id'], team['name'], team['abbreviation'], team['locationName']))

    conn.commit()
    conn.close()
