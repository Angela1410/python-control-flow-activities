score = float(input("Enter student's score: "))

if score >= 90:
    grade = "Excellent"
elif score >= 75:
    grade = "Good"
elif score >= 60:
    grade = "Pass"
else:
    grade = "Fail"

print(f"Grade: {grade}")