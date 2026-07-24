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
# LOGIN - retry on wrong credentials, then act once per role
# ============================================================
while True:
    # OUTPUT
    print("\n===== SCHOOL MANAGEMENT SYSTEM - LOGIN =====")

    # INPUT
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    # PROCESS - validate credentials
    if username in users and users[username]['password'] == password:
        break

    # OUTPUT
    print("Wrong user/password!")

role = users[username]['rol']
name = users[username]['name']

# OUTPUT
print(f"\nBienvenid@!, {name} ({role})")

# ============================================================
# MODE 1 - STUDENT: show the report and end
# ============================================================
if role == "student":
    # PROCESS - split this student's subjects into Approved / Pending
    approved = set()
    pending = set()
    for subject in subjects:
        if subject in notes[username]:
            if notes[username][subject] >= 7.0:
                approved.add(subject)
            else:
                pending.add(subject)

    # OUTPUT
    print("\n=== School Report ===")
    print("Approved:", approved)
    print("Pending:", pending)

# ============================================================
# MODE 2 - PROFESSOR: grade one student on one subject, then end
# ============================================================
elif role == "professor":
    # OUTPUT
    print("\n=== Students ===")
    for uname, info in users.items():
        if info['rol'] == 'student':
            print(f"  {info['name']} ({uname})")

    print("\n=== Subjects ===")
    for subject in subjects:
        print(f"  {subject}")

    # INPUT
    targetUser = input("Student username: ").strip()
    subjectName = input("Subject: ").strip()
    newGrade = input("New grade: ").strip()

    # PROCESS - validate the student, the subject, and the grade
    if targetUser not in notes:
        # OUTPUT
        print("Ese usuario no existe")
    elif subjectName not in notes[targetUser]:
        # OUTPUT
        print("Esa materia no existe")
    else:
        try:
            newGradeValue = float(newGrade)
        except ValueError:
            # OUTPUT
            print("La calificación debe ser un número")
        else:
            if not (0 <= newGradeValue <= 10):
                # OUTPUT
                print("La calificación debe estar entre 0 y 10")
            else:
                oldGrade = notes[targetUser][subjectName]

                # OUTPUT
                print("\nDo you confirm (yes/no)?")
                print(f"   {subjectName}: {oldGrade} ==> {newGradeValue}")

                # INPUT
                confirm = input().strip().lower()

                # PROCESS / OUTPUT
                if confirm == "yes":
                    notes[targetUser][subjectName] = newGradeValue
                    print("Grade updated.")
                elif confirm == "no":
                    print("Update cancelled.")

# ============================================================
# MODE 3 - COORDINATOR: show all three tables and end
# ============================================================
elif role == "coordinator":
    # OUTPUT
    print("\n=== Professors ===")
    for uname, info in users.items():
        if info['rol'] == 'professor':
            print(f"  {info['name']} ({uname})")

    print("\n=== Students ===")
    for uname, info in users.items():
        if info['rol'] == 'student':
            print(f"  {info['name']} ({uname})")

    print("\n=== Records ===")
    for uname in notes:
        print(f"  {users[uname]['name']}:")
        for subject in subjects:
            if subject in notes[uname]:
                print(f"    {subject}: {notes[uname][subject]}")
