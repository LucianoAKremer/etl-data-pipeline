import requests
import pandas as pd
import psycopg2
from datetime import datetime

# ---------- CONFIG ----------
DB_CONFIG = {
    'dbname': 'etl_db',
    'user': 'etl_user',
    'password': 'etl_password',
    'host': 'localhost',
    'port': 5432
}

API_URL = "https://api.publicapis.org/entries"
CSV_FILE = "data.csv"

# ---------- ETAPA 1: EXTRACCIÓN ----------
def extract():
    print(f"[{datetime.now()}] Extrayendo datos de la API...")
    response = requests.get(API_URL)
    data = response.json()['entries']
    df = pd.DataFrame(data)
    df.to_csv(CSV_FILE, index=False)
    print(f"[{datetime.now()}] Datos guardados en {CSV_FILE}")
    return df

# ---------- ETAPA 2: TRANSFORMACIÓN ----------
def transform(df):
    print(f"[{datetime.now()}] Transformando datos...")
    df = df[['API', 'Description', 'Auth', 'HTTPS', 'Cors', 'Category']]
    df['Description'] = df['Description'].str[:255]  # Truncar si es muy largo
    print(f"[{datetime.now()}] Transformación completada.")
    return df

# ---------- ETAPA 3: CARGA ----------
def load(df):
    print(f"[{datetime.now()}] Cargando datos en PostgreSQL...")
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()

    # Crear tabla si no existe
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

    # Insertar datos
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO public_apis (API, Description, Auth, HTTPS, Cors, Category)
            VALUES (%s,%s,%s,%s,%s,%s)
        """, tuple(row))

    conn.commit()
    cursor.close()
    conn.close()
    print(f"[{datetime.now()}] Carga completada.")

# ---------- MAIN ----------
def main():
    df_raw = extract()
    df_transformed = transform(df_raw)
    load(df_transformed)
    print(f"[{datetime.now()}] ETL finalizado correctamente.")

if __name__ == "__main__":
    main()
