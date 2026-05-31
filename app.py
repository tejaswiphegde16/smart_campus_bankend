
import os
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

students = []
student_ids = []

def load_students():
    students.clear()
    student_ids.clear()
    try:
        with open("students.csv", "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = {
                    "id": int(row["ID"]),
                    "name": row["Name"],
                    "score": float(row["Score"]),
                    "grade": row["Grade"],
                    "remark": row["Remark"]
                }
                students.append(student)
                student_ids.append(student["id"])
    except FileNotFoundError:
        with open("students.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Score", "Grade", "Remark"])

def save_student(student):
    with open("students.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            student["id"], student["name"], student["score"],
            student["grade"], student["remark"]
        ])

def register_student():
    print("\n=== Student Registration ===")

    while True:
        try:
            sid = int(input("Enter Student ID: "))
            break
        except ValueError:
            print("Student ID must be a number!")

    name = input("Enter Student Name: ")

    while True:
        try:
            score = float(input("Enter Exam Score (0-100): "))
            if 0 <= score <= 100:
                break
            print("Score must be between 0 and 100.")
        except ValueError:
            print("Score must be a number!")

    if score >= 90:
        grade, remark = "A", "Excellent"
    elif score >= 75:
        grade, remark = "B", "Very Good"
    elif score >= 60:
        grade, remark = "C", "Good"
    elif score >= 40:
        grade, remark = "D", "Average"
    else:
        grade, remark = "F", "Needs Improvement"

    student = {
        "id": sid,
        "name": name,
        "score": score,
        "grade": grade,
        "remark": remark
    }

    students.append(student)
    student_ids.append(sid)
    save_student(student)

    print("Student Registered Successfully!")

def course_enrollment():
    courses = []
    while len(courses) < 5:
        course = input("Enter Course Name (or done): ")
        if course.lower() == "done":
            break

        credits = input("Enter Credits: ")
        if not credits.isdigit() or int(credits) <= 0:
            print("Invalid credits.")
            continue

        courses.append((course, int(credits)))

    print("\nCourses:")
    for c, cr in courses:
        print(c, "-", cr)

def student_records():
    if not students:
        print("No Student Records Available")
        return

    for s in students:
        print("-" * 25)
        print("ID:", s["id"])
        print("Name:", s["name"])
        print("Score:", s["score"])
        print("Grade:", s["grade"])
        print("Remark:", s["remark"])

def search_sort():
    if not student_ids:
        print("No IDs Available")
        return

    ids = sorted(student_ids)
    print("Sorted IDs:", ids)

    try:
        target = int(input("Enter ID to Search: "))
        if target in ids:
            print("ID Found")
        else:
            print("ID Not Found")
    except ValueError:
        print("Invalid ID")

def calculate_fee():
    try:
        tuition = float(input("Tuition Fee: "))
        hostel = float(input("Hostel Fee: "))
        transport = float(input("Transport Fee: "))
        print("Total Fee =", tuition + hostel + transport)
    except ValueError:
        print("Enter valid numbers.")

def file_handling():
    try:
        with open("students.csv", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("students.csv not found")

class MissingFolderError(Exception):
    pass

def directory_scan():
    path = input("Enter Directory Path: ")
    try:
        if not os.path.exists(path):
            raise FileNotFoundError

        for root, dirs, files in os.walk(path):
            print(root)
            for f in files:
                print("  ", f)

            if not dirs and not files:
                raise MissingFolderError("Empty Folder Found")

    except FileNotFoundError:
        print("Invalid Directory Path")
    except MissingFolderError as e:
        print(e)

def performance_analytics():
    data = {
        "Name": ["Rahul", "Priya", "Anita"],
        "Math": [80, 90, 95],
        "Science": [85, 88, 92],
        "English": [75, 91, 89]
    }

    df = pd.DataFrame(data)
    print(df)
    print(df.describe())

    scores = df[["Math", "Science", "English"]].to_numpy()
    means = np.mean(scores, axis=0)

    plt.bar(["Math", "Science", "English"], means)
    plt.title("Average Scores")
    plt.show()

load_students()

while True:
    print("\n===== SMART CAMPUS INFORMATION SYSTEM =====")
    print("1. Student Registration")
    print("2. Course Enrollment")
    print("3. Student Records")
    print("4. Search and Sort Student IDs")
    print("5. Fee Calculation")
    print("6. File Handling")
    print("7. Directory Scan")
    print("8. Performance Analytics")
    print("9. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        register_student()
    elif choice == "2":
        course_enrollment()
    elif choice == "3":
        student_records()
    elif choice == "4":
        search_sort()
    elif choice == "5":
        calculate_fee()
    elif choice == "6":
        file_handling()
    elif choice == "7":
        directory_scan()
    elif choice == "8":
        performance_analytics()
    elif choice == "9":
        break
    else:
        print("Invalid Choice")
