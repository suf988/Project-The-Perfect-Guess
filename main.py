# We are going to write a program that generates a random number and asks the user to guess it.

# If the player’s guess is higher than the actual number, the program displays “Lower number please”. Similarly, if the user’s guess is too low, the program prints “higher number please” When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number.

from random import randint

rand = randint(0,10)
guesses = 0

user_guess = -1

while(user_guess != rand):
    guesses += 1
    user_guess = int(input("Guess a number between 0-10: "))

    if user_guess > rand:
        print("Guess a lower number.")
    elif user_guess < rand:
        print("Guess a higher number.")

print(f"Congratulations! You guessed the correct number {rand}")
print(f"Your guesses: {guesses}")