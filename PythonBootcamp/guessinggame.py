from random import randint

num = randint(1,101)

guesses = []

print("Make a guess between 1 and 100!")


while True:

    guess = int(input('guess: '))

    if guess < 1 or guess > 100:
        print("OUT OF BOUNDS")
        continue

    guesses.append(guess)

    if guesses[-1] == num:
        print('You have guessed it')
        break

    if(len(guesses) <= 1):
        if abs(guesses[-1] - num) < 10:
            print("WARM")
        else:
            print("COLD")
    else:
        if abs(guesses[-1] - num) < abs(guesses[-2] - num):
            print("WARMER")
        else:
            print("COLDER")


