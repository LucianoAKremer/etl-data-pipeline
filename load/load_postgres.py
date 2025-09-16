import pandas as pd
import psycopg2
from datetime import datetime

CSV_FILE = "../data/data.csv"
DB_CONFIG = {
    'dbname': 'etl_db',
    'user': 'etl_user',
    'password': 'etl_password',
    'host': 'localhost',
    'port': 5432
}

def load():
    print(f"[{datetime.now()}] Cargando datos en PostgreSQL...")
    df = pd.read_csv(CSV_FILE)

    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS public_apis (
            API TEXT,
            Description TEXT,
            Auth TEXT,
            HTTPS BOOLEAN,
            Cors TEXT,
            Category TEXT
        );
    """)

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO public_apis (API, Description, Auth, HTTPS, Cors, Category)
            VALUES (%s,%s,%s,%s,%s,%s)
        """, tuple(row))

    conn.commit()
    cursor.close()
    conn.close()
    print(f"[{datetime.now()}] Carga completada.")

if __name__ == "__main__":
    load()
