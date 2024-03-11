
# This file is based on "car.py", a homework Python file I wrote for
# homework assignment 9 in Professor Malasri's COMP-1900-101 course.

require 'ruby_car'

RSpec.describe Car do

    # Lets make an imaginary car called the "Fiat Imaginary".
    let(:fiat) { Car.new("Fiat Imaginary", "Green", "1000")}

    describe "#set_price" do
        it "correctly sets/changes the car's price" do
            fiat.set_price(500)
            expect(fiat.car_price).to eql(500)
        end
    end

    describe "#paint" do
        it "correctly changes the car's color" do
            fiat.paint('Olive Green')
            expect(fiat.car_color).to eql('Olive Green')
        end
    end

    describe "#show_car_info" do
        it "successfully prints out the information of the car" do
            fiat.show_car_info
        end
    end

    describe "#travel" do
        it "correctly shows how much your car has traveled" do
            fiat.travel(200)
            expect(fiat.traveled_mileage).to eq(200)
        end
    end
end