# 📊 ETL Data Pipeline

Proyecto de **Ingeniería de Datos** con un pipeline ETL (Extract, Transform, Load).  
Los datos se extraen de una API pública, se transforman con **pandas** y se cargan en **PostgreSQL**.

# Para ejecutar:
- crear una conexion en dbeaver (o a postgreSQL)
- seguir paso a paso el archivo "postgre_creator.sql" 

# 🚀 Tecnologías
- Python
- pandas
- PostgreSQL
- Apache Airflow / Prefect `proximamente`
- Docker

## 📂 Estructura
- `extract/` → scripts de extracción de datos.
- `transform/` → limpieza y normalización.
- `load/` → carga a la base de datos.
- `dags/` → futuros flujos de Airflow.

### Por qué opte por esta estructura?
- Modular: cada etapa ETL es independiente → fácil mantenimiento.
- Preparada para migrar a Airflow: después podés convertir cada script en una tarea (PythonOperator).

## 💡 Próximos pasos
- Agregar orquestación con Airflow.
- Conectar con dashboard de visualización.
