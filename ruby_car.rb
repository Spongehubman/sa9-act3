
# This file is based on "car.py", a homework Python file I wrote for
# homework assignment 9 in Professor Malasri's COMP-1900-101 course.

class Car

    def initialize(make_and_model, car_color, car_price)
        @make_and_model = make_and_model
        @car_color = car_color
        @car_price = car_price
        @traveled_mileage = 0

    end
    
    def set_price(p)
        @car_price = p
        puts "The price of #{@make_and_model} has been updated!"
        puts "Its new price is #{@car_price}."

    end

    def paint(c)
        @car_color = c
        puts "The #{@make_and_model} has been re-painted!"
        puts "Its new color is #{@car_color}."

    end

    


end