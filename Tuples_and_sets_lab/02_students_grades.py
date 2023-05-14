students_count = int(input())

students_data = {}

for _ in range(students_count):
    name, grade = input().split()
    grade = float(grade)

    if name not in students_data.keys():
        students_data[name] = []
    students_data[name].append(grade)

for student, grades in students_data.items():
    average_grade = sum(grades) / len(grades)
    print(f"{student} -> {' '.join(str(f'{x:.2f}') for x in grades)} (avg: {average_grade:.2f})")