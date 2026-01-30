'''
Christmas Tree Printer
Instead of creating a plain tree like the one in the previous project, write
a program that prints a Christmas tree with o ball ornaments randomly
replacing ^ branch characters. For example, a Christmas tree of size 6
could look like this:
Enter the tree size: 6
     ^
    ^^o
   o^^^o
  ^o^^^o^
 ^^^^^^^^^
o^^^^^^o^oo
     #
     #
The code should be quite similar to that of the previous project. You’ll
need an additional nested loop to build the string for each row of branches,
however. You can call the random.randint() function to determine whether to
add a ^ or o character to the row string. For example, the condition random
.randint(1, 4) == 1 will be True one-quarter of the time and can lead your
code to create a tree with roughly one-quarter of the branches as ′o′ ornament characters and three-quarters as ^ branch characters.
As a second exercise, write this same program using while loops instead
of for loops.
'''