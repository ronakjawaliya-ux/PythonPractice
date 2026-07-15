# multiple inheritance = when a class is derived from more than one parent class

class Prey:    #Parent class-1

     def flee(self):
         print("This animal flees")

class Predator:     #Parent class-2

    def hunt(self):
        print("This animal hunts")


class Rabbit(Prey):     #Child class-1
    pass

class Hawk(Predator):   #Child class-2
    pass

class Fish(Prey, Predator):   #Child class-3
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.hunt()
fish.flee()