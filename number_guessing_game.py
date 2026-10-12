# Name: Juan Lizarraga
# Period: AM

# This generates a random number
import random

random_number = random.randint(1, 10)
# randint stands for random integer

past_guesses = []
user_guess = 0

while user_guess != random_number:
        user_guess = int(input("Guess a number between 1 and 10: "))
       
        if user_guess < 1 or user_guess > 10:
            print("This guess will not work! Please try again!")
            print(past_guesses)
        
        elif user_guess in past_guesses:
            print("You already guessed that number!")
            print(past_guesses)
        
        elif user_guess < random_number:
            print("Try again! Your guess is higher!")
            print(past_guesses)
            past_guesses.append(user_guess)
        elif user_guess > random_number:
            print("Try again! Your guess is lower!")
            print(past_guesses)
            past_guesses.append(user_guess)

        elif user_guess == random_number:
            print("Congratulations! You guessed the number!")
            print(past_guesses)

        else:
            past_guesses.append(user_guess)
