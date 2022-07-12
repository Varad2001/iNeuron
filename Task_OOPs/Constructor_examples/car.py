import logging
logging.basicConfig(filename='constructor_examples.log', level=logging.DEBUG, format="%(levelname)s: %(name)s: %(asctime)s: %(message)s")

class car :
    name = ''

    def __init__(self, title, salary , company):
        self.title = title
        self.salary = salary
        self.company = company
        print("Job object instantiated.")

try :
    job = job("Data engineer",50000,"Google")
    logging.info("Job object instantiated successfully. ")
except Exception as e:
    logging.error(e)