

studentList = []
running = True


while running:
    # OUTPUT
    print("\n===== SCHOOL MANAGEMENT SYSTEM =====")
    print("1. Manage Students")
    print("2. View Records")
    print("3. Generate Reports")
    print("4. Exit")

    # INPUT
    mode = input("Select a mode: ").strip()

    
    if mode == "1":
        inSubMenu = True

        while inSubMenu:
            # OUTPUT
            print("\n--- Manage Students ---")
            print("1. Add Student")
            print("2. Remove Student")
            print("3. Update Grade")
            print("4. Back to Main Menu")

            # INPUT
            choice = input("Choose an option: ").strip()

            if choice == "1":
                # INPUT
                name = input("Student name: ").strip()
                studentID = input("Student ID: ").strip()
                gradeText = input("Student grade: ").strip()

                # PROCESS
                if gradeText.replace(".", "", 1).isdigit():
                    grade = float(gradeText)
                    studentList.append({"id": studentID, "name": name, "grade": grade})
                    # OUTPUT
                    print("Student added successfully.")
                else:
                    # OUTPUT
                    print("Invalid grade. Student not added.")

            elif choice == "2":
                # INPUT
                searchID = input("Enter ID of student to remove: ").strip()

                # PROCESS - iterate to find and remove the student
                found = False
                for student in studentList:
                    if student["id"] == searchID:
                        studentList.remove(student)
                        found = True
                        break

                # OUTPUT
                if found:
                    print("Student removed successfully.")
                else:
                    print("Student not found.")

            elif choice == "3":
                # INPUT
                searchID = input("Enter ID of student to update: ").strip()
                gradeText = input("New grade: ").strip()

                # PROCESS - iterate to find and update the student
                if gradeText.replace(".", "", 1).isdigit():
                    newGrade = float(gradeText)
                    found = False
                    for student in studentList:
                        if student["id"] == searchID:
                            student["grade"] = newGrade
                            found = True
                            break

                    # OUTPUT
                    if found:
                        print("Grade updated successfully.")
                    else:
                        print("Student not found.")
                else:
                    # OUTPUT
                    print("Invalid grade. Update cancelled.")

            elif choice == "4":
                # PROCESS - exit the submenu loop
                inSubMenu = False

            else:
                # OUTPUT
                print("Invalid option, try again.")


    elif mode == "2":
        inSubMenu = True

        while inSubMenu:
            # OUTPUT
            print("\n--- View Records ---")
            print("1. Search Student")
            print("2. Display All Students")
            print("3. Back to Main Menu")

            # INPUT
            choice = input("Choose an option: ").strip()

            if choice == "1":
                # INPUT
                term = input("Enter ID or name to search: ").strip()

                # PROCESS - iterate through all students looking for a match
                found = False
                for student in studentList:
                    if student["id"] == term or student["name"].lower() == term.lower():
                        # OUTPUT
                        print(f"ID: {student['id']} | Name: {student['name']} | Grade: {student['grade']}")
                        found = True

                # OUTPUT
                if not found:
                    print("Student not found.")

            elif choice == "2":
                # PROCESS / OUTPUT - iterate through every student in the list
                if len(studentList) == 0:
                    print("No students registered.")
                else:
                    for student in studentList:
                        print(f"ID: {student['id']} | Name: {student['name']} | Grade: {student['grade']}")

            elif choice == "3":
                # PROCESS - exit the submenu loop
                inSubMenu = False

            else:
                # OUTPUT
                print("Invalid option, try again.")

    elif mode == "3":
        # PROCESS - guard against empty list
        if len(studentList) == 0:
            # OUTPUT
            print("\nNo students registered, cannot generate report.")
        else:
            total = 0
            highest = studentList[0]["grade"]
            highestName = studentList[0]["name"]
            lowest = studentList[0]["grade"]
            lowestName = studentList[0]["name"]

            # PROCESS - iterate through all students once to accumulate statistics
            for student in studentList:
                total += student["grade"]

                if student["grade"] > highest:
                    highest = student["grade"]
                    highestName = student["name"]

                if student["grade"] < lowest:
                    lowest = student["grade"]
                    lowestName = student["name"]

            average = total / len(studentList)

            # OUTPUT
            print("\n--- Class Report ---")
            print(f"Class Average: {average:.2f}")
            print(f"Highest Grade: {highestName} ({highest})")
            print(f"Lowest Grade: {lowestName} ({lowest})")

    # ------------------------------------------------------------
    # MODE 4 - Exit
    # ------------------------------------------------------------
    elif mode == "4":
        # PROCESS
        running = False
        # OUTPUT
        print("Goodbye!")

    else:
        # OUTPUT
        print("Invalid option, try again.")