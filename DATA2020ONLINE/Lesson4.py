# Object Oriented Way
# Improves code re-use
# Think of an object - car
#A car has attributes/state/properties = color, weight, height,age, size, name
#A car has behaviors/functions - what it does, move(), carry(), hoot()

# lets understand it
# A class is where the object lives - blueprint/template
class Car:

    def __init__(self):
        self.name = 'Nissan'
        self.weight = 500
        self.color = 'Blue'
        self.age = 10
        self.mileage = 50000
        # above we define attributes of a car as variables



    def move(self):
        print('A car is moving')
        print('The car weight is ',self.weight)
        print('The car mileage is ', self.mileage)

    def carry(self):
        print('The car is Carrying')
        print('The car weight is ', self.weight, 'Kgs')
        print('The car age is ', self.age)


# Use object
object = Car() # instantiate
object.move()
object.carry()

# .(dot) - you are accessing the behaviours/functions of an object








