import logging
logging.basicConfig(filename='constructor_examples.log', level=logging.DEBUG, format="%(levelname)s: %(name)s: %(asctime)s: %(message)s")

class class_type :
    class_name=''
    no_of_students = 0
    def __init__(self,name , num):
        self.class_name = name
        self.no_of_students = num
        print("Class_type object is instantiated.")

try :
    clst = class_type("Data science", 300)
    logging.info("Class_type object instantiated successfully. ")
except Exception as e:
    logging.error(e)