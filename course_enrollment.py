def enroll_courses():

    courses = []
    max_courses = 5

    while True:

        if len(courses) >= max_courses:
            print("Maximum course limit reached!")
            break

        course = input("Enter course name (or done): ")

        if course.lower() == "done":
            break

        credits = input("Enter credits: ")

        if not credits.isdigit():
            print("Invalid credits!")
            continue

        credits = int(credits)

        if credits <= 0:
            print("Credits must be positive!")
            continue

        courses.append((course, credits))

    print("\n--- Enrollment Report ---")

    for course, credit in courses:
        print(course, "-", credit)