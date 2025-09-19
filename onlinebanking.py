class BankAccount:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✅ {amount} deposited successfully.")
        else:
            print("❌ Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"✅ {amount} withdrawn successfully.")
        else:
            print("❌ Insufficient balance or invalid amount.")

    def get_balance(self):
        print(f"💰 Current Balance: {self.balance}")


# --- Menu-driven program ---
def main():
    account = BankAccount("1001", "Alice", 5000)

    while True:
        print("\n--- Banking Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)

        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)

        elif choice == "3":
            account.get_balance()

        elif choice == "4":
            print("✅ Thank you for using our banking system.")
            break

        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
