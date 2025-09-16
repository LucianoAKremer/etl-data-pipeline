import pandas as pd
from datetime import datetime

CSV_FILE = "../data/data.csv"

def transform():
    print(f"[{datetime.now()}] Transformando datos...")
    df = pd.read_csv(CSV_FILE)
    df = df[['API', 'Description', 'Auth', 'HTTPS', 'Cors', 'Category']]
    df['Description'] = df['Description'].str[:255]  # Truncar si es muy largo
    df.to_csv(CSV_FILE, index=False)  # Sobrescribe CSV limpio
    print(f"[{datetime.now()}] Transformación completada.")
    return df

if __name__ == "__main__":
    transform()
