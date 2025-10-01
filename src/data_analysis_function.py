# functions for data analysis
import os

def load_data(filename):
    """Generic loader that dispatches based on file extension."""
 
    if filename.endswith(".csv"):
        return load_csv(filename)
    raise ValueError(f"Unsupported file type: {ext}")

def load_csv(filename="data/students.csv"):
    students = []
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for raw in lines[1:]:  # skip header
        line = raw.strip()
        if not line:
            continue
        parts = [p.strip() for p in line.split(",")]
        # drop empty trailing tokens from dangling commas (optional)
        while parts and parts[-1] == "":
            parts.pop()
        if len(parts) < 4:
            continue

        name, age_str, grade_str, subject = parts[:4]

        try:
            grade = int(grade_str)
        except ValueError:
            continue

        # optional: parse age if it's clean
        try:
            age = int(age_str)
        except ValueError:
            age = age_str

        students.append({
            "name": name,
            "age": age,
            "grade": grade,
            "subject": subject.lower(),
        })
    return students

def analyze_grade_distribution(grades):

    dist = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for g in grades:
        if g >= 90:
            dist["A"] += 1
        elif g >= 80:
            dist["B"] += 1
        elif g >= 70:
            dist["C"] += 1
        elif g >= 60:
            dist["D"] += 1
        else:
            dist["F"] += 1
    return dist

def analyze_data(students):
    if not students:
        return {
            "total_students": 0,
            "average_grade": 0.0,
            "highest_grade": 0,
            "lowest_grade": 0,
            "grade_range": 0,
            "subject_counts": {},
            "grade_distribution": {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0},
            "grade_distribution_pct": {"A": 0.0, "B": 0.0, "C": 0.0, "D": 0.0, "F": 0.0},
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

    grades = [s["grade"] for s in students]
    total = len(students)
    avg = sum(grades) / len(grades) if grades else 0.0
    highest = max(grades) if grades else 0
    lowest = min(grades) if grades else 0

    # Per-subject counts
    subject_counts = {}
    for s in students:
        sub = s.get("subject", "").strip().lower()
        if not sub:
            continue
        subject_counts[sub] = subject_counts.get(sub, 0) + 1

    # Letter-grade distribution
    dist_counts = analyze_grade_distribution(grades)
    dist_pct = {k: ((v / total) * 100.0 if total else 0.0) for k, v in dist_counts.items()}

    return {
        "total_students": total,
        "average_grade": avg,
        "highest_grade": highest,
        "lowest_grade": lowest,
        "grade_range": highest - lowest,
        "subject_counts": subject_counts,
        "grade_distribution": dist_counts,
        "grade_distribution_pct": dist_pct,
    
    }


def save_results(results, filename="output/analysis_report.txt"):

    out_dir = os.path.dirname(filename) or "."
    os.makedirs(out_dir, exist_ok=True)

    with open(filename, "a", encoding="utf-8") as f: # append the advanced report to the old report
        f.write("COMPREHENSIVE STUDENT ANALYSIS REPORT\n")
        f.write("=" * 50 + "\n\n")

        f.write("BASIC STATISTICS\n")
        f.write("-" * 20 + "\n")
        f.write(f"Total students: {results['total_students']}\n")
        f.write(f"Average grade: {results['average_grade']:.1f}\n")
        f.write(f"Highest grade: {results['highest_grade']}\n")
        f.write(f"Lowest grade: {results['lowest_grade']}\n")
        f.write(f"Grade range: {results['grade_range']}\n\n")

        f.write("SUBJECT COUNTS\n")
        f.write("-" * 20 + "\n")
        if results["subject_counts"]:
            for subj in sorted(results["subject_counts"]):
                f.write(f"{subj.capitalize()}: {results['subject_counts'][subj]}\n")
        else:
            f.write("(none)\n")
        f.write("\n")

        f.write("GRADE DISTRIBUTION (Letter Grades)\n")
        f.write("-" * 35 + "\n")
        dist = results["grade_distribution"]
        pct = results["grade_distribution_pct"]
        for label in ["A", "B", "C", "D", "F"]:
            f.write(f"{label}: {dist[label]} ({pct[label]:.1f}%)\n")

    return True

def main():
    # Build paths relative to this file so it works from any CWD
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.join(base_dir, "..", "data", "students.csv")
    out_file = os.path.join(base_dir, "..", "output", "analysis_report.txt")

    students = load_data(data_file)
    results = analyze_data(students)
    save_results(results, out_file)
    print(f"Advanced report saved to {out_file}")


if __name__ == "__main__":
    main()