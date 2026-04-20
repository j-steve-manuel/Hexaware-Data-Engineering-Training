import json
import csv

# Create separate functions for the following:

# Task 26
# A function to read names from students.txt .
def get_student_names(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]

# Task 27
# A function to load student marks from marks.json .
def load_marks_data(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
        return data['students']

# Task 28
# A function to load attendance from attendance.csv .
def load_attendance_data(filename):
    attendance = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['days_present'] = int(row['days_present'])
            row['total_days'] = int(row['total_days'])
            attendance.append(row)
        return attendance

# Task 29
# A function to calculate average marks.
def calculate_average(marks_list):
    if not marks_list:
        return 0
    return sum(marks_list) / len(marks_list)

# Task 30
# A function to calculate attendance percentage.
def calculate_attendance_pct(present, total):
    if total == 0:
        return 0
    return (present / total) * 100

# Task 31
# A function to return the topper.
def get_topper(marks_dict):
    if not marks_dict:
        return None
    return max(marks_dict, key=marks_dict.get)

# Task 32
# A function to generate grade for a mark.
def generate_grade(mark):
    if mark >= 90: return 'A'
    elif mark >= 75: return 'B'
    elif mark >= 50: return 'C'
    else: return 'Fail'



# --- TESTING THE FUNCTIONS ---

# Loading data
names = get_student_names('students.txt')
marks_json = load_marks_data('marks.json')
attendance_csv = load_attendance_data('attendance.csv')

# Creating a marks dictionary for the topper function
marks_only_dict = {s['name']: s['marks'] for s in marks_json}

# Example outputs
print(f"Total Unique Students: {len(set(names))}")
print(f"Average Mark: {calculate_average(list(marks_only_dict.values())):.2f}")
print(f"Class Topper: {get_topper(marks_only_dict)}")
print(f"Grade for 82: {generate_grade(82)}")