# run_pipeline.py
from extract.extract_api import extract
from transform.transform_data import transform
from load.load_postgres import load

def main():
    extract()
    transform()
    load()
    print("ETL completado correctamente.")

if __name__ == "__main__":
    main()
