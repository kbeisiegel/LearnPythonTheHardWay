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

    def enter(self):
        pass

class Lobby(Scene):

    def enter(self):
        pass

class Jungle(Scene):

    def enter(self):
        pass

class Desert(Scene):

    def enter(self):
        pass

class Diamond(Scene):

    def enter(self):
        pass

class Red(Scene):

    def enter(self):
        pass

class KoiPond(Scene):

    def enter(self):
        pass

class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

a_map = Map('lobby')
a_game = Engine(a_map)
a_game.play()
