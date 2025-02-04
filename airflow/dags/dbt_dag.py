from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 2, 1),
    "retries": 0,

}

dag = DAG(
    "dbt_pipeline",
    default_args=default_args,
    description="Runs dbt transformations",
    schedule_interval=None,
    catchup=False,
)

# Task to run dbt inside the dbt container
run_dbt = BashOperator(
    task_id="run_dbt",
    bash_command="docker exec dbt dbt run",
    dag=dag,
)

run_dbt
