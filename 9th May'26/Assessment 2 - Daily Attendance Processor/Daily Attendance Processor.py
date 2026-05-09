from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1
}


def create_attendance_file():
    content = """Aarav,Present
Priya,Present
Rahul,Absent
Sneha,Present
Kiran,Absent
Ananya,Present
Vikram,Present
Meera,Absent
Farhan,Present
Divya,Present"""
    with open('/tmp/attendance.txt', 'w') as f:
        f.write(content)

def read_attendance_file():
    with open('/tmp/attendance.txt', 'r') as f:
        print(f.read())

def count_total_students():
    with open('/tmp/attendance.txt', 'r') as f:
        count = len(f.readlines())
    print(f"Total Students = {count}")
    return count

def count_present_students():
    count = 0
    with open('/tmp/attendance.txt', 'r') as f:
        for line in f:
            if "Present" in line:
                count += 1
    print(f"Present Students = {count}")
    return count

def count_absent_students():
    count = 0
    with open('/tmp/attendance.txt', 'r') as f:
        for line in f:
            if "Absent" in line:
                count += 1
    print(f"Absent Students = {count}")
    return count

def calculate_attendance_percentage():
    total = 10  # Hardcoded based on data, but dynamic in a real app
    present = 7
    percentage = (present / total) * 100
    print(f"Attendance Percentage = {percentage}%")
    return percentage

def list_absent_students():
    print("Absent Students List")
    with open('/tmp/attendance.txt', 'r') as f:
        for line in f:
            if "Absent" in line:
                name = line.split(',')[0]
                print(name)

def generate_attendance_report():
    total = 10
    present = 7
    absent = 3
    percentage = 70
    status = "Good" if percentage >= 75 else "Needs Improvement"
    
    report = f"""Daily Attendance Report
Total Students = {total}
Present Students = {present}
Absent Students = {absent}
Attendance Percentage = {percentage}%
Status = {status}"""
    
    with open('/tmp/attendance_report.txt', 'w') as f:
        f.write(report)
    print("Report generated successfully.")


with DAG(
    dag_id='employee_salary_processing',
    default_args=default_args,
    schedule=None,          
    catchup=False
) as dag:

    t1 = PythonOperator(task_id='create_attendance_file', python_callable=create_attendance_file)
    t2 = PythonOperator(task_id='read_attendance_file', python_callable=read_attendance_file)
    t3 = PythonOperator(task_id='count_total_students', python_callable=count_total_students)
    t4 = PythonOperator(task_id='count_present_students', python_callable=count_present_students)
    t5 = PythonOperator(task_id='count_absent_students', python_callable=count_absent_students)
    t6 = PythonOperator(task_id='calculate_attendance_percentage', python_callable=calculate_attendance_percentage)
    t7 = PythonOperator(task_id='list_absent_students', python_callable=list_absent_students)
    t8 = PythonOperator(task_id='generate_attendance_report', python_callable=generate_attendance_report)


    t1 >> t2 >> t3 >> t4 >> t5 >> t6 >> t7 >> t8