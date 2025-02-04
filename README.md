# 🚀 Data Engineering Pipeline with Flask, PostgreSQL, dbt & Airflow

## 📌 Overview

This project is a containerized data pipeline that:

1. **📡 Generates Data via a Flask API**: A Flask application simulates data generation and provides endpoints for data ingestion.
2. **🗄️ Stores Data in PostgreSQL**: Ingested data is stored in a PostgreSQL database for persistence.
3. **🔄 Transforms Data Using dbt**: Data Build Tool (dbt) is utilized for data modeling and transformation, converting raw data into a structured format.
4. **📊 Automates Workflows with Apache Airflow**: Airflow orchestrates the data pipeline, scheduling and managing the ETL processes.

## 🛠️ Tech Stack

- **🐳 Docker**: Containerization and orchestration
- **🌐 Flask**: API for data ingestion
- **🐘 PostgreSQL**: Database for storing raw and transformed data
- **⚡ dbt**: Data modeling and transformation
- **⏳ Apache Airflow**: Workflow orchestration

## 📂 Project Structure

The repository is organized as follows:

```
data-engineering-project/
├── ⚡ airflow/                # Airflow DAGs and setup
│   ├── dags/
│   │   ├── dbt_dag.py      # Airflow DAG for dbt
│   ├── Dockerfile          # Airflow Dockerfile
├── 📊 dbt/                    # dbt project
│   ├── models/
│   │   ├── staging/
│   │   │   ├── stg_payment_amount.sql
│   │   ├── transformations/
│   │   │   ├── payment_amount.sql
│   ├── dbt_project.yml
│   ├── profiles.yml        # dbt profiles configuration
├── 🌐 flask-api/              # Flask application
│   ├── app.py              # Main Flask app
│   ├── db_utils.py         # Database utility functions
│   ├── requirements.txt    # Flask dependencies
├── 🐘 postgres/               # PostgreSQL initialization
│   ├── init.sql            # Database initialization script
├── ⚙️ .env                    # Environment variables
├── 📖 README.md               # Project documentation
├── 🐳 docker-compose.yml      # Docker Compose configuration
```

## ⚙️ Setup and Deployment

### 🛠️ Prerequisites

- 🐳 Docker & Docker Compose installed
- 🐍 Python 3 installed

### 🚀 Steps to Run the Project

1. **📥 Clone the Repository**:
   ```bash
   git clone https://github.com/hakanozger/data-engineering-dbt-airflow.git
   cd data-engineering-dbt-airflow
   ```

2. **📝 Set Up Environment Variables**:
   - Create a `.env` file in the root directory with the necessary environment variables.
   - Ensure that the `profiles.yml` file is correctly configured for dbt.

3. **🏗️ Build and Start Docker Containers**:
   ```bash
   docker-compose up --build
   ```

### 🔍 Verifying Setup
To check if dbt profile is properly mapped inside the container, run:
```sh
docker exec -it dbt ls /root/.dbt/
```
If `profiles.yml` is missing, manually copy it:
```sh
docker cp ./dbt/profiles.yml dbt:/root/.dbt/profiles.yml
```

### 🌎 Accessing Components

- **🌐 Flask API**: Accessible at `http://localhost:5001`
- **📊 Airflow UI**: Accessible at `http://localhost:8080` username=admin password: admin

## 🚀 Future Enhancements

- 📈 Implement logging and monitoring for better observability.
- ✅ Add data validation and quality checks to ensure data integrity.
- ⚡ Optimize dbt models for improved performance.

## 📜 License

This project is open-source and available for modifications.

For more details, please refer to the [GitHub repository](https://github.com/hakanozger/data-engineering-dbt-airflow).
