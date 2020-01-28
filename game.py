"""A number-guessing game."""

import random

print("Howdy, what's your name?")
user_name = input("(type in your name) ")
print(f"{user_name} I'm thinking of a number between 1 and 100.")
print("Try to guess my number.")

rand_num = random.randrange(101)


guess = int(input("Your guess? "))
guess_count = 1

while guess != rand_num:
    if guess < rand_num:
        print("Your guess is too low, try again.")
    elif guess > rand_num:
        print("Your guess is too high, try again.")

    guess = int(input("Your guess? "))
    guess_count += 1

print(f"Well done, {user_name}! You found my number in {guess_count} tries!")