class Dog(object):

    def implicit(self):
        print("DOG implicit")

class Puppy(Dog):

    pass

animal = Dog()
small_animal = Puppy()
animal.implicit()
small_animal.implicit()
