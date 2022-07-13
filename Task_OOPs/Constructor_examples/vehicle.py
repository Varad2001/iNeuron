import logging
logging.basicConfig(filename='inheritance_examples.log', level=logging.DEBUG, format="%(levelname)s: %(name)s: %(asctime)s: %(message)s")

class vehicle:
    no_of_wheels = 0
    fuel_type = ''
    fuel_amt = 10    # litres
    max_fuel_limit = 0  # litres
    def __init__(self, wheels, fuel):
        self.no_of_wheels = wheels
        self.fuel_type = fuel
    def show_fuel(self):
        print("Vehicle has {} litres of {} currently.".format(self.fuel_amt, self.fuel_type))
    def refill(self, amt):
        self.show_fuel()
        new_amt = self.fuel_amt + amt
        if new_amt <= self.max_fuel_limit:
            self.fuel_amt = new_amt
            self.show_fuel()
        else :
            print("Refill amount exceeds maximum fuel limit. Enter smaller amount.")

            
 try :
    car = vehicle(4,'Diesel')
    logging.info("Vehicle object instantiated successfully. ")
except Exception as e:
    logging.error(e)

car.max_fuel_limit = 30
car.show_fuel()
car.refill(40)
car.refill(10)
