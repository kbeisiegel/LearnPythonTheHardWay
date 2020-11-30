from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('diamond')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):

    quips = [
        "You have died, you suck at this game.",
        "Wow, you're trash."
]


    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class Lobby(Scene):

    def enter(self):
        print(dedent("""
            You find yourself standing in a lobby area.
            All of the sudden, a group of criminals storm past you.
            They are robbers who have stolen very rare diamonds who
            are attempting to make a getaway through the maze of rooms.
            You have to act fast in order to catch them.

            You see a door to your left and a door to your right.
            You're not entirely sure which door they went through,
            since they were running so fast. Which door do you choose?
            """))

        choice = input("> ")

        if 'left' in choice:
            print("""
            You stumble into a room of forests.
            """)
            return 'jungle'

        elif 'right' in choice:
            print("""
            You enter into a room with a huge pond filled with koi fish.
            """)
            return 'koipond'

        else:
            print("I have no clue what you mean.")


class Jungle(Scene):

    def enter(self):
        print(dedent("""
            In this jungle, there's so many trees everywhere,
            it makes it easy for the robbers to hide.
            Ultimately, they get away and you
            failed your mission.
            """))
        Death()

class Desert(Scene):

    def enter(self):
        pass

class Diamond(Scene):

    def enter(self):
        print(dedent("""
            You enter into the final room to find the robbers
            stopped in their tracks, with no where else to go.
            You take down and handcuff each one, and return
            the diamond to their rightful owner. Congrats! You
            won!
            """))

class Red(Scene):

    def enter(self):
        print(dedent("""
            This room is all lit up in various colors of red.
            You can sense that the robbers just passed through
            this room. You must enter the correct code, to be
            granted access to the next room. The code is 2 digits
            and will only allow for 5 attempts before you are locked out.
            """))

        redcode = f"{randint(1,3)}{randint(1,3)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != redcode and guess < 5:
            print("WRONG")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == redcode:
            print(dedent("""
                The door shakes and the lock falls off. You
                have entered the correct code and have been granted
                access into the final room. As you proceed toward the
                next room, diamonds are flashing through the window
                and catch your eye.
                """))
            return 'diamond'

        else:
            print(dedent("""
                The doors shake and everything trembles around you.
                It feels like an earthquake is happening right beneath
                your feet. The temperature in the room is very warm,
                and is making you sweat profusely. You become locked in
                this sauna of a room and ultimately, the robbers get away
                and you have failed your mission.
                """))
            return 'death'

class KoiPond(Scene):

    def enter(self):
        print(dedent("""
            All of the doors are locked around you.
            You can't see the robbers anywhere in this room, but you
            can tell that they were just here recently. To continue
            past this room, you must guess how many different type of
            koi fish live in this pond. The code is 3 digits and will
            only allow 10 attempts until you become locked out.
            """))

        code = f"{randint(1,5)}{randint(1,5)}{randint(1,5)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("WRONG!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
                You hear everything move around you, as a door clicks
                and unlocks for you. Allowing you to proceed through.
                """))
            return 'red'
        else:
            print(dedent("""
                Everything moves and shakes around you,
                the doors stay locked and you are now
                trapped with the koi fish.
                """))
            return 'death'


class Map(object):

    scenes = {
        'lobby': Lobby(),
        'koipond': KoiPond(),
        'jungle': Jungle(),
        'desert': Desert(),
        'red': Red(),
        'diamond': Diamond(),
        'death': Death()
    }


    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('lobby')
a_game = Engine(a_map)
a_game.play()
