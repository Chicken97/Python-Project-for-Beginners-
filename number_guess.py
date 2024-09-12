import random

def number_guess():
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            user_input = int(input("Enter a number between 1 to 100: "))
            attempts += 1
            if user_input == secret_number:
                print(f"Congratulations! You have guessed the correct number. Attempts: {attempts} time{'s' if attempts > 1 else ''}")
                return
            elif user_input < secret_number:
                print("too low")
            else:
                print("too high")

        except ValueError:
            print("Please enter a valid number")

number_guess()
