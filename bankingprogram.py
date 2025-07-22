accounts = {}

def create_account():
    name = input("Enter your name: ").strip().lower()
    if name in accounts:
        print("Account already exists.")
    else:
        try:
            deposit = float(input("Enter amount to deposit: "))
            accounts[name] = deposit
            print("Account created successfully.")
        except ValueError:
            print("Invalid amount.")

def access_account():
    name = input("Enter your name: ").strip().lower()
    if name not in accounts:
        print("Account not found.")
        return

    print(f"Welcome back, {name}!")
    print("1. Check Balance\n2. Deposit\n3. Withdraw")
    try:
        op = int(input("Choose an option: "))
    except ValueError:
        print("Invalid input.")
        return

    if op == 1:
        print(f"Your balance is ₹{accounts[name]:.2f}")

    elif op == 2:
        try:
            amount = float(input("Enter amount to deposit: "))
            accounts[name] += amount
            print("Amount deposited successfully.")
        except ValueError:
            print("Invalid amount.")

    elif op == 3:
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= accounts[name]:
                accounts[name] -= amount
                print("Amount withdrawn successfully.")
            else:
                print("Insufficient balance.")
        except ValueError:
            print("Invalid amount.")

    else:
        print("Invalid operation.")

def show_all_accounts():
    print("\n Account Summary:")
    for name, balance in accounts.items():
        print(f"{name}: ₹{balance:.2f}")


while True:
    print("=" * 60)
    print("WELCOME TO PYTHON BANK")
    print("=" * 60)
    try:
        choice = int(input("1. Create Account\n2. Access Account\n3. Show All\n4. Exit\n>> "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    match choice:
        case 1:
            create_account()
        case 2:
            access_account()
        case 3:
            show_all_accounts()
        case 4:
            print("Thanks for using Python Bank ")
            break
        case _:
            print("Invalid choice. Please select a valid option.")
