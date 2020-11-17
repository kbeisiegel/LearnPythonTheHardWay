print("""You enter a dark room with three doors. Do you go through door #1, door #2, 
or door #3?""")
door = input("> ")

if door == "1":
    print("There's a giant bear here eating pie.")
    print("What do you do?")
    print("1. Take his pie.")
    print("2. Try to run away without the bear chasing you.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Congrats.")
    elif bear == "2":
        print("The bear chases you down and eats your legs off for disturbing him. Congrats.")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")



elif door == "2":
    print("You stare into an endless abyss, as it pulls you in with it's force.")
    print("1. Walk into the abyss.")
    print("2. Blueberries.")
    print("3. Do nothing.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body gets disintegrated by the abyss. Congrats.")
    else:
        print("The insanity rots your brain into a pool of muck. Congrats.")

elif door == "3":
    print("You find yourself inside a log cabin.")
    print("What do you do?")
    print("1. Go outside.")
    print("2. Stay inside the cabin, look for food.")

    maple = input("> ")

    if maple == "1":
        print("The door locks behind you and you are now stranded in a forest outside the locked cabin. Congrats.")
    else:
        print("You find tons of food in the cabin, you stuff your face. Congrats.")

else:
    print("You stumble around and fall on a knife and die. Congrats.")
