# Global balance
balance = 0

def deposit(amount):
    global balance
    balance += amount
    print(f"Deposited: ₦{amount}")

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print(f"Withdrew: ₦{amount}")
    else:
        print("Insufficient funds.")

def check_balance():
    print(f"Current balance: ₦{balance}")

# Example usage
deposit(5000)
withdraw(2000)
check_balance()
