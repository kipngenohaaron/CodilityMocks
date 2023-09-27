def gradingStudents(grades):
    rounded_grades = []
    for grade in grades:
        if grade < 38:
            # If the grade is less than 38, no rounding is needed.
            rounded_grades.append(grade)
        else:
            # Calculate the next multiple of 5 greater than or equal to the grade.
            next_multiple_of_5 = ((grade + 4) // 5) * 5
            if next_multiple_of_5 - grade < 3:
                # If the difference is less than 3, round up to the next multiple of 5.
                rounded_grades.append(next_multiple_of_5)
            else:
                # Otherwise, keep the grade as is.
                rounded_grades.append(grade)
    return rounded_grades

# Input
n = int(input().strip())
grades = []
for _ in range(n):
    grade = int(input().strip())
    grades.append(grade)

# Call the gradingStudents function to get rounded grades
rounded_grades = gradingStudents(grades)

# Output the rounded grades
for grade in rounded_grades:
    print(grade)
