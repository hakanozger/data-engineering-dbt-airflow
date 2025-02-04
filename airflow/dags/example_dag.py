from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import requests

def generate_sample_data():
    url = "http://flask-api:5001/generate"
    requests.post(url)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 0,
}

dag = DAG(
    'data_pipeline',
    default_args=default_args,
    description='A simple data pipeline DAG',
    schedule_interval=None,
    catchup=False,
)

task_generate_data = PythonOperator(
    task_id='generate_data',
    python_callable=generate_sample_data,
    dag=dag,
)

task_generate_data
