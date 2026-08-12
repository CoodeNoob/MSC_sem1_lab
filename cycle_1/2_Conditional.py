student_marks = [50, 20, 80, 90, 30, 45, 60, 70, 55]

print(f"Marks list: {student_marks}\n")

for mark in student_marks:
    # Determine the grade/status based on marks
    if mark > 80:
        status = "Distinction"
    elif mark > 65:
        status = "Merit"
    elif mark > 45:
        status = "Pass"
    else:
        status = "Fail"
    
    print(f"Mark: {mark:>3}  ->  {status}")