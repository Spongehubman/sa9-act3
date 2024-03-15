
# This file is based on "car.py", a homework Python file I wrote for
# homework assignment 9 in Professor Malasri's COMP-1900-101 course.

require 'ruby_car'

RSpec.describe Car do

    # Lets make an imaginary car called the "Fiat Imaginary".
    let(:fiat) { Car.new("Fiat Imaginary", "Green", 1000)}

    describe "#set_price" do
        it "correctly sets/changes the car's price" do
            fiat.set_price(500)
            expect(fiat.car_price).to eql(500)
        end

        it "correctly outputs the results of updating a car's price" do

            expect{fiat.set_price(500)}.to output("The price of Fiat Imaginary has been updated!\nIts new price is 500.\n").to_stdout
        end
    end

    describe "#paint" do
        it "correctly changes the car's color" do
            fiat.paint('Olive Green')
            expect(fiat.car_color).to eql('Olive Green')
        end

        it "correctly outputs the results of updating a car's color" do

            expect{fiat.paint('Olive Green')}.to output("The Fiat Imaginary has been re-painted!\nIts new color is Olive Green.\n").to_stdout
        end
    end

    describe "#show_car_info" do
        it "successfully prints out the information of the car" do

            expect{fiat.show_car_info}.to output("Car make and model:       Fiat Imaginary\nCar color:                Green\nCar price:               $1000\nCar's Travelled mileage:  0 Miles\n").to_stdout
        end
    end

    describe "#travel" do
        it "correctly shows how much your car has traveled" do
            fiat.travel(200)
            expect(fiat.traveled_mileage).to eq(200)
        end

        it "correctly shows the results of your car travelling a certain distance" do

            expect{fiat.travel(200)}.to output("The Fiat Imaginary has travelled 200 miles!\nIts new mileage is 200 miles.\n").to_stdout
        end
    end
end