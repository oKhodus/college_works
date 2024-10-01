def pass_mark(student_mark):
    try:
        if 66 <= int(student_mark) <= 100:
            return str("The obtained points are enough to be considered for admission.")
        elif 0 < int(student_mark) < 66:
            return str("The obtained points are not enough to be considered for admission.")
        elif int(student_mark) < 0:
            return str("You cannot obtain negative points.")
        elif int(student_mark) > 100:
            return str("You cannot obtain so many points.")
    except ValueError:
        return str("We expect a numeric value to be entered.")

student_mark = input("Enter a number of points: ")
print(pass_mark(student_mark))