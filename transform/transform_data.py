# transform/transform_data.py
import os
import pandas as pd
from datetime import datetime

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CSV_FILE = os.path.join(BASE_DIR, "data", "data.csv")

def transform():
    print(f"[{datetime.now()}] Transformando datos...")
    df = pd.read_csv(CSV_FILE, encoding='utf-8')


    # columnas que queremos
    cols = ['userId', 'id', 'title', 'body']
    # asegurarnos que existan
    for c in cols:
        if c not in df.columns:
            df[c] = pd.NA

    df = df[cols].copy()

    # normalización
    df['title'] = df['title'].astype(str).str.slice(0,200)
    df['body'] = df['body'].astype(str).str.slice(0,1000)

    # tipos
    df['userId'] = pd.to_numeric(df['userId'], errors='coerce').fillna(0).astype(int)
    df['id'] = pd.to_numeric(df['id'], errors='coerce').fillna(0).astype(int)

    # eliminar duplicados
    df = df.drop_duplicates(subset=['id'])

    df.to_csv(CSV_FILE, index=False)
    print(f"[{datetime.now()}] Transformación completada. Archivo actualizado: {CSV_FILE}")
    return df

if __name__ == "__main__":
    transform()
