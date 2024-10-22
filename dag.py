from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator  # Updated import for newer versions
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 10, 21),
    'depends_on_past': False,
    'email': ['danielkyme@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('fetch_cricket_stats',
          default_args=default_args,
          description='Runs a Python script to fetch cricket statistics',
          schedule_interval='@daily',
          catchup=False)

with dag:
    run_script_task = BashOperator(
        task_id='run_script',
        bash_command='python3 /home/airflow/gcs/dags/scripts/extract_data.py',  # Explicitly using python3
    )
