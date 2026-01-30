'''
Transaction Tracker
Write a function named after_transaction() that returns the amount of
money in an account after a transaction. The two parameters for this function are balance and transaction. They will both have integer arguments. The
balance is how much money is currently in the account, and the transaction is
how much to add or remove from the account (based on whether transaction
is a positive or negative integer).
This operation is more complicated than just return balance + transaction.
If the transaction is negative and would overdraw the account (that is, if
balance + transaction is less than zero), then the transaction should be
ignored and the original balance returned. For example, calling the function from the interactive shell should look like this:
>>> after_transaction(500, 20)
520
>>> after_transaction(300, -200)
100
>>> after_transaction(3, -1000)
3
>>> after_transaction(3, -4)
3
>>> after_transaction(3, -3)
0
'''
