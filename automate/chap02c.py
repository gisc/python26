'''
Fizz Buzz
Fizz Buzz is a common programming challenge that goes like this. Write a
program that accepts an integer from the user. If the integer is divisible by
3, the program should print Fizz. If the integer is divisible by 5, the program
should print Buzz. If the integer is divisible by 3 and 5, the program should
print Fizz Buzz. Otherwise, the program should print the number the user
entered. The output of this program should look something like this:
Enter an integer:
18
Fizz
Or this:
Enter an integer:
25
Buzz
Or this:
Enter an integer:
15
Fizz Buzz
Or this:
Enter an integer:
37
37
Here are some hints to help you write this program:
•	 Use the modulo operator to determine whether a number is divisible. If
the condition number % 3 == 0 is True, then number is divisible by 3.
•	 Be sure to check whether the number is divisible by both 3 and 5 before
checking whether the number is divisible by either 3 or 5. Otherwise,
the number 15 won’t cause the program to print Fizz Buzz.
'''