
# Nicholas Folis

# Kriangsiri Malasri

# COMP-1900-101

# 12/5/22


# This program defines the "Car" class, and describes various instance attributes for instance
# objects created using the "Car" class. New instance objects will be made using this class,
# and their instance attributes will be printed as output (with some edited) later on.

# Defining the "Car" class, which is the "outer skeleton" for the inside methods of "Car".
class Car():

        # Defining the __init__(self, make_and_model, car_color, car_price) constructor.
        # This constructor makes new "Car" object for a variable that assign's the object's
        # "make_and_model", "car_color", and "car_price" attributes, and initializes the object's
        # "traveled_mileage" attribute to zero.
        def __init__(self, make_and_model, car_color, car_price):
                self.make_and_model = make_and_model
                self.car_color = car_color
                self.car_price = car_price
                self.traveled_mileage = 0

        # Defining set_price(self, p), which will update the (instance object) car's price attribute.
        # The instance object and its respective "car_price" attribute are printed below as well.
        # The two "print" statements are 'combined' by using "end = """. They tell the user what
        # was updated.
        def set_price(self, p):
                self.car_price = p
                print(f"The price of {self.make_and_model} has been updated! ", end = "")
                print(f"Its new price is ${self.car_price:.2f}.")

        # Defining paint(self, p), which will update the (instance object) car's color attribute.
        # The instance object and its respective "car_color" attribute are printed below as well.
        # The two "print" statements are 'combined' by using "end = """. They tell the user what
        # was updated.
        def paint(self, c):
                self.car_color = c
                print(f"The {self.make_and_model} has been re-painted! ", end = "")
                print(f"Its new color is {self.car_color}.")
    
        # Defining show_car_info(self), which show's the (instance object) car's info. Namely,
        # the respective object's attributes for make_and_model, car_color, car_price, and traveled_mileage
        # are printed out. Spaces within the "print" statements' values are used to make the output look nicer
        # when printed out. Four "print" statements tell the user the instance object's instance attribute values.
        def show_car_info(self):
                print(f"Car make and model:      {self.make_and_model}")
                print(f"Car color:               {self.car_color}")
                print(f"Car price:              ${self.car_price:.2f}")
                print(f"Car's traveled mileage:  {self.traveled_mileage} Miles")

        # Defining travel(self, distance), which increases the respective object's traveled_mileage
        # attribute by the value of distance passed onto this function definition. Also printed below
        # is the instance object's respective values for its "make_and_model" and new "traveled_mileage"
        # instance variables. The "distance" traveled in "miles" ("miles" is a quotation but not a variable
        # or attribute) is also printed as output.
        def travel(self, distance):
                print(f"The {self.make_and_model} has traveled {distance} miles! ", end = "")
                self.traveled_mileage += distance
                print(f"Its new mileage is {self.traveled_mileage} miles.")

#---------------------------------------------------------------------------------------------------

# A "print" function to make space from the top of the program's execution on Idle.
print()

# The statements below create two new "Car" instance objects for the variables "cayman" and "corolla".
# Their respective instance attribute values for "make_and_model", "car_price", "car_color", and
# "traveled_mileage" are assigned from the respective arguments for each class method call.
cayman = Car("Porsche 718 Cayman GTS 4.0", "Black", 90300)
corolla = Car("Toyota Corolla LE", "Red", 21500)


# The statements below call the show_car_info(self) object method for the instance objects of both
# cayman and corolla. Each instance object's instance variables will be printed out according to the
# class method's definition of show_car_info(self) given above.
Car.show_car_info(cayman)

# A "print" statement is here to create extra spacing between method calls.
print()
Car.show_car_info(corolla)

# Two "print" statements are here to create extra spacing between method calls.
print()
print()


# These two paint() method calls are used to change the instance attribute "car_color" for each of the
# respective instance objects named below. The instance object attached to "cayman" has its instance attribute
# "car_color" changed to "Olive Green", and the instance object attached to "corolla" has its instance attribute
# "car_color" changed to "Blue".
cayman.paint("Olive Green")

# A "print" statement is here to create extra spacing between method calls.
print()
corolla.paint("Blue")

# Two "print" statements are here to create extra spacing between method calls.
print()
print()


# The two travel() method statements below change each instance object's respective "traveled_mileage"
# attribute to the new arguments "6500" and "4000".
cayman.travel(6500)

# A "print" statement is here to create extra spacing between method calls.
print()
corolla.travel(4000)

# Two "print" statements are here to create extra spacing between method calls.
print()
print()


# The two set_price() method statements below change each instance object's respective "car_price" attribute
# to the new arguments "82000" and "19500".
cayman.set_price(82000)

# A "print" statement is here to create extra spacing between method calls.
print()
corolla.set_price(19500)

# Two "print" statements are here to create extra spacing between method calls.
print()
print()


# The statements below call the show_car_info() object method for the instance objects of both
# cayman and corolla. These method calls show the updated "car_color", "car_price", and "traveled_mileage"
# for each respective instance object.
Car.show_car_info(cayman)

# A "print" statement is here to create extra spacing between method calls.
print()
Car.show_car_info(corolla)

# This "print" statement creates extra spacing, just in case.
print()

