import pandas as pd
from db_connection import connect_to_db  # adjust if needed

def load_data_to_mysql():
    df = pd.read_csv("data/clean_jobs.csv")

    # Replace NaN with empty string
    df = df.fillna("")

    connection = connect_to_db()
    cursor = connection.cursor()

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO jobs (company, position, location, tags, url)
            VALUES (%s, %s, %s, %s, %s)
        """, tuple(row))

    connection.commit()
    cursor.close()
    connection.close()
    print("Data loaded into MySQL")

if __name__ == "__main__":
    load_data_to_mysql()
