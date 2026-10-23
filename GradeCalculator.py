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


def calculate_total(marks_list):
    return sum(marks_list)


def calculate_percentage(total):
    return total / 5


def get_grade(percentage):
    if percentage >= 85:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 55:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"


def get_result(percentage):
    if percentage >= 40:
        return "Pass"
    else:
        return "Fail"

def main():
    while True:
        name = input("Enter student name: ")

        marks_list = []
        for i in range(1, 6):
            marks_list.append(get_valid_marks(i))

        total = calculate_total(marks_list)
        percentage = calculate_percentage(total)
        grade = get_grade(percentage)
        result = get_result(percentage)

        print(f"{name} | Total: {total} | Percentage: {percentage:.2f}% | Grade: {grade} | Result: {result}")

        again = input("Another student? (y/n): ")
        if again.lower() != "y":
            break


main()
