# in method overriding = an object will use a method that is more closely associated with itself first
# before relying on a method that it may inherit from a parent class.

class Animal():

    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):

    def eat(self):
        print("This rabbit is eating a carrot")


rabbit = Rabbit()
rabbit.eat()

