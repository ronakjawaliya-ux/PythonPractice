#classes can have children classes:
# 1 the children class will inherit everything that there parent class have (attributes and methods).
# 2 the children class can also implement there own unique attributes and methods as well.


class Animal:

    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):
    def run(self):
        print("This rabbit is running")

class Dog(Animal):
    def swim(self):
        print("This dog is swimming")
class Cat(Animal):
    def fly(self):
        print("This cat is flying")


rabbit = Rabbit()
dog = Dog()
cat = Cat()

#print(rabbit.alive)
#dog.eat()
#cat.sleep()

rabbit.run()
dog.swim()
cat.fly()