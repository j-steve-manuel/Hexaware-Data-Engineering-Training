from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Path definitions
MARKS_FILE = '/tmp/student_marks.txt'
RESULT_FILE = '/tmp/result.txt'

# 1. Create the marks file
def create_marks_file():
    content = "Math,80\nScience,75\nEnglish,90\nPython,95"
    with open(MARKS_FILE, 'w') as f:
        f.write(content)
    print(f"File created at {MARKS_FILE}")

# 2. Read and log the marks
def read_marks_file():
    with open(MARKS_FILE, 'r') as f:
        lines = f.readlines()
        for line in lines:
            print(line.strip())

# 3. Calculate total marks and pass to XCom
def calculate_total(ti):
    total = 0
    with open(MARKS_FILE, 'r') as f:
        for line in f:
            if line.strip():
                _, mark = line.strip().split(',')
                total += int(mark)
    print(f"Total Marks = {total}")
    ti.xcom_push(key='total_marks', value=total)

# 4. Bonus Task: Calculate Percentage
def percentage_calculation(ti):
    total = ti.xcom_pull(key='total_marks', task_ids='calculate_total')
    # Assuming 4 subjects, 100 marks each
    percentage = (total / 400) * 100
    print(f"Percentage = {percentage}")
    ti.xcom_push(key='percentage', value=percentage)

# 5. Generate final result file
def generate_result(ti):
    total = ti.xcom_pull(key='total_marks', task_ids='calculate_total')
    percentage = ti.xcom_pull(key='percentage', task_ids='percentage_calculation')
    
    result_status = "PASS" if percentage >= 40 else "FAIL"
    
    content = (
        f"Student Result Summary\n"
        f"Total Marks = {total}\n"
        f"Percentage = {int(percentage)}\n"
        f"Result = {result_status}"
    )
    
    with open(RESULT_FILE, 'w') as f:
        f.write(content)
    print(f"Result file generated at {RESULT_FILE}")

# DAG Definition
with DAG(
    dag_id='student_marks_workflow',
    start_date=datetime(2024, 1, 1),
    schedule=None,  # Fixed: changed from schedule_interval
    catchup=False
) as dag:

    t1 = PythonOperator(
        task_id='create_marks_file', 
        python_callable=create_marks_file
    )
    
    t2 = PythonOperator(
        task_id='read_marks_file', 
        python_callable=read_marks_file
    )
    
    t3 = PythonOperator(
        task_id='calculate_total', 
        python_callable=calculate_total
    )
    
    t4 = PythonOperator(
        task_id='percentage_calculation', 
        python_callable=percentage_calculation
    )
    
    t5 = PythonOperator(
        task_id='generate_result', 
        python_callable=generate_result
    )

    # Dependency Chain
    t1 >> t2 >> t3 >> t4 >> t5

