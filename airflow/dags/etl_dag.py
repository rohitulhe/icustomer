from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import logging

from etl.data_ingestion import ingest_data
from etl.data_cleaning import clean_data
from etl.data_transformation import transform_data
from etl.data_loading import load_data

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'etl_dag',
    default_args=default_args,
    description='ETL DAG',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(1),
    catchup=False,
)

csv_file = 'data/interaction.csv'  #CSV file path
db_url = 'postgresql://airflow:airflow@postgres:5432/airflow'  #PostgreSQL URL


ingest_task = PythonOperator(
    task_id='ingest',
    provide_context=True,
    python_callable=ingest_data,
    op_args=[csv_file],
    dag=dag,
)

clean_task = PythonOperator(
    task_id='clean',
    provide_context=True,
    python_callable=clean_data,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform',
    provide_context=True,
    python_callable=transform_data,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load',
    provide_context=True,
    python_callable=load_data,
    op_args=[db_url],
    dag=dag,
)

ingest_task >> clean_task >> transform_task >> load_task
