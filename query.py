import mysql.connector
from db_connection import connect_to_db  # or adjust import if in root

def fetch_jobs(limit=10):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, company, position, location, tags, url FROM jobs LIMIT %s", (limit,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

if __name__ == "__main__":
    for row in fetch_jobs():
        print(row)
