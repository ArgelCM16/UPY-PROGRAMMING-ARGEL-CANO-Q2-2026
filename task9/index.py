"""
Spanish Verb Conjugator - Regular Verbs Only
Core logic and functions (No interactive main menu)
"""

import random

# -------------------------------------------------------------
# INPUT (static data used by the whole program)
# -------------------------------------------------------------
PERSONS = ["yo", "tú", "él/ella", "nosotros", "vosotros", "ellos/ellas"]

REGULAR_ENDINGS = {
    "ar": ["o", "as", "a", "amos", "áis", "an"],
    "er": ["o", "es", "e", "emos", "éis", "en"],
    "ir": ["o", "es", "e", "imos", "ís", "en"],
}

ALL_KNOWN_VERBS = [
    "hablar", "caminar", "estudiar", "cantar", "bailar", 
    "comer", "beber", "correr", "aprender", "leer",
    "vivir", "escribir", "abrir", "decidir", "subir"
]


# -------------------------------------------------------------
# PROCESS (core conjugation logic)
# -------------------------------------------------------------
def get_conjugation(verb, person_index):
    """
    Returns the conjugated form of `verb` for the person at `person_index`
    (0 = yo, 1 = tú, 2 = él/ella, 3 = nosotros, 4 = vosotros, 5 = ellos/ellas)
    Returns None if the verb is not recognized as a regular -ar/-er/-ir verb.
    """
    verb = verb.strip().lower()

    # Try regular endings based on verb ending
    ending = verb[-2:]
    if ending in REGULAR_ENDINGS:
        stem = verb[:-2]
        return stem + REGULAR_ENDINGS[ending][person_index]

    return None  # invalid verb


# -------------------------------------------------------------
# FUNCTION: Single conjugation prompt
# -------------------------------------------------------------
def mode_single_conjugation():
    verb = input("Enter the regular infinitive verb (e.g. hablar): ").strip()
    
    print("\nPersons:")
    for i, person in enumerate(PERSONS, start=1):
        print(f"  {i}. {person}")
        
    try:
        choice = int(input("\nPerson number (1-6): "))
    except ValueError:
        print("That is not a valid number.\n")
        return

    if choice < 1 or choice > 6:
        print("Please choose a number between 1 and 6.\n")
        return

    result = get_conjugation(verb, choice - 1)

    if result is None:
        print(f'"{verb}" is not a recognized regular -ar/-er/-ir verb.\n')
    else:
        print(f'\nResult: {verb} ({PERSONS[choice - 1]}) -> {result}\n')


# -------------------------------------------------------------
# FUNCTION: Full conjugation table
# -------------------------------------------------------------
def mode_full_table():
    verb = input("Enter the regular infinitive verb (e.g. comer): ").strip()

    if get_conjugation(verb, 0) is None:
        print(f'"{verb}" is not a recognized regular -ar/-er/-ir verb.\n')
        return

    print(f"\nFull present-tense conjugation of '{verb}':")
    for index, person in enumerate(PERSONS):
        result = get_conjugation(verb, index)
        print(f"  {person:12s} -> {result}")
    print()


# -------------------------------------------------------------
# FUNCTION: Quiz / practice mode
# -------------------------------------------------------------
def mode_quiz():
    try:
        num_questions = int(input("How many questions do you want? "))
    except ValueError:
        print("That is not a valid number.\n")
        return

    if num_questions <= 0:
        print("Please enter a positive number.\n")
        return

    score = 0

    for q in range(1, num_questions + 1):
        verb = random.choice(ALL_KNOWN_VERBS)
        person_index = random.randint(0, 5)
        correct_answer = get_conjugation(verb, person_index)

        print(f"\nQuestion {q}: Conjugate '{verb}' for '{PERSONS[person_index]}'")
        user_answer = input("Your answer: ").strip().lower()

        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The right answer is: {correct_answer}")

    print(f"\nYou scored {score} out of {num_questions}.\n")