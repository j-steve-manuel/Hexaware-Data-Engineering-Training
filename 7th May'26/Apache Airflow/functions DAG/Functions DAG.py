from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def wake_up_task_function():
    print("Student woke up at 6 AM")

def exercise_task_function():
    print("Student completed morning exercise")

def attend_class_task_function():
    print("Student attended python classes")


def complete_assignment_task_function():
    print("Student completed Airflow assignment")

def sleep_task_function():
    print("Student went to sleep at 10PM")


with DAG(
    dag_id="student_daily_tasks_dag",

    start_date=datetime(2025, 1, 1),

    schedule="@daily",

    catchup=False,

    tags=["training"]

) as dag:


    task1 = PythonOperator(
        task_id="wake_up_task",

        python_callable=wake_up_task_function
    )

    task2 = PythonOperator(
        task_id="exercise_task",

        python_callable=exercise_task_function
    )

    task3 = PythonOperator(
        task_id="attend_class_task",

        python_callable=attend_class_task_function
    )


    task4 = PythonOperator(
        task_id="complete_assignment_task",

        python_callable=complete_assignment_task_function
    )
    
    task5 = PythonOperator(
        task_id="sleep_task",

        python_callable=sleep_task_function
    )
    
    task1 >> task2 >> task3 >> task4 >> task5
    
