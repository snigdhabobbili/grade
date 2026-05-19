# main.py
# 🤝 SHARED FILE — both people import from here
# Don't edit this until you're ready to practice a merge conflict!

from report import print_student_report, print_class_summary
from grades import get_highest_mark, get_lowest_mark

# Sample data
students = {
    "Alice":   [88, 92, 79, 95],
    "Bob":     [60, 55, 70, 65],
    "Charlie": [30, 45, 38, 50],
    "Diana":   [100, 98, 95, 99],
}

if __name__ == "__main__":
    # Print individual report cards
    for name, marks in students.items():
        print_student_report(name, marks)
        print()

    # Print class summary
    print_class_summary(students)
    
test_marks = [88, 92, 79, 95]
print(f"Highest: {get_highest_mark(test_marks)}")   
print(f"Lowest:  {get_lowest_mark(test_marks)}")  

# -------------------------------------------------------
# 💥 CONFLICT EXERCISE (do this after both branches work):
#   Both of you change the line below to different things,
#   merge both branches, and watch Git flag the conflict!
#
TEAM_NAME = "Section B"   # ← both edit this line differently
# -------------------------------------------------------
