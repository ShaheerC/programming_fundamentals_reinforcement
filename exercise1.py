def grade_out(grade):
    return "Your grade is {}.".format(grade)

def grade_in(percent):
    user_num = int(input("What is your grade?"))

    if user_num > 100:
        grade = "not possible"
        return grade_out(grade)
    elif user_num > 94:
        grade = "A+"
        return grade_out(grade)
    elif user_num > 84:
        grade = "A"
        return grade_out(grade)
    elif user_num > 74:
        grade = 'A-'
        return grade_out(grade)
    elif user_num > 64:
        grade = 'B+'
        return grade_out(grade)
    elif user_num > 49:
        grade = 'B'
        return grade_out(grade)
    else:
        return 'You have failed.'

print(grade_in(1))