'''
Rectangle Printer
Write a program that prints a rectangle of capital O characters. For exam
ple, the following rectangle has a width of eight and a height of five:
OOOOOOOO
OOOOOOOO
OOOOOOOO
OOOOOOOO
OOOOOOOO
The program should always print a rectangle of O characters that has a 
height of five (that is, five rows), but the width should be based on an inte
ger the user enters. For example, the output of this program could look 
like this:
Enter the width for the rectangle:
15
OOOOOOOOOOOOOOO
OOOOOOOOOOOOOOO
OOOOOOOOOOOOOOO
OOOOOOOOOOOOOOO
OOOOOOOOOOOOOOO
'''

'''
Here are some hints to help you write this program:
•	Call the print() function with a message to tell the user to enter the 
width, then call input() to accept the width.
•	Store the width returned from input() in a variable.
•	The input() function returns strings, but we want an integer form of 
the user input, so pass the variable to the int() function and store 
what int() returns in a variable.
•	Use string replication to create a string of O letters of the desired 
width. (If a variable named width has 8 in it, then O * width will 
evaluate to OOOOOOOO.)
•	Call print() five times to produce five rows of the string replication 
letters.
'''