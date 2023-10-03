class User:
    def __init__(self, user_id, pin, balance):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposit: +${amount}")
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: -${amount}")
            return True
        return False

    def transfer(self, recipient, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transfer to {recipient.user_id}: -${amount}")
            recipient.transaction_history.append(f"Transfer from {self.user_id}: +${amount}")
            return True
        return False

    def view_transaction_history(self):
        return self.transaction_history


class ATM:
    def __init__(self):
        self.users = {}
        # Add some initial users (you can load them from a file or database)
        self.users['user1'] = User('user1', '1234', 1000)
        self.users['user2'] = User('user2', '5678', 1500)
        self.current_user = None

    def authenticate_user(self):
        user_id = input("Enter your User ID: ")
        pin = input("Enter your PIN: ")

        if user_id in self.users and self.users[user_id].pin == pin:
            self.current_user = self.users[user_id]
            print("Authentication successful. Welcome!")
            return True
        else:
            print("Authentication failed. Please try again.")
            return False

    def display_menu(self):
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. View Transaction History")
        print("6. Quit")

    def run(self):
        while True:
            if not self.current_user:
                if not self.authenticate_user():
                    continue

            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                print(f"Balance: ${self.current_user.check_balance()}")
            elif choice == '2':
                amount = float(input("Enter the deposit amount: $"))
                if self.current_user.deposit(amount):
                    print("Deposit successful.")
                else:
                    print("Invalid deposit amount.")
            elif choice == '3':
                amount = float(input("Enter the withdrawal amount: $"))
                if self.current_user.withdraw(amount):
                    print("Withdrawal successful.")
                else:
                    print("Insufficient funds or invalid amount.")
            elif choice == '4':
                recipient_id = input("Enter recipient's User ID: ")
                amount = float(input("Enter the transfer amount: $"))
                if recipient_id in self.users:
                    recipient = self.users[recipient_id]
                    if self.current_user.transfer(recipient, amount):
                        print("Transfer successful.")
                    else:
                        print("Insufficient funds or invalid amount.")
                else:
                    print("Recipient not found.")
            elif choice == '5':
                history = self.current_user.view_transaction_history()
                print("\nTransaction History:")
                for transaction in history:
                    print(transaction)
            elif choice == '6':
                print("Thank you for using our ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    atm = ATM()
    atm.run()
