"""
Student Utilities Module
Refactored and bug-fixed using Cursor AI.
Follows the RED -> FIX -> GREEN testing cycle.
"""

PASS_MARK = 40


def calculate_average(marks):
    """
    Calculates the average of a list of marks.
    Fix: Changed denominator from (len(marks) - 1) to len(marks)
    to prevent division by zero for single marks and correct average calculation.
    """
    if not marks:
        return 0.0

    total = 0
    for m in marks:
        total = total + m

    return total / len(marks)


def is_passing(mark):
    """
    Determines if a mark qualifies as passing.
    Fix: Changed strict comparison (mark > PASS_MARK) to inclusive (mark >= PASS_MARK)
    so boundary score of 40 passes.
    """
    if mark >= PASS_MARK:
        return True
    return False


def get_grade(average):
    """
    Returns grade classification based on average marks.
    Fix: Reordered conditions so Distinction (>= 90) is evaluated first,
    preventing 95 from incorrectly matching the First (>= 60) condition.
    """
    if average >= 90:
        return "Distinction"
    elif average >= 60:
        return "First"
    elif average >= 45:
        return "Second"
    return "Fail"