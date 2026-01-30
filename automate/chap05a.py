'''
Buggy Grade-Average Calculator
Copy the following program into your editor or download it from https://autbor
.com/buggygradeaverage.py. This program lets the user enter any number of grades
until the user enters done. It then displays the average of the entered grades.
'''
def calculate_grade_average(grade_sum, number_of_grades):
    grade_average = int(grade_sum / number_of_grades)
    return grade_average

counter = 0
total = 0
while True:
    print('Enter a grade, or "done" if done entering grades:')
    grade = input()
    if grade == 'done':
        break
    counter = counter + 1
    total = total + int(grade)
avg = calculate_grade_average(counter, total)
print('The grade average is:', avg)
'''
When you run the program and enter 100 and 50, however, it reports the
average as 0 instead of 75:
Enter a grade, or "done" if done entering grades:
100
Enter a grade, or "done" if done entering grades:
50
Enter a grade, or "done" if done entering grades:
done
The grade average is: 0
Run this program under a debugger to find out why it doesn't work,
then fix the bug. (Note that if the user enters a response other than done or
a number, the program crashes; ignore this bug for now.)
'''
