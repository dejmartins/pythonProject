student_1 = [56, 29, 48]
student_2 = [73, 27, 73]
student_3 = [47, 38, 48]

print(list(zip(student_1, student_2, student_3, strict=True)))

s_scores = [max(subject) for subject in zip(student_1, student_2, student_3)]
print(s_scores)

s_slice = slice(1, 4)
print("Hello"[s_slice])