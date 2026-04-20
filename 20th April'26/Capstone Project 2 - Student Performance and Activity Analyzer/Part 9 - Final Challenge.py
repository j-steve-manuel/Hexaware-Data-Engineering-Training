# Final Challenge
# Task 39
# Generate this final console output:
# Topper: Sneha
# Best Attendance: Sneha
# Average Marks: 82.6
# Eligible Students: Rahul, Sneha, Priya
# Students Needing Improvement: Karan

# Task 40
# Make the program modular using functions and keep the code clean.

import json
import csv

def load_student_data():
    with open('marks.json', 'r') as f:
        marks_list = json.load(f)['students']

    attendance_lookup = {}
    with open('attendance.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            pct = (int(row['days_present']) / int(row['total_days'])) * 100
            attendance_lookup[row['name']] = pct

    combined = {}
    for s in marks_list:
        name = s['name']
        combined[name] = {
            "marks": s['marks'],
            "attendance": attendance_lookup.get(name, 0),
            "course": s['course']
        }
    return combined


def get_analytics(data):
    topper = max(data, key=lambda x: data[x]['marks'])
    best_att = max(data, key=lambda x: data[x]['attendance'])
    avg_marks = sum(s['marks'] for s in data.values()) / len(data)
    eligible = [n for n, info in data.items() if info['marks'] >= 75 and info['attendance'] >= 80]
    needs_imp = [n for n, info in data.items() if info['marks'] < 75 or info['attendance'] < 80]

    return topper, best_att, avg_marks, eligible, needs_imp


def main():
    final_data = load_student_data()

    topper, best_att, avg, eligible, improvement = get_analytics(final_data)

    print(f"Topper: {topper}")
    print(f"Best Attendance: {best_att}")
    print(f"Average Marks: {avg:.1f}")
    print(f"Eligible Students: {', '.join(eligible)}")
    print(f"Students Needing Improvement: {', '.join(improvement)}")


if __name__ == "__main__":
    main()