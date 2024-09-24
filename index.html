def calculate_grades(absences, prelim_exam, quizzes, requirements, recitation):
    # Input validation
    if absences < 0:
        return "Error: Absences cannot be negative."
    if absences >= 4:
        return "FAILED due to absences."

    if not (0 <= prelim_exam <= 100) or not (0 <= quizzes <= 100) or not (0 <= requirements <= 100) or not (0 <= recitation <= 100):
        return "Error: All grades must be between 0 and 100."

    # Attendance calculation
    attendance = 100 - (absences * 10)

    # Class standing calculation
    class_standing = (0.40 * quizzes) + (0.30 * requirements) + (0.30 * recitation)

    # Prelim grade calculation
    prelim_grade = (0.60 * prelim_exam) + (0.10 * attendance) + (0.30 * class_standing)

    # Target midterm and final grades for passing (75%) and Dean's List (90%)
    prelim_percent = 0.20
    midterm_percent = 0.30
    final_percent = 0.50
    passing_grade = 75
    deans_list_grade = 90

    # Current total from prelim grade
    current_total = prelim_grade * prelim_percent

    # Required midterm and final grades to pass with 75%
    required_total_for_75 = passing_grade - current_total
    if required_total_for_75 > 0:
        required_midterm_and_final_75 = required_total_for_75 / (midterm_percent + final_percent)
    else:
        required_midterm_and_final_75 = 0

    # Required midterm and final grades to achieve 90%
    required_total_for_90 = deans_list_grade - current_total
    if required_total_for_90 > 0:
        required_midterm_and_final_90 = required_total_for_90 / (midterm_percent + final_percent)
    else:
        required_midterm_and_final_90 = 0

    # Output the results
    results = f"""
    Prelim Grade: {prelim_grade:.2f}%
    To pass with 75%, you need a Midterm grade of {required_midterm_and_final_75:.2f}% and a Final grade of {required_midterm_and_final_75:.2f}%.

    To achieve 90%, you need a Midterm grade of {required_midterm_and_final_90:.2f}% and a Final grade of {required_midterm_and_final_90:.2f}%.
    """
    return results


# Example usage
absences = int(input("Enter Number of Absences: "))
prelim_exam = float(input("Enter Prelim Exam Grade (0-100): "))
quizzes = float(input("Enter Quizzes Grade (0-100): "))
requirements = float(input("Enter Requirements Grade (0-100): "))
recitation = float(input("Enter Recitation Grade (0-100): "))

result = calculate_grades(absences, prelim_exam, quizzes, requirements, recitation)
print(result)
