'''
Tree Printer
Use a for loop to print a triangular pine tree of a size the user asks for. The
tree branches should be printed as a number of rows of ^ characters, while
the trunk should always be two # characters. For example, if the user enters
5 for the size, the program should print this:
Enter the tree size: 5
    ^
   ^^^
  ^^^^^
 ^^^^^^^
^^^^^^^^^
    #
    #
If the user enters 3 for the size, the program should print the following:
Enter the tree size: 3
  ^
 ^^^
^^^^^
  #
  #
Let’s examine the pattern of text produced if the size is, say, 5. There
are five rows of tree branches, the same as the size. Each row consists of
two parts: a number of spaces of indentation followed by a number of ^
tree branch characters. I’ve replaced the spaces with periods to make them
easier to count:
size == 5
....^ 4 spaces, 1 branch
...^^^ 3 spaces, 3 branches
..^^^^^ 2 spaces, 5 branches
.^^^^^^^ 1 spaces, 7 branches
^^^^^^^^^ 0 spaces, 9 branches
Notice the pattern: The first row has four spaces (one less than the size)
and one branch character. In the later rows, the number of spaces decreases
by one and the number of branches increases by two. If we use the statement for row_num in range(1, size + 1): for our loop, the number of ' '
space characters in each row is (size - row_num) and the number of ^ branch
characters in each row is (row_num * 2 - 1). You can then use string replication to create the string to print: If row_num is 3, then ^ * (row_num * 2 – 1)
evaluates to ^^^^^.
The trunk is always two rows long and uses a single # trunk character
per row regardless of the tree’s size. However, the size does determine how
many spaces you must place in front of the trunk character to put the trunk
in the middle of the tree:
size == 5
....# 4 spaces, 1 trunk
....# 4 spaces, 1 trunk
Use this information to write a program that asks the user to enter a
size and then prints the corresponding tree. Remember that the input()
function returns a string, so you’ll need to convert it to an integer to perform math on it. The code could look something like size = int(input()).
As a second exercise, write this same program using while loops instead
of for loops.
'''
