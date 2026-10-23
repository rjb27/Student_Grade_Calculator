# Student Grade Calculator

This is a Python program that takes a student's name and marks in 5 subjects,
then shows the total, percentage, grade and whether the student passed or failed.
After each student it asks if you want to enter another one.

Marks are out of 100. Grades: 85 and above is A, 70 and above is B,
55 and above is C, 40 and above is D, below 40 is F. 40% or more is a pass.

# How to run

Make sure Python 3 is installed, then run this in the folder:
python GradeCalculator.py

# How it works

1. get_valid_marks() keeps asking until the user types a whole number from 0 to 100
2. calculate_total() adds the 5 marks
3. calculate_percentage() divides the total by 5, since the full marks are 500
4. get_grade() and get_result() use if-elif-else to decide the grade and pass/fail
5. main() runs everything in a loop for each student

# Sample output

Enter student name: Aman
Enter marks for subject 1: 80
Enter marks for subject 2: 70
Enter marks for subject 3: 90
Enter marks for subject 4: 60
Enter marks for subject 5: 50
Aman | Total: 350 | Percentage: 70.00% | Grade: B | Result: Pass
Another student? (y/n): n

I also tested the boundary case (all 40s gives grade D, Pass), invalid input
(105 and abc are rejected), and two students in one run (Riya and Karan).
