# BankAccountInfo
This Python code defines a BankAccount class that simulates a simple bank account with balance management functionality, including deposits and withdrawals. Below is an explanation of the main components:

Class Definition: The BankAccount class encapsulates the properties and behaviors of a bank account.

Constructor (__init__ method): Initializes the bank account with an optional initial balance.

initial_balance (float): Optional argument to set the starting balance. Defaults to 0.
Methods:

deposit(amount): Adds the specified amount to the account balance if the amount is positive.
withdraw(amount): Deducts the specified amount from the account balance if the amount is positive and sufficient funds are available.
get_balance(): Returns the current balance of the account.
Example Usage:

Prompts the user for initial balance, deposit amount, and withdrawal amount.
Creates an instance of BankAccount with the specified initial balance.
Performs deposit and withdrawal operations.
Prints the final account balance.
