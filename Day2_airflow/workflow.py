import os
import sys
import pytz
import datetime
from datetime import datetime, timedelta
from preprocessing import execute_preprocessing
from train import  execute_train
from inference import execute_inference


import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

START_TIME = datetime.now(pytz.timezone('Asia/Tokyo')).strftime('%Y-%m-%d %H:%M:%S')

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime.today(),
    'email': None,
    'email_on_failure': False,
    'email_on_retry': False,
}

dag = DAG(
    'ml_operation',
    description='DAG for ML operation',
    default_args=default_args,
    schedule_interval=timedelta(days=1)
)


preprocess = PythonOperator(
    task_id='preprocess',
    python_callable=execute_preprocessing,
    dag=dag
)

train = PythonOperator(
    task_id='train',
    python_callable=execute_train,
    dag=dag
)

inference = PythonOperator(
    task_id='',
    python_callable=execute_preprocessing,
    dag=dag
)

preprocess >> train >> inference
