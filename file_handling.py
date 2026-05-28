import os


def file_demo():

    os.makedirs("data", exist_ok=True)

    file = open("data/student_records.txt", "w")

    file.write("ID,Name,Marks\n")
    file.write("101,Rahul,89\n")
    file.write("102,Priya,95\n")

    file.close()

    print("Data written successfully!")

    file = open("data/student_records.txt", "r")

    print("\nStored Records:\n")

    print(file.read())

    file.close()