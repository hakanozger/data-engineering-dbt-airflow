# data-engineering-dbt-airflow

## Project Overview

This project integrates Apache Airflow and dbt (data build tool) to create a robust data engineering pipeline. The pipeline orchestrates data extraction, transformation, and loading (ETL) processes using Airflow and dbt.

## Project Structure
data-engineering-project/
│── airflow/              # Airflow DAGs and setup
│   ├── dags/
│   │   ├── dbt_dag.py    # Airflow DAG for dbt
│   ├── Dockerfile        # Airflow Dockerfile
│── dbt/                  # dbt project
│   ├── models/
│   │   ├── staging/
│   │   │   ├── stg_payment_amount.sql
│   │   ├── transformations/
│   │   │   ├── payment_amount.sql
│   ├── dbt_project.yml
│   ├── profiles.yml      # dbt connection config
│   ├── Dockerfile        # dbt Dockerfile
│── flask-api/            # Flask API
│   ├── app.py            # Flask application
│   ├── requirements.txt  # Flask dependencies
│   ├── Dockerfile        # Flask Dockerfile
│── postgres/             # PostgreSQL configuration
│   ├── init.sql          # SQL script to initialize databases
│── .env                  # Environment variables
│── docker-compose.yml    # Docker Compose configuration
│── README.md             # Documentation

## Components

### Airflow

Airflow is used to orchestrate the ETL processes. The Airflow directory contains configuration files, DAGs (Directed Acyclic Graphs), and logs.

- **DAGs**: The `dags/` directory contains the DAGs for the ETL processes. For example, `dbt_dag.py` and `example_dag.py`.
- **Configuration**: The `airflow.cfg` file contains the Airflow configuration.
- **Logs**: The `logs/` directory contains the logs generated by Airflow.

### dbt

dbt is used for data transformation. The dbt directory contains the dbt project configuration, models, and logs.

- **Project Configuration**: The `dbt_project.yml` file contains the dbt project configuration.
- **Profiles**: The `profiles.yml` file contains the dbt profiles configuration.
- **Models**: The `models/` directory contains the dbt models for staging and transformations.
- **Logs**: The `logs/` directory contains the logs generated by dbt.

### Flask API

A Flask API is used to interact with the data pipeline. The Flask API directory contains the application code, database utilities, and dependencies.

- **Application**: The `app.py` file contains the Flask application code.
- **Database Utilities**: The `db_utils.py` file contains utility functions for database interactions.
- **Dependencies**: The `requirements.txt` file contains the Python dependencies for the Flask API.

### Postgres

Postgres is used as the database for the data pipeline. The Postgres directory contains the initialization SQL script.

- **Initialization**: The `init.sql` file contains the SQL script to initialize the database.

### Docker

Docker is used to containerize the different components of the project. The `docker-compose.yml` file is used to orchestrate the containers.

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Setup

1. Clone the repository:

    ```sh
    git clone <repository-url>
    cd data-engineering-dbt-airflow
    ```

2. Create a  file with the necessary environment variables.

3. Build and start the Docker containers:

    ```sh
    docker-compose up --build
    ```

4. Access the Airflow web server at `http://localhost:8080`.

5. Access the Flask API at `http://localhost:5000`.

## Usage

- **Airflow**: Use the Airflow web interface to trigger and monitor DAGs.
- **dbt**: Use dbt commands to run models and generate documentation.
- **Flask API**: Use the Flask API to interact with the data pipeline.

## Logs

- Airflow logs are stored in the  directory.
- dbt logs are stored in the  directory.
- Flask API logs are stored in the `flask-api/logs/` directory.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.