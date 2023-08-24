from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

def process_orders():
    # Your order processing logic here
    print("Processing orders...")

def generate_invoice():
    # Your invoice generation logic here
    print("Generating invoices...")

default_args = {
    'owner': 'your_name',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'order_fulfillment_dag',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
) as dag:
    start_task = DummyOperator(task_id='start_task')
    
    process_orders_task = PythonOperator(
        task_id='process_orders_task',
        python_callable=process_orders,
    )
    
    generate_invoice_task = PythonOperator(
        task_id='generate_invoice_task',
        python_callable=generate_invoice,
    )

    end_task = DummyOperator(task_id='end_task')

    start_task >> process_orders_task >> generate_invoice_task >> end_task
