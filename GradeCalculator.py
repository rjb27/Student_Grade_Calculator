def get_valid_marks(subject_number):
    while True:
        value = input(f"Enter marks for subject {subject_number}: ")
        try:
            marks = int(value)
        except ValueError:
            print("Invalid marks. Enter a number between 0 and 100.")
            continue
        if 0 <= marks <= 100:
            return marks
        print("Invalid marks. Enter a number between 0 and 100.")

print("You entered:", get_valid_marks(2))