from datetime import datetime
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.providers.dbt.cloud.operators.dbt import DbtCloudRunJobOperator

def my_func():
    print('Get data')

with DAG(dag_id='DBT', 
         schedule_interval=None, 
         start_date=datetime(2023, 1, 1), 
         default_args={"dbt_cloud_conn_id": "dbt_cloud", "account_id": 142169,},
         catchup=False) as dag: 

    rest_API_1 = PythonOperator(
        task_id='Hit_api',
        python_callable=my_func
        )

    trigger_job = DbtCloudRunJobOperator(
        task_id="trigger_job",
        job_id=204058,
        check_interval=10,
        timeout=300
        )

    task_3 = DummyOperator(task_id='Task_3')

rest_API_1 >> trigger_job >> task_3
