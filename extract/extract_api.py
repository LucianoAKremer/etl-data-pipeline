# extract/extract_api.py
import os
import requests
import pandas as pd
from datetime import datetime
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CSV_FILE = os.path.join(BASE_DIR, "data", "data.csv")
SAMPLE_FILE = os.path.join(BASE_DIR, "data", "sample_data.csv")
API_URL = "https://jsonplaceholder.typicode.com/posts"

def _requests_session_with_retries(total=3, backoff=1):
    session = requests.Session()
    retries = Retry(
        total=total,
        backoff_factor=backoff,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=frozenset(['GET', 'POST'])
    )
    adapter = HTTPAdapter(max_retries=retries)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session

def _create_sample_csv(path):
    sample = [
        {"userId": 1, "id": 1, "title": "Sample Title 1", "body": "This is a sample body text 1."},
        {"userId": 2, "id": 2, "title": "Sample Title 2", "body": "This is a sample body text 2."}
    ]
    df = pd.DataFrame(sample)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
    return df

def extract():
    print(f"[{datetime.now()}] Intentando extraer datos desde la API: {API_URL}")
    session = _requests_session_with_retries()
    try:
        resp = session.get(API_URL, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        if not isinstance(data, list) or len(data) == 0:
            raise ValueError("Respuesta vacía o no lista de posts.")
        df = pd.DataFrame(data)
        os.makedirs(os.path.dirname(CSV_FILE), exist_ok=True)
        df.to_csv(CSV_FILE, index=False)
        print(f"[{datetime.now()}] Extracción exitosa. Guardado en {CSV_FILE}")
        return df
    except Exception as e:
        print(f"[{datetime.now()}] ERROR al obtener datos de la API: {e}")
        if os.path.exists(SAMPLE_FILE):
            print(f"[{datetime.now()}] Usando archivo local de muestra: {SAMPLE_FILE}")
            df = pd.read_csv(SAMPLE_FILE)
            df.to_csv(CSV_FILE, index=False)
            return df
        else:
            print(f"[{datetime.now()}] No existe sample_data.csv, generando uno de ejemplo en {SAMPLE_FILE}")
            df = _create_sample_csv(SAMPLE_FILE)
            df.to_csv(CSV_FILE, index=False)
            return df

if __name__ == "__main__":
    extract()
