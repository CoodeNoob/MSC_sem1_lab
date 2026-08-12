name: str = "Swan Htet Pyae Sone"
age: int = 23
height: float = 1.56
is_student: bool = True 
born_year: int = 2002
academic_start_year: int = 2026
current_year: int = 2026

def description(name: str, age: int, height: float, is_student: bool, born_year: int, academic_start_year: int):
    """
    Prints a detailed description of a person based on their attributes.
    """
    graduation_year = academic_start_year + 2
    
   
    student_status = "currently a student" if is_student else "not a student"
    
   
    print(f"Name: {name}")
    print(f"Age: {age} years old")
    print(f"Height: {height} meters")
    print(f"Born in: {born_year}")
    print(f"Student status: {student_status}")
    print(f"Academic start year: {academic_start_year}")
    print(f"Expected graduation year: {graduation_year}")
    print(f"Current year: {current_year}")
    print("-" * 40)
    
    
    years_until_graduation = graduation_year - current_year
    if years_until_graduation > 0:
        print(f"Years until graduation: {years_until_graduation}")
    elif years_until_graduation == 0:
        print("Graduating this year!")
    else:
        print(f"Graduated {abs(years_until_graduation)} years ago")
    
    calculated_age = current_year - born_year
    if calculated_age == age:
        print(f"Age verification: Age matches birth year (born {born_year})")
    else:
        print(f"Age mismatch: Born in {born_year} would make you {calculated_age}, but age is listed as {age}")

description(name, age, height, is_student, born_year, academic_start_year)