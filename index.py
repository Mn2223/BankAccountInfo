class BankAccount:
    """
    Represents a bank account with balance and deposit/withdraw functionality.
    """

    def __init__(self, initial_balance=0):
        """
        Initializes the bank account with an optional initial balance.

        Args:
            initial_balance (float): The starting balance of the account.
        """
        self._balance = initial_balance

    def deposit(self, amount):
        """
        Deposits money into the account.

        Args:
            amount (float): The amount to deposit.
        """
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount:.2f}. New balance: {self._balance:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        """
        Withdraws money from the account.

        Args:
            amount (float): The amount to withdraw.
        """
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount:.2f}. New balance: {self._balance:.2f}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        """
        Returns the current balance of the account.

        Returns:
            float: The account balance.
        """
        return self._balance


# Example usage:
A = int(input("Enter the initial balance in account:"))
x = int(input("enter deposit amount:" ))
y = int(input("enter withdraw amount:"))
account = BankAccount(A)
account.deposit(x)
account.withdraw(y)
print(f"Final balance: {account.get_balance():.2f}")
