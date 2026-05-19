# grades.py
# ✏️  YOUR FILE — work on this one!
# This file handles all the grade calculations.

def calculate_average(marks: list[float]) -> float:
    """Returns the average of a list of marks."""
    if not marks:
        return 0.0
    return sum(marks) / len(marks)


def get_letter_grade(average: float) -> str:
    """Converts a numeric average to a letter grade."""
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def is_passing(average: float) -> bool:
    """Returns True if the student is passing (average >= 40)."""
    return average >= 40


# -------------------------------------------------------
# 🧪 TODO for YOU (your friend won't touch this file):
#   1. Add a function: get_highest_mark(marks) -> float
#   2. Add a function: get_lowest_mark(marks) -> float
#   3. Push to YOUR branch and open a Pull Request!
# -------------------------------------------------------
