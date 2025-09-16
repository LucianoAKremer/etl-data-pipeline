# 📊 ETL Data Pipeline

Proyecto de **Ingeniería de Datos** con un pipeline ETL (Extract, Transform, Load).  
Los datos se extraen de una API pública, se transforman con **pandas** y se cargan en **PostgreSQL**.

# Para ejecutar:
- configura tu base de datos (PostgreSQL):
`CREATE DATABASE etl_db;`
`CREATE USER etl_user WITH ENCRYPTED PASSWORD 'etl_password';`
`GRANT ALL PRIVILEGES ON DATABASE etl_db TO etl_user;`

- Para ejecutar el script, usa `python scripts/etl_pipeline.py`.

# 🚀 Tecnologías
- Python
- pandas
- PostgreSQL
- Apache Airflow / Prefect
- Docker

## 📂 Estructura
- `extract/` → scripts de extracción de datos.
- `transform/` → limpieza y normalización.
- `load/` → carga a la base de datos.
- `dags/` → flujos de Airflow.

## 💡 Próximos pasos
- Agregar orquestación con Airflow.
- Conectar con dashboard de visualización.
