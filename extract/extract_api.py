import requests
import pandas as pd
from datetime import datetime

CSV_FILE = "../data/data.csv"
API_URL = "https://api.publicapis.org/entries"

def extract():
    print(f"[{datetime.now()}] Extrayendo datos de la API...")
    response = requests.get(API_URL)
    data = response.json()['entries']
    df = pd.DataFrame(data)
    df.to_csv(CSV_FILE, index=False)
    print(f"[{datetime.now()}] Datos guardados en {CSV_FILE}")
    return df

if __name__ == "__main__":
    extract()
