import random

number_to_guess =random.randint(1, 100)

while True:
    try:
        guess = int(input("Enter your guess (1-100): "))

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("Well done! You've guessed the number.")
            break
    except ValueError:
        print("Please enter a valid integer.")


#https://youtu.be/yVl_G-F7m8c?si=Ki3g9unlWieVFvPf





# Definition for a Node (N-ary Tree Node).