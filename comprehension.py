import random  # import random module
# Program ask for name, and to guess a random number between 1 and 20 in 6 guesses.
guessesTaken = 0  # Assign 0 to variable guessesTaken

print('Hello! What is your name?')  # Print string to console
myName = input()  # Assign input to variable myName

number = random.randint(1, 20)  # Assign random number between 1 and 20 to variable number
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')  # Print string to console

while guessesTaken < 6:  # Loop, while variable guessesTaken is smaller than 6
    print('Take a guess.')  # Print string to console
    guess = input()  # Assign input to variable guess
    guess = int(guess)  # Change input from string to integer

    guessesTaken += 1  # Add 1 to variable guessesTaken

    if guess < number:  # Check if guess smaller than number
        print('Your guess is too low.')  # Print string to console if line above True

    if guess > number:  # Check if guess bigger than number
        print('Your guess is too high.')  # Print string to console if line above True

    if guess == number:  # Check if guess equals number
        break  # Break while loop if line above True

if guess == number:  # Check if guess equals number
    guessesTaken = str(guessesTaken)  # If line above True: change guessesTaken type from integer to string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')  # Print string to console

if guess != number:  # Check if guess not equals number
    number = str(number)  # If line above True: change number type from integer to string
    print('Nope. The number I was thinking of was ' + number)  # Print string to console
