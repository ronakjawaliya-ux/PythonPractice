# multi-level inheritance = when a derived (child) class inherits another derived (child) class

class Organism:    #level-0

    alive = True

class Animal(Organism):    #level-1

    def eat(self):
        print("This animal is eating")

class Dog(Animal):      #level-2

    def bark(self):
        print("This dog is barking")

dog = Dog()
print(dog.alive)           #inherited from the Organism class
dog.eat()                  #inherited from the Animal class
dog.bark()                 #defined in Dog class