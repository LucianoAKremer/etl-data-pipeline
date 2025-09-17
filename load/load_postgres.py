import psycopg2
import pandas as pd

def load():
    # Conexión a PostgreSQL
    conn = psycopg2.connect(
        dbname="etl_db",
        user="etl_user",
        password="etl_password",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()

    # Crear la tabla dentro del esquema etl_schema
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS etl_schema.posts (
            userId INT,
            id INT PRIMARY KEY,
            title TEXT,
            body TEXT
        )
    """)
    conn.commit()

    # Leer el CSV generado en la fase transform
    df = pd.read_csv("transform/posts_clean.csv")

    # Insertar datos en la tabla
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO etl_schema.posts (userId, id, title, body)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING;
        """, (row["userId"], row["id"], row["title"], row["body"]))

    conn.commit()
    cursor.close()
    conn.close()
