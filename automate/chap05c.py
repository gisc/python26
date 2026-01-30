'''
Leap Year Calculator
Copy the following program into your editor or download it from https://autbor.com/buggyLeapYear.py. This program has an is_leap_year() function that
takes an integer year, then returns True if it's a leap year and False if it isn't.
'''
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False
while True:
    print('Enter a year or "done":')
    response = input()
    if response == 'done':
        break
    print('Is leap year:', is_leap_year(int(response)))
'''
For example, if you run this program, the output will look like this:
Enter a year or "done":
2000
Is leap year: True
Enter a year or "done":
2001
Is leap year: False
Enter a year or "done":
2004
Is leap year: True
Enter a year or ″done″:
2100
Is leap year: True
Enter a year or ″done″:
done
A year is a leap year if it is evenly divisible by 4. An exception to this rule
occurs if the year is also evenly divisible by 100, in which case it is not a leap
year. There is an exception to that exception too: If the year is also evenly
divisible by 400, it is a leap year.
The year 2100 should not be a leap year, but the function call is_leap
_year(2100) incorrectly returns True. Run this code under a debugger so that
you can see where exactly the bug is, and then write the corrected is_leap
_year() function.
'''
