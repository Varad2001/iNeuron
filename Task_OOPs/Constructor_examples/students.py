import logging
logging.basicConfig(filename='constructor_examples.log', level=logging.DEBUG, format="%(levelname)s: %(name)s: %(asctime)s: %(message)s")

class student :
    name = ''
    roll_no = 0
    email = ''
    age = 0
    # constructor
    def __init__(self, name , roll_no, email, age):
        self.name = name
        self.roll_no = roll_no
        self.email = email
        self.age = age
        print("Student object instantiated.")

try :
    std = student("varad", 1, "varad@gmail.com", 20)        # right number of arguments passed
    logging.info("student object instantiated successfully. ")
except Exception as e:
    logging.error(e)


