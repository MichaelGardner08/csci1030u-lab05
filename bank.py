
def main():
    balance = 0.0
    while True:
        print("1) Deposit")
        print("2) Withdraw")
        print("3) Balance")
        print("4) Quit")
        choice = input("Choice: ").strip()

        if choice == "1":
            amount = float(input("Amount: "))
            balance = balance + amount
            print(f"New balance: {balance:.2f}")

        elif choice == "2":
            amount = float(input("Amount: "))
            if amount > balance:
                print("Insufficient funds")
            else:
                balance = balance - amount
                print(f"New balance: {balance:.2f}")

        elif choice == "3":
            print(f"Current balance: {balance:.2f}")

        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
