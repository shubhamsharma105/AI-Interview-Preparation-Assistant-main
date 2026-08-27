import sqlite3
import pandas as pd
import os

DB_PATH = os.path.join("database", "interview.db")

def generate_report():
    if not os.path.exists(DB_PATH):
        return None

    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql_query("SELECT * FROM interviews", conn)
    conn.close()

    if df.empty:
        return None

    total_interviews = len(df)
    avg_score = df["score"].mean()
    pass_count = len(df[df["score"] >= 70])
    pass_rate = (pass_count / total_interviews) * 100

    # Role-based average scores
    role_summary = df.groupby("role")["score"].mean().reset_index()
    role_summary.columns = ["Role", "Average Score"]

    report = {
        "df": df,
        "total_interviews": total_interviews,
        "average_score": round(avg_score, 2),
        "pass_rate": round(pass_rate, 1),
        "role_summary": role_summary
    }

    return report
