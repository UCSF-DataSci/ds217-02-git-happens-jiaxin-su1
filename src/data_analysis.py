# data analysis to do...

import os

def load_students(filename="data/students.csv"):
    students = []
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()        

    for raw in lines[1:]:# skip header
        line = raw.strip()
        if not line:
            continue# skip blanks
        parts = [p.strip() for p in line.split(",")]
        if len(parts) < 4:
            # not enough columns: name, age, grade, subject
            continue
        name, age_str, grade_str, subject = parts[:4]

        # convert grade; skip row if not an int
        try:
            grade = int(grade_str)
        except ValueError:
            continue

        students.append([name, age_str, grade, subject.lower()])
    return students

def count_math_students(students):
    return sum(1 for s in students if len(s) >= 4 and str(s[3]).lower() == "math")

def calculate_average_grade(students):
    total = 0
    count = 0
    for student in students:
        total += int(student[2])
        count += 1
    return total / count if count > 0 else 0

def generate_report(students):
    total = len(students)
    avg = calculate_average_grade(students)
    math_count = count_math_students(students)

    report = f"""basic analysis report
Total Students: {total}
Average Grade: {avg:.1f}
Math Students: {math_count}"""
    return report

def save_report(report, filename="output/analysis_report.txt"):
    """Write report to a file, creating the output directory if needed."""
    out_dir = os.path.dirname(filename) or "."
    os.makedirs(out_dir, exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(report)


def main():
    students = load_students()
    report = generate_report(students)
    save_report(report)
    print("Report saved to output/analysis_report.txt")


if __name__ == "__main__":
    main()