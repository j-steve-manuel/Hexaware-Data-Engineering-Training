from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1
}



def create_employee_file():
    content = """Rahul,45000
Sneha,52000
Amit,61000
Priya,47000
Kiran,39000"""
    with open('/tmp/employees.txt', 'w') as f:
        f.write(content)
    print("Employee file created successfully.")

def read_employee_data():
    with open('/tmp/employees.txt', 'r') as f:
        data = f.read()
        print(data)

def calculate_salary_expense():
    total = 0
    with open('/tmp/employees.txt', 'r') as f:
        for line in f:
            name, salary = line.strip().split(',')
            total += int(salary)
    print(f"Total Salary Expense = {total}")
    return total

def find_highest_salary():
    highest_val = 0
    top_employee = ""
    with open('/tmp/employees.txt', 'r') as f:
        for line in f:
            name, salary = line.strip().split(',')
            if int(salary) > highest_val:
                highest_val = int(salary)
                top_employee = name
    print(f"Highest Salary = {highest_val}")
    print(f"Employee = {top_employee}")
    return {"name": top_employee, "salary": highest_val}

def generate_salary_report():
    total_expense = 0
    count = 0
    with open('/tmp/employees.txt', 'r') as f:
        for line in f:
            count += 1
            total_expense += int(line.strip().split(',')[1])
            
    report_content = f"""Employee Salary Report
Total Employees = {count}
Total Salary Expense = {total_expense}
Status = Processed Successfully"""
    
    with open('/tmp/salary_report.txt', 'w') as f:
        f.write(report_content)
    print("Salary report generated at /tmp/salary_report.txt")



with DAG(
    dag_id='employee_salary_processing',
    default_args=default_args,
    schedule=None,           
    catchup=False
) as dag:

    t1 = PythonOperator(task_id='create_employee_file', python_callable=create_employee_file)
    t2 = PythonOperator(task_id='read_employee_data', python_callable=read_employee_data)
    t3 = PythonOperator(task_id='calculate_salary_expense', python_callable=calculate_salary_expense)
    t4 = PythonOperator(task_id='find_highest_salary', python_callable=find_highest_salary)
    t5 = PythonOperator(task_id='generate_salary_report', python_callable=generate_salary_report)

   
    t1 >> t2 >> t3 >> t4 >> t5