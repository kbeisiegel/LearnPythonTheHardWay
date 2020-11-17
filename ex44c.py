class Other(object):

    def implicit(self):
        print("OTHER implicit")

class Dog(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

animal = Dog()
animal.implicit()
