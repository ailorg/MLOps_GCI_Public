from datetime import timedelta

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': None,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}
dag = DAG(
    'mlops2',
    default_args=default_args,
    description='A flow of ML',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2),
    tags=['example'],
)

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = BashOperator(
    task_id='Data_Extraction',
    bash_command='sleep 3',
    dag=dag,
)

t2 = BashOperator(
    task_id='model1_trian',
    depends_on_past=False,
    bash_command='sleep 5',
    retries=3,
    dag=dag,
)
dag.doc_md = __doc__

t3 = BashOperator(
    task_id='model2_train',
    depends_on_past=False,
    bash_command='sleep 5',
    dag=dag,
)

t4 = BashOperator(
    task_id='model3_train',
    depends_on_past=False,
    bash_command='sleep 5',
    dag=dag,
)

t5 = BashOperator(
    task_id='ensemble',
    depends_on_past=False,
    bash_command='sleep 5',
    dag=dag,
)

t1 >> [t2, t3, t4] >> t5
