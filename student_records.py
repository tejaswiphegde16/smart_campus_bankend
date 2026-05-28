def manage_student_records():

    students = []

    n = int(input("How many students? "))

    for _ in range(n):

        name = input("Enter name: ")
        age = int(input("Enter age: "))

        grades = []

        for i in range(3):
            marks = int(input(f"Enter mark {i+1}: "))
            grades.append(marks)

        students.append({
            "name": name,
            "age": age,
            "grades": grades
        })

    print("\n=== Student Records ===")

    for student in students:
        print(student)