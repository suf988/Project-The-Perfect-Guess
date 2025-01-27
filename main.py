# We are going to write a program that generates a random number and asks the user to guess it.

# If the player’s guess is higher than the actual number, the program displays “Lower number please”. Similarly, if the user’s guess is too low, the program prints “higher number please” When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number.

from random import randint

rand = randint(0,100)
guesses = 0

user_guess = -1

print("\n***** Welcome to The Perfect Guess *****")

while(user_guess != rand):
    guesses += 1
    user_guess = int(input("\nGuess a number between 0-100: "))

    if user_guess < 0:
        print("\nX----X---- ERROR! Number can't be negative ----X----X")
    elif user_guess > 100:
        print("\nX----X---- ERROR! Number can't be greater than 100 ----X----X")
    elif user_guess > rand:
        print("\nGuess a lower number.")
    elif user_guess < rand:
        print("\nGuess a higher number.")

print(f"\nCongratulations! You guessed the correct number: {rand}")
print(f"Your guesses: {guesses}")

with open("highscore.txt") as f:
    old_score = int(f.read())

if guesses < old_score:
    with open("highscore.txt", 'w') as p:
        p.write(str(guesses))
    print("\nYou beat the Highscore!")
else:
    print("\nYou couldn't beat the highscore.")

print(f"\nHighscore: {min(old_score, guesses)}")