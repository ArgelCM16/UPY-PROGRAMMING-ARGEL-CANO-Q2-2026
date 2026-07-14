
users = {
    'jperez':  {'password': '1234', 'rol': 'student',     'name': 'Juan Pérez'},
    'dromo':   {'password': '1234', 'rol': 'student',     'name': 'Daniela Romo'},
    'mjuarez': {'password': '1234', 'rol': 'student',     'name': 'Mauricio Juárez'},
    'mlopez':  {'password': '1234', 'rol': 'student',     'name': 'María López'},
    'euc':     {'password': '1234', 'rol': 'student',     'name': 'Ernesto Uc'},
    'cbalam':  {'password': '1234', 'rol': 'student',     'name': 'Carlos Balam'},
    'jpedrozo':{'password': '1234', 'rol': 'professor',   'name': 'Jorge Pedrozo'},
    'dgamboa': {'password': '1234', 'rol': 'coordinator', 'name': 'Didier Gamboa'}
}

subjects = (
    "Discrete Mathematics",
    "Programming",
    "English II",
    "Differential Calculus",
    "Probability and Statistics",
    "Computer and Server Architecture",
    "Socio-Emotional Skills and Conflict Management"
)

notes = {
    'jperez': {
        'Discrete Mathematics': 8.5, 'Programming': 9.2, 'English II': 9.0,
        'Differential Calculus': 7.8, 'Probability and Statistics': 8.3,
        'Computer and Server Architecture': 6.8,
        'Socio-Emotional Skills and Conflict Management': 9.5
    },
    'dromo': {
        'Discrete Mathematics': 9.0, 'Programming': 6.7, 'English II': 9.4,
        'Differential Calculus': 6.2, 'Probability and Statistics': 9.1,
        'Computer and Server Architecture': 6.5,
        'Socio-Emotional Skills and Conflict Management': 9.8
    },
    'mjuarez': {
        'Discrete Mathematics': 7.5, 'Programming': 8.0, 'English II': 8.5,
        'Differential Calculus': 7.0, 'Probability and Statistics': 7.8,
        'Computer and Server Architecture': 6.2,
        'Socio-Emotional Skills and Conflict Management': 8.9
    },
    'mlopez': {
        'Discrete Mathematics': 9.5, 'Programming': 9.8, 'English II': 9.2,
        'Differential Calculus': 9.0, 'Probability and Statistics': 9.6,
        'Computer and Server Architecture': 9.4,
        'Socio-Emotional Skills and Conflict Management': 10.0
    },
    'euc': {
        'Discrete Mathematics': 8.2, 'Programming': 6.9, 'English II': 8.8,
        'Differential Calculus': 6.0, 'Probability and Statistics': 6.4,
        'Computer and Server Architecture': 8.1,
        'Socio-Emotional Skills and Conflict Management': 9.0
    },
    'cbalam': {
        'Discrete Mathematics': 8.8, 'Programming': 9.0, 'English II': 8.5,
        'Differential Calculus': 6.6, 'Probability and Statistics': 8.9,
        'Computer and Server Architecture': 8.7,
        'Socio-Emotional Skills and Conflict Management': 9.2
    }
}

# ============================================================
# MAIN PROGRAM LOOP - login, then branch into one of 3 modes
# ============================================================
runningApp = True

