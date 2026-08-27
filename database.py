import sqlite3
import os

DB_PATH = os.path.join("database", "interview.db")

def create_tables():
    os.makedirs("database", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS interviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        candidate_name TEXT,
        role TEXT,
        score REAL,
        feedback TEXT
    )
    """)
    conn.commit()
    conn.close()

def save_interview(candidate_name, role, score, feedback):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO interviews (candidate_name, role, score, feedback)
        VALUES (?, ?, ?, ?)
    """, (candidate_name, role, score, feedback))
    conn.commit()
    conn.close()

def get_all_interviews():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, candidate_name, role, score, feedback FROM interviews ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows

if __name__ == "__main__":
    create_tables()
