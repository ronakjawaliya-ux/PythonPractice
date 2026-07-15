#use of both class_variable and instance_variable

from car_demo import Car

car_1=Car("Chevy","Corvette","2021","blue")
car_2=Car("Ford","Mustang","2022","")

car_1.drive()
car_1.stop()

car_2.drive()
car_2.stop()

car_1.drive()
car_2.stop()

car_2.drive()
car_1.stop()


print(car_1.wheels)
print(car_2.wheels)