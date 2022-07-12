import logging
logging.basicConfig(filename='constructor_examples.log', level=logging.DEBUG, format="%(levelname)s: %(name)s: %(asctime)s: %(message)s")

class animal :
    name = ''
    age = 0
    is_hungry = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Dog object instantiated.")
    def eat(self):
        self.is_hungry = False
    def run(self):
        self.is_hungry = True

try :
    dog = animal("dog",10)
    logging.info("Dog object instantiated successfully. ")
except Exception as e:
    logging.error(e)