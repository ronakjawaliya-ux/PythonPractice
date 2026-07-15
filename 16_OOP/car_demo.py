class Car:

    wheels = 4 #class_variable

    def __init__(self,make,model,year,color):
        self.make = make       #instance_variable
        self.model = model     #instance_variable
        self.year = year       #instance_variable
        self.color = color     #instance_variable

    def drive(self):
        print("This "+self.model+" is driving")

    def stop(self):
        print("This "+self.model+" is stopped")