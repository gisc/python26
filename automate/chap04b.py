'''
Arithmetic Functions Without Arithmetic Operators
Let’s create add(number1, number2) and multiply(number1, number2) functions
that add and multiply their arguments without using the + or * operators.
These functions will be quite inefficient, but don’t worry; the computer
doesn’t mind.
Imagine that we start with this plus_one() function, which is the only
function where we’ll allow the use of the + operator:
'''
def plus_one(number):
 return number + 1
'''
For example, calling plus_one(5) returns 6 and calling plus_one(6)
returns 7.
Your add() function should not use the + operator; rather, it should have
loops that repeatedly call the plus_one() function to perform the addition
operation on the operands passed as parameters. After all, the operation
4 + 3 is the same as 4 + 1 + 1 + 1. Your add() function is expected to handle
positive integers only.
If you need a hint, start with the following template:
'''
def add(number1, number2):
    total_sum = ____
    for i in range(number2):
        total_sum = plus_one(total_sum)
    return total_sum
'''
Your multiply() function should work in the same way: Avoid using the
* operator, and instead use a loop to repeatedly call your add() function.
After all, the operation 3 * 5 is the same as 3 + 3 + 3 + 3 + 3 or 5 + 5 + 5.
It’s a good idea to make sure your add() function works before beginning on multiply(). Also note that 2 + 8 is the same as 8 + 2 and 2 * 8 is the
same as 8 * 2.
'''