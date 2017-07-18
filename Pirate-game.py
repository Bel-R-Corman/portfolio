import time

import msvcrt as m

name = input("Oy mate! What do you call yourself?")
print("Welcome aboard, Captian " + name)

def wait():
    m.getch()

    wait()

def pstoryline():
    print("Although the seas are infested with pirates and scoundrels, only one name striks the chord of fear in people so profoundly as Captain " + name)
    wait()
    print("You and your crew are roming the seven seas hunting for treasure")
    wait()
    print("Along your travles you have encountered storms and mythical beasts, death and catastrophe")
    wait()
    print("But you endevor through it all in hopes of finding the alleged 'Treasure of Amora'")

    #wait for five seconds
    wait()

    print("As you look out into the gray horizon, you see shadowy figures that can easily be recognized as fellow shipmongers")
    wait()
    print("you've been traveling at sea for many moons and both you and your crew is starving for food as well as excitement")
    wait()
    print("Your pirate sailors agree its time to have some fun!")

#wait for five seconds
    wait()

    print("Multiple ships prowl the water around you.")
    wait()
    print("out of all of them, two ships catch your eye")
    wait()
    print("A magnifacent ship with an ink black starboard, the mast so tall it disappears into the fog.")
    wait()
    print("The second ship is a small dingy, and you see only a few sailors aboard")
    wait()
    print("You are confident you will capture the dingy swiftly but you're not sure you it has much treasure aboard")
    wait()
    print("The other ship however, seems to have much treasure aboard but you dont know if you have enough manpower to overcome them")

    #wait for five seconds
    time.sleep(5)

pstoryline()

def Choseship():
    choice = input("Which boat do you choose, esteemed Capt'n? The dingy or the ship?")
    if choice == "dingy":
        print("ATTACK, Captian!")
    else:
        print("May the wind be on your side of the sail.")
    #elif:
        #print("Keep your eyes on the rigging!")
