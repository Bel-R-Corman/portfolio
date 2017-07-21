from random import randint
dice = [1, 2, 3, 4, 5, 6]
roll = dice[randint(0,5)]
guess = input("Pick the number you think the dice will roll! (Obviously between 1-6)")

g = int(guess)
print (guess)
print (roll)
if g == roll:
    print("You read my mind!")
else:
    print("You are definatly not a telepath, better luck next time!")
    print("Your guess")
    print(g)
    print("Dice roll:")
    print(roll)
