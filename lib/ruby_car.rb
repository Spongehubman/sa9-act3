
# This file is based on "car.py", a homework Python file I wrote for
# homework assignment 9 in Professor Malasri's COMP-1900-101 course.

class Car
    attr_accessor :make_and_model, :car_color, :car_price, :traveled_mileage


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

    def show_car_info
        puts "Car make and model:       #{@make_and_model}"
        puts "Car color:                #{@car_color}"
        puts "Car price:               $#{@car_price}"
        puts "Car's Travelled miliage:  #{@traveled_mileage} Miles"
    end

    def travel(distance)
        puts "The #{@make_and_model} has travelled #{distance} miles!"
        @traveled_mileage += distance
        puts "Its new mileage is #{@traveled_mileage} miles."
    end
end

#==================================
