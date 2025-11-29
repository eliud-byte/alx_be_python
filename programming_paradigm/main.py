import sys
from bank_account import BankAccount

def main():
    account = BankAccount(250) # Example starting balance
    
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    try:
        command_parts = sys.argv[1].split(':')
        command = command_parts[0]
        # Handles cases where no amount is provided (e.g., just "display")
        amount = float(command_parts[1] if len(command_parts) > 1 else 0)
    except ValueError:
        print("Error: Amount nust be a number.")
        sys.exit(1)

    if command == "deposit":
        account.deposit(amount)
        print(f"Deposited: ${amount:,.2f}")
        account.display_balance()

    elif command == "withdraw":
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:,.2f}")
            account.display_balance()
        else:
            print("Insufficient funds.")
    
    elif command == "display":
        account.display_balance()
    
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
