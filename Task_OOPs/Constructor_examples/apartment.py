import logging
logging.basicConfig(filename='constructor_examples.log', level=logging.DEBUG, format="%(levelname)s: %(name)s: %(asctime)s: %(message)s")

class apartment :
    name = ''
    wings = 0
    floors = 0
    city = ''
    def __init__(self, name, wings, floors, city):
        self.name= name
        self.wings = wings
        self.floors = floors
        self.city = city
        print("City object instantiated.")

try :
    apt = apartment("Skyrise",8,10,"Pune")
    logging.info("Apartment object instantiated successfully. ")
except Exception as e:
    logging.error(e)