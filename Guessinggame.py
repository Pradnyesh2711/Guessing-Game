import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I have selected a random number between 1 and 100. Can you guess it?")

   
    secret_number = random.randint(1, 100)
    
    attempts = 0
    guessed_number = None

    while guessed_number != secret_number:
        try:
            # Get user input for their guess
            guessed_number = int(input("Enter your guess: "))
            attempts += 1

            # Check if the guess is too high, too low, or correct
            if guessed_number < secret_number:
                print("Too low! Try again.")
            elif guessed_number > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    guessing_game()

