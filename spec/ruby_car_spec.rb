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




end