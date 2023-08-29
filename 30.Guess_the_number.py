import random

def guess_the_number(n):
    random_number = random.randint(1, n)
    attempts = 0
    
    print(f"Welcome to Guess the Number game!")
    print(f"I'm thinking of a number between 1 and {n}. Can you guess it?")
    
    while True:
        user_guess = int(input("Enter your guess: "))
        attempts += 1
        
        if user_guess < random_number:
            print("Too low! Try again.")
        elif user_guess > random_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {random_number} in {attempts} attempts.")
            break

range_of_numbers = 100
guess_the_number(range_of_numbers)
