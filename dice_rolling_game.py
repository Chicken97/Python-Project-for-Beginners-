from random import randint

def dice_rolling_game(choice):
    if choice == 'y':
        print(f"Player One : {randint(1, 6)} and Player Two : {randint(1, 6)}")
    elif choice == 'n':
        print("Thank you for playing!")
        exit()
    else:
        print("Invalid choice! Please enter 'y' or 'n'")

while True:
    user_input = input("Roll the dice? (y/n:) ").lower()
    dice_rolling_game(user_input)






