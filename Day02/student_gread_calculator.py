#Function to calculate grade on the bases of average marks.
def cal_grade(marks):
    average = sum(marks) / len(marks)

    if average >= 95:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    return average, grade



marks = []
for i in range(4):
    score = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(score)

average, grade = cal_grade(marks)

print(f"\nAverage Marks: {average:.2f}")
print(f"Final Grade: {grade}")
