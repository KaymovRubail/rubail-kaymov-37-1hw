import random
from decouple import config

def play_casino_game():
    my_money = int(config('MY_MONEY', default=1000))
    slot_numbers = list(range(1, 11))

    while True:
        print(f"Your current balance is ${my_money}.")
        bet_amount = int(input("Enter your bet amount: "))

        if bet_amount > my_money:
            print("You don't have enough money. Please enter a valid bet amount.")
            continue

        selected_slot = int(input("Choose a slot number (1-10): "))
        winning_slot = random.choice(slot_numbers)

        if selected_slot == winning_slot:
            my_money += 2 * bet_amount
            print(f"Congratulations! You won ${2 * bet_amount}. Your new balance is ${my_money}.")
        else:
            my_money -= bet_amount
            print(f"Sorry, you lost ${bet_amount}. Your new balance is ${my_money}.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print(f"Game over. Your final balance is ${my_money}.")
            break
