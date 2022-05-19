number_of_students = int(input("How many students would you like to input for: "))
number_of_subjects = int(input("How many subjects do they offer: "))

student_counter = 0
grade_list = []
grades_per_student_list = []
student_position = []


def calculate_student_total(index):
    total = 0
    for score in range(number_of_subjects):
        total += grade_list[index][score]
    return total


def calculate_student_average(index):
    total = calculate_student_total(index)
    average = total / number_of_subjects
    return average


# def calculate_student_position(index):
#     total = calculate_student_total(index)
#     student_position.append(total)
#     student_position.sort(reverse=True)


print("\n" * 15)
while student_counter < number_of_students:
    print("Student", (student_counter + 1))

    subject_counter = 0
    while subject_counter < number_of_subjects:
        print("Subject", (subject_counter + 1), end=": ")
        grade = int(input())
        grades_per_student_list.append(grade)
        subject_counter += 1

    grade_list.append(grades_per_student_list)
    grades_per_student_list = []
    student_counter += 1
    print("\n" * 15)

print(" " * 9, end="")
for subject in range(number_of_subjects):
    print(f'{"SUB":s}{subject + 1:d}', end="  ")
print(f'{"TOT":>4s} {"AVG":>4s} {"POS":>4s}')


for student in range(len(grade_list)):
    print("Student", student + 1, end="   ")
    student_total = calculate_student_total(student)
    student_average = calculate_student_average(student)
    student_position.append(student_total)
    student_position.sort(reverse=True)
    for subject in range(len(grade_list[student])):
        print(f'{grade_list[student][subject]:<4d}', end=" ")
    print(student_total, end="  ")
    print(student_average, end="  ")
    print(student_position.index(student_total), end="")
    print()

print(student_position)



# if __name__ == '__main__':
#     pass