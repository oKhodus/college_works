def user_input(first_name, grades):
    first_name = first_name.capitalize()
    grades = grades.upper()
    return first_name, grades


def calc_quantity(grades):
    a_grade = grades.count("A")
    b_grade = grades.count("B")

    sum_anb = a_grade + b_grade
    total_grades = len(grades)
    sec_grade = grades[1] if total_grades > 1 else "No second grade"

    return sum_anb, total_grades, sec_grade


def output():
    first_name_inp = input("Enter first name: ")
    grades_inp = input("Enter grades: ")

    first_name, grades = user_input(first_name_inp, grades_inp)

    sum_anb, total_grades, sec_grade = calc_quantity(grades)

    output_message = (
        f"Hello {first_name}, your grades are {grades}.\n"
        f"You have {total_grades} grades.\n"
        f"Your grade for the second course is {sec_grade}.\n"
        f"The number of A's and B's is {sum_anb}.\n"
    )

    print(output_message)


output()
