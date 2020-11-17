from sys import exit

def trap_room():
    print("You enter the tunnel, where you now find yourself in a room that leads to a trapdoor.")
    print("What do you do?")

    choice = input("> ")

    if "enter" in choice:
        dead("You enter the trapdoor and become trapped beneath the floorboards.")
    elif "turn back" in choice:
        start()
    else:
        print("I'm not sure what you mean.")

def monster_room():
    print("You enter the tunnel that leads you to a monster guarding treasure.")
    print("What do you do?")
    print("Hint: Telling him may be way more difficult than asking.")


    while True:
        choice = input("> ")
        if "tell" in choice:
            dead("The monster decides to eat you in one bite.")
        elif "ask" in choice:
            print("He moves to give you the treasure. Congrats, you win!")
            exit(0)
        else:
            print("I don't understand.")

def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a very dark cave.")
    print("You see tunnels to the left and the right.")
    print("Which tunnel do you enter?")

    choice = input("> ")

    if choice == "left":
        trap_room()
    elif choice == "right":
        monster_room()
    else:
        dead("Your failure to pick a proper tunnel has caused you to die.")

start()
