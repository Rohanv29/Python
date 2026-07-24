# # Write your code here
# import random

# def game():
#     a = random.randint(1,100)

#     while True:
#         guess=int(input("enter a number"))

#         if guess == a:
#                 print("Congrations! You guessed correct")
#         elif guess > a:
#                 print("Too high, try lower number")
#         elif guess < a:
#                 print("Too low, try a higher number")
#         else:
#                 print("Not a valid input")

# game()
import random

secret_number = random.randint(1, 100)

guess = None
attempts = 0

print("I'm thinking of a number between 1 and 100.")

while guess != secret_number:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try higher.")
    elif guess > secret_number:
        print("Too high! Try lower.")


print(f"Congratulations! You guessed it in {attempts} attempts.")