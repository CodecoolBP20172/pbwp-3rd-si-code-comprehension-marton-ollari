import random  # import random module
# Program ask for name, and to guess a random number between 1 and 20 in 6 guesses.
guessesTaken = 0  # assign 0 to variable guessesTaken

print('Hello! What is your name?')  # print string
myName = input()  # assign input to variable myName

number = random.randint(1, 20)  # assign random number between 1 and 20 to variable number
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')  # print string

while guessesTaken < 6:  # loop, while variable guessesTaken is smaller than 6
    print('Take a guess.')  # print string
    guess = input()  # assign input to variable guess
    guess = int(guess)  # change input from string to integer

    guessesTaken += 1  # add 1 to variable guessesTaken

    if guess < number:  # check if guess smaller than number
        print('Your guess is too low.')  # print string if line above True

    if guess > number:  # check if guess bigger than number
        print('Your guess is too high.')  # print string if line above True

    if guess == number:  # check if guess equals number
        break  # break while loop if line above True

if guess == number:  # check if guess equals number
    guessesTaken = str(guessesTaken)  # if line above True: change input from integer to string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')  # print string

if guess != number:  # check if guess not equals number 
    number = str(number)  # if line above True: change input from integer to string
    print('Nope. The number I was thinking of was ' + number)  # print string