while runningApp:
    # OUTPUT
    print("\n===== SCHOOL MANAGEMENT SYSTEM - LOGIN =====")

    # INPUT
    username = input("Username (or 'exit' to quit): ").strip()

    if username.lower() == "exit":
        # PROCESS
        runningApp = False
        # OUTPUT
        print("Goodbye!")
        continue

    # INPUT
    password = input("Password: ").strip()

    # PROCESS - validate credentials
    if username in users and users[username]['password'] == password:
        role = users[username]['rol']
        name = users[username]['name']

        # OUTPUT
        print(f"\nWelcome, {name}! ({role.upper()} mode)")
        loggedIn = True

        # --------------------------------------------------------
        # MODE 1 - STUDENT
        # --------------------------------------------------------
        while loggedIn and role == "student":
            # OUTPUT
            print("\n--- Student Menu ---")
            print("1. View My Grades")
            print("2. View My Average")
            print("3. Logout")

            # INPUT
            choice = input("Choose an option: ").strip()

            if choice == "1":
                # PROCESS / OUTPUT - iterate through this student's subjects
                print(f"\nGrades for {name}:")
                for subject in subjects:
                    if subject in notes[username]:
                        print(f"  {subject}: {notes[username][subject]}")

            elif choice == "2":
                # PROCESS - iterate to accumulate the total
                total = 0
                for grade in notes[username].values():
                    total += grade
                average = total / len(notes[username])

                # OUTPUT
                print(f"\nYour average grade is: {average:.2f}")

            elif choice == "3":
                # PROCESS
                loggedIn = False

            else:
                # OUTPUT
                print("Invalid option, try again.")

        # --------------------------------------------------------
        # MODE 2 - PROFESSOR
        # --------------------------------------------------------
        while loggedIn and role == "professor":
            # OUTPUT
            print("\n--- Professor Menu ---")
            print("1. View a Student's Grades")
            print("2. Update a Student's Grade")
            print("3. List Subjects")
            print("4. Logout")

            # INPUT
            choice = input("Choose an option: ").strip()

            if choice == "1":
                # INPUT
                targetUser = input("Student username: ").strip()

                # PROCESS / OUTPUT - iterate through that student's grades
                if targetUser in notes:
                    print(f"\nGrades for {users[targetUser]['name']}:")
                    for subject in subjects:
                        if subject in notes[targetUser]:
                            print(f"  {subject}: {notes[targetUser][subject]}")
                else:
                    print("Student not found.")

            elif choice == "2":
                # INPUT
                targetUser = input("Student username: ").strip()

                if targetUser in notes:
                    print("\nAvailable subjects:")
                    # PROCESS / OUTPUT - iterate to display the subject list
                    subjectIndex = 1
                    for subject in subjects:
                        print(f"  {subjectIndex}. {subject}")
                        subjectIndex += 1

                    # INPUT
                    subjectChoice = input("Enter the subject name exactly as shown: ").strip()

                    # PROCESS - validate the subject exists
                    if subjectChoice in subjects:
                        gradeText = input("New grade: ").strip()
                        if gradeText.replace(".", "", 1).isdigit():
                            notes[targetUser][subjectChoice] = float(gradeText)
                            # OUTPUT
                            print("Grade updated successfully.")
                        else:
                            print("Invalid grade. Update cancelled.")
                    else:
                        print("Subject not found.")
                else:
                    print("Student not found.")

            elif choice == "3":
                # PROCESS / OUTPUT - iterate through the subjects tuple
                print("\nSubjects offered:")
                for subject in subjects:
                    print(f"  - {subject}")

            elif choice == "4":
                # PROCESS
                loggedIn = False

            else:
                # OUTPUT
                print("Invalid option, try again.")

        # --------------------------------------------------------
        # MODE 3 - COORDINATOR
        # --------------------------------------------------------
        while loggedIn and role == "coordinator":
            # OUTPUT
            print("\n--- Coordinator Menu ---")
            print("1. View All Students and Averages")
            print("2. View Average by Subject")
            print("3. Search a Student")
            print("4. Logout")

            # INPUT
            choice = input("Choose an option: ").strip()

            if choice == "1":
                # PROCESS / OUTPUT - iterate through every student in notes
                print("\n--- All Students ---")
                for studentUser in notes:
                    total = 0
                    for grade in notes[studentUser].values():
                        total += grade
                    average = total / len(notes[studentUser])
                    studentName = users[studentUser]['name']
                    print(f"  {studentName} ({studentUser}): average = {average:.2f}")

            elif choice == "2":
                # PROCESS / OUTPUT - iterate through every subject, then every student
                print("\n--- Average by Subject ---")
                for subject in subjects:
                    subjectTotal = 0
                    subjectCount = 0
                    for studentUser in notes:
                        if subject in notes[studentUser]:
                            subjectTotal += notes[studentUser][subject]
                            subjectCount += 1
                    if subjectCount > 0:
                        subjectAverage = subjectTotal / subjectCount
                        print(f"  {subject}: {subjectAverage:.2f}")

            elif choice == "3":
                # INPUT
                targetUser = input("Student username: ").strip()

                # PROCESS / OUTPUT
                if targetUser in users:
                    print(f"\nName: {users[targetUser]['name']}")
                    print(f"Role: {users[targetUser]['rol']}")
                    if targetUser in notes:
                        print("Grades:")
                        for subject in subjects:
                            if subject in notes[targetUser]:
                                print(f"  {subject}: {notes[targetUser][subject]}")
                else:
                    print("User not found.")

            elif choice == "4":
                # PROCESS
                loggedIn = False

            else:
                # OUTPUT
                print("Invalid option, try again.")

    else:
        # OUTPUT
        print("Invalid username or password. Try again.")