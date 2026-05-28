# ============================================
# SMART CAMPUS INFORMATION SYSTEM
# ============================================

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ============================================
# GLOBAL LIST
# ============================================

students = []

# ============================================
# MODULE 1 : STUDENT REGISTRATION
# ============================================

def register_student():

    print("\n===== STUDENT REGISTRATION =====")

    try:

        name = input("Enter Student Name : ")

        student_id = input("Enter Student ID : ")

        age = int(input("Enter Age : "))

        score = float(input("Enter Marks : "))

        # Grade Calculation
        if score >= 90:
            grade = "A"
            remark = "Excellent"

        elif score >= 75:
            grade = "B"
            remark = "Very Good"

        elif score >= 60:
            grade = "C"
            remark = "Good"

        elif score >= 40:
            grade = "D"
            remark = "Average"

        else:
            grade = "F"
            remark = "Fail"

        # Store Data
        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "score": score,
            "grade": grade,
            "remark": remark,
            "courses": []
        }

        students.append(student)

        print("\nStudent Registered Successfully!")

    except:
        print("Invalid Input!")

# ============================================
# MODULE 2 : COURSE ENROLLMENT
# ============================================

def enroll_course():

    print("\n===== COURSE ENROLLMENT =====")

    sid = input("Enter Student ID : ")

    found = False

    for student in students:

        if student["id"] == sid:

            found = True

            while True:

                course_name = input(
                    "Enter Course Name (done to stop) : "
                )

                if course_name.lower() == "done":
                    break

                try:

                    credits = int(
                        input("Enter Credits : ")
                    )

                    student["courses"].append(
                        (course_name, credits)
                    )

                    print("Course Added Successfully!")

                except:
                    print("Invalid Credits!")

    if found == False:
        print("Student Not Found!")

# ============================================
# MODULE 3 : DISPLAY STUDENT RECORDS
# ============================================

def display_records():

    print("\n===== STUDENT RECORDS =====")

    if len(students) == 0:

        print("No Records Available")
        return

    for student in students:

        print("\n--------------------------")

        print("Student ID :", student["id"])
        print("Name       :", student["name"])
        print("Age        :", student["age"])
        print("Marks      :", student["score"])
        print("Grade      :", student["grade"])
        print("Remark     :", student["remark"])

        print("Courses    :")

        if len(student["courses"]) == 0:
            print("No Courses Enrolled")

        else:

            for course in student["courses"]:

                print(
                    course[0],
                    "-",
                    course[1],
                    "Credits"
                )

# ============================================
# MODULE 4 : SORTING & SEARCHING
# ============================================

def sort_students():

    print("\n===== SORTED STUDENT IDs =====")

    if len(students) == 0:

        print("No Records Available")
        return

    ids = []

    for student in students:
        ids.append(student["id"])

    ids.sort()

    print(ids)

def search_student():

    print("\n===== SEARCH STUDENT =====")

    sid = input("Enter Student ID : ")

    found = False

    for student in students:

        if student["id"] == sid:

            found = True

            print("\nStudent Found")
            print("Name   :", student["name"])
            print("Marks  :", student["score"])
            print("Grade  :", student["grade"])

    if found == False:
        print("Student Not Found!")

# ============================================
# MODULE 5 : FEE CALCULATION
# ============================================

def calculate_fee(tuition, hostel=0, transport=0):

    total = tuition + hostel + transport

    return total

def fee_module():

    print("\n===== FEE CALCULATION =====")

    try:

        tuition = float(
            input("Enter Tuition Fee : ")
        )

        hostel = float(
            input("Enter Hostel Fee : ")
        )

        transport = float(
            input("Enter Transport Fee : ")
        )

        total = calculate_fee(
            tuition,
            hostel,
            transport
        )

        print("Total Fee =", total)

    except:
        print("Invalid Input!")

# ============================================
# MODULE 6 : FILE HANDLING
# ============================================

def save_records():

    with open(
        "student_records.txt",
        "w"
    ) as file:

        for student in students:

            file.write(
                f"{student['id']},"
                f"{student['name']},"
                f"{student['age']},"
                f"{student['score']},"
                f"{student['grade']}\n"
            )

    print("\nRecords Saved Successfully!")

def read_records():

    print("\n===== FILE RECORDS =====")

    try:

        with open(
            "student_records.txt",
            "r"
        ) as file:

            data = file.readlines()

            for line in data:
                print(line.strip())

    except:
        print("File Not Found!")

# ============================================
# MODULE 7 : DIRECTORY SCANNING
# ============================================

def scan_directory():

    print("\n===== DIRECTORY SCANNING =====")

    try:

        files = os.listdir()

        for file in files:
            print(file)

    except:
        print("Error While Scanning")

# ============================================
# MODULE 8 : PERFORMANCE ANALYSIS
# ============================================

def performance_analysis():

    print("\n===== PERFORMANCE ANALYSIS =====")

    if len(students) == 0:

        print("No Student Data Available")
        return

    names = []
    marks = []

    for student in students:

        names.append(student["name"])
        marks.append(student["score"])

    # Pandas DataFrame
    df = pd.DataFrame({

        "Name": names,
        "Marks": marks

    })

    print("\n===== STUDENT DATA =====")

    print(df)

    # NumPy Analysis
    arr = np.array(marks)

    print("\n===== ANALYSIS =====")

    print("Average :", np.mean(arr))
    print("Highest :", np.max(arr))
    print("Lowest  :", np.min(arr))
    print("Median  :", np.median(arr))

    # Save CSV
    df.to_csv(
        "student_analysis.csv",
        index=False
    )

    print("\nCSV File Saved Successfully!")

    # Graph
    plt.figure(figsize=(7,5))

    plt.bar(names, marks)

    plt.title(
        "Student Performance Analysis"
    )

    plt.xlabel("Student Name")
    plt.ylabel("Marks")

    plt.savefig("student_graph.png")

    print("Graph Saved Successfully!")

# ============================================
# MAIN MENU
# ============================================

def main():

    while True:

        print("\n================================")
        print(" SMART CAMPUS INFORMATION SYSTEM ")
        print("================================")

        print("1. Student Registration")
        print("2. Course Enrollment")
        print("3. Display Records")
        print("4. Sort Student IDs")
        print("5. Search Student")
        print("6. Fee Calculation")
        print("7. Save Records")
        print("8. Read Records")
        print("9. Directory Scanning")
        print("10. Performance Analysis")
        print("11. Exit")

        choice = input(
            "\nEnter Your Choice : "
        )

        if choice == "1":
            register_student()

        elif choice == "2":
            enroll_course()

        elif choice == "3":
            display_records()

        elif choice == "4":
            sort_students()

        elif choice == "5":
            search_student()

        elif choice == "6":
            fee_module()

        elif choice == "7":
            save_records()

        elif choice == "8":
            read_records()

        elif choice == "9":
            scan_directory()

        elif choice == "10":
            performance_analysis()

        elif choice == "11":

            print(
                "\nExiting Smart Campus System..."
            )

            break

        else:
            print("Invalid Choice!")

# ============================================
# PROGRAM STARTS HERE
# ============================================

main()

