class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account Holder: {self.account_holder}, Balance: ${self.balance}"

# Input validation helpers
def get_valid_name():
    while True:
        name = input("Enter account holder name: ").strip()
        if name:
            return name
        else:
            print("Name cannot be empty. Please try again.")

def get_valid_amount(prompt, allow_zero=True):
    while True:
        try:
            value = float(input(prompt))
            if value < 0 or (value == 0 and not allow_zero):
                print("Amount must be positive.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")

# Main program
if __name__ == "__main__":
    name = get_valid_name()
    initial_balance = get_valid_amount("Enter initial deposit amount: ")

    account = BankAccount(name, initial_balance)
    print("\nAccount created successfully!")
    print(account)

    while True:
        print("\nChoose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Show Balance")
        print("4. Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            amount = get_valid_amount("Enter deposit amount: ", allow_zero=False)
            account.deposit(amount)
        elif choice == '2':
            amount = get_valid_amount("Enter withdrawal amount: ", allow_zero=False)
            account.withdraw(amount)
        elif choice == '3':
            print(f"Current balance: ${account.get_balance()}")
        elif choice == '4':
            print("Thank you for using the bank system!")
            break
        else:
            print("Enter valid option")
