from random import randint

money = int(input("How much money do you want to start with?"))
bet = int(input("How much money would you like to bet?"))

def guessC():
    color = ["red", "black"]
    guessc = input("Guess which color the ball will land on, red or black?")
    rollc = color[randint(0,1)]
    if guessc == rollc:
        print("You guessed right! You didn't lose your money yet!")
        money= money + bet
    else:
        print("Wrong! Keep the money coming")
        print("Your guess")
        print(guessc)
        print("Correct color")
        print(rollc)
        money= money-bet

def guessP():
    dice = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    guessp = input("Guess the parity of the number the ball will land on, odd or even?")
    rollp = dice[randint(0,8)]
    parity = ''
    if rollp% 2==0:
        parity == "even"
        if guessp == parity:
            print("You guessed right! You didn't lose your money yet!")
            money= money + bet
    else:
        print("Wrong!! Keep the money coming!")
        print("Your guess")
        print(guessp)
        print("Ball roll")
        print(rollp)
        money= money - bet


def guessSN():
    guesssn = int(input("Guess a specific number (1-9)!"))
    dice = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    rollsn = dice[randint(0,8)]
    if guesssn == rollsn:
        print("You guessed right! You didn't lose your money yet!")
        money= money + bet
    else:
        print("Wrong!! Keep the money coming!")
        print("Your guess")
        print(guesssn)
        print("Ball roll")
        print(rollsn)
        money= money - bet


overall = input("Place your bet- color, parity, or a specific number")
if overall == ("color"):
    guessC()
elif overall == ("parity"):
    guessP()
elif overall == ("specific number"):
    guessSN()
