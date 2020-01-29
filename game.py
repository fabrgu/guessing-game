"""A number-guessing game."""

import random


def get_valid_user_input(message):
    guess = None
    try:
        guess = int(input(message))
    except ValueError:
        print("Not a number, silly!")
    return guess


print("Howdy, what's your name?")
user_name = input("(type in your name) ")
print(f"{user_name} I'm thinking of a number between 1 and 100.")
print("Try to guess my number.")

rand_num = random.randrange(101)

guess = get_valid_user_input("Your guess? ")
guess_count = 1

while guess is None:
    guess = get_valid_user_input("Please enter a real number: ")
    guess_count += 1

while guess < 1 or guess > 100:
    print("That's not between 1 and 100 silly!")
    guess = get_valid_user_input(
        f"Please enter a valid number between 1 and 100: ")
    guess_count += 1


while True:
    if guess is None:
        guess = get_valid_user_input("Please enter a real number: ")

    if guess < 1 or guess > 100:
        print("That's not between 1 and 100 silly!")
        guess = get_valid_user_input(
            f"Please enter a valid number between 1"
            f"and 100: ")
    if guess == rand_num:
        print(
            f"Well done, {user_name}!"
            f" You found my number in {guess_count} tries!"
        )
        break

    if guess < rand_num:
        print("Your guess is too low, try again.")
    elif guess > rand_num:
        print("Your guess is too high, try again.")

    guess = get_valid_user_input("Your guess? ")
    guess_count += 1
    while guess is None:
        guess = get_valid_user_input("Please enter a real number: ")
        guess_count += 1

    while guess < 1 or guess > 100:
        print("That's not between 1 and 100 silly!")
        guess = get_valid_user_input(
            f"Please enter a valid number "
            f"between 1 and 100: ")
        guess_count += 1
