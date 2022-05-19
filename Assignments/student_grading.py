number_of_students = int(input("How many students would you like to input for: "))
number_of_subjects = int(input("How many subjects do they offer: "))

print("\n" * 15)
print("Input the names of subjects:")
names_of_subjects = [str(input("Subject name: ")) for subject in range(number_of_subjects)]

print("\n" * 15)

lst_of_students_details = []
print("Input student details:")
print("Input first name only, and score for each subject")
counter = 0
while counter < number_of_students:
    student_dict = {"name": str(input("Name of student: "))}
    for subject in names_of_subjects:
        student_dict[subject] = int(input(f'{subject:s}: '))
    lst_of_students_details.append(student_dict)
    print()
    counter += 1


for student in lst_of_students_details:
    total = 0
    for subject in names_of_subjects:
        total += student[subject]
    print(total, end=" ")
    print(total / len(subject))


print(lst_of_students_details)




# student_sum = {'sum': total}
#     lst_of_students_details.append(student.update(student_sum))

# for subject_name in names_of_subjects:
#     print("Enter scores per subject:")
#     print(subject_name, end=": ")
#     student_grades = [{}]  input()
