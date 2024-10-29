import random
guess = 11
guesses = 4
print ("You have 4 guesses")
num = random.randint(0,10)
while guesses > 0 and int(guess) != num:
    guess = input("Guess: ")
    if guesses == 1:
        print("You ran out of guesses")
    elif int(guess) != num:
        guesses = guesses - 1
        print("guess again")
    else:
        print("You got it")
