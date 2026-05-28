from student_registration import register_student
from course_enrollment import enroll_courses
from student_records import manage_student_records
from sorting_searching import sorting_searching_demo
from fee_calculation import fee_demo
from file_handling import file_demo
from directory_scanner import scan_demo
from performance_analysis import performance_demo

def main():

    while True:
        print("\n===== SMART CAMPUS INFORMATION SYSTEM =====")
        print("1. Student Registration")
        print("2. Course Enrollment")
        print("3. Student Records")
        print("4. Sorting and Searching")
        print("5. Fee Calculation")
        print("6. File Handling")
        print("7. Directory Scanner")
        print("8. Performance Analysis")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_student()

        elif choice == "2":
            enroll_courses()

        elif choice == "3":
            manage_student_records()

        elif choice == "4":
            sorting_searching_demo()

        elif choice == "5":
            fee_demo()

        elif choice == "6":
            file_demo()

        elif choice == "7":
            scan_demo()

        elif choice == "8":
            performance_demo()

        elif choice == "9":
            print("Exiting Smart Campus System...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()