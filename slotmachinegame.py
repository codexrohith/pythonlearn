import random

def spin_row():
    elements = ["🍉", "🍇", "🍒", "🍊"]
    result = [random.choice(elements) for _ in range(3)]
    print("| " + " | ".join(result) + " |")
    return result

def payout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=="🍉":
            win=bet*2
            return win
        elif row[0]=="🍇":
            win=bet*3
            return win
        elif row[0]=="🍒":
            win=bet*5
            return win
        else:
            win=bet*10
            return win
    else:
        return 0

def main():
    balance = 100
    print("*" * 50)
    print("WELCOME TO PYTHON SLOT MACHINE")
    print("*" * 50)

    while True:
        print(f"\nYour current balance is ₹{balance}")
        try:
            bet = int(input("Enter the amount you want to bet: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if bet > balance:
            print("Not enough balance to place that bet.")
            continue
        if bet <= 0:
            print("Enter a valid bet amount greater than 0.")
            continue

        balance -= bet
        result = spin_row()

        money = payout(result,bet)
        if money>0:
            print(f"JACKPOT! You won {money/bet} your bet!")
            balance += money
        else:
            print("Better luck next time!")

        print(f"New balance: ₹{balance}")

        if balance == 0:
            print(" You ran out of money. Game over.")
            break

        choice = input("Do you want to play again? (y/n): ")
        if choice.lower() == "n":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
