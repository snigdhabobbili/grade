# report.py
# ✏️  YOUR FRIEND'S FILE — they work on this one!
# This file handles printing and displaying results.

from grades import calculate_average, get_letter_grade, is_passing


def print_student_report(name: str, marks: list[float]) -> None:
    """Prints a formatted report card for a student."""
    average = calculate_average(marks)
    grade   = get_letter_grade(average)
    status  = "PASS ✅" if is_passing(average) else "FAIL ❌"

    print("=" * 35)
    print(f"  REPORT CARD — {name.upper()}")
    print("=" * 35)
    print(f"  Marks   : {marks}")
    print(f"  Average : {average:.1f}")
    print(f"  Grade   : {grade}")
    print(f"  Status  : {status}")
    print("=" * 35)


def print_class_summary(students: dict[str, list[float]]) -> None:
    """Prints a summary for the entire class."""
    print("\n📋 CLASS SUMMARY")
    print("-" * 35)
    for name, marks in students.items():
        avg = calculate_average(marks)
        grade = get_letter_grade(avg)
        print(f"  {name:<15} {avg:>5.1f}   [{grade}]")
    print("-" * 35)


# -------------------------------------------------------
# 🧪 TODO for YOUR FRIEND (you won't touch this file):
#   1. Add a function: print_topper(students) that prints
#      the student with the highest average
#   2. Add colour to the output using ANSI codes
#   3. Push to THEIR branch and open a Pull Request!
# -------------------------------------------------------
