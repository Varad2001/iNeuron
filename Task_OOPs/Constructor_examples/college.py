import logging
logging.basicConfig(filename='constructor_examples.log', level=logging.DEBUG, format="%(levelname)s: %(name)s: %(asctime)s: %(message)s")

class college :
    name = ''
    NIRF_rank = 0
    location = ''
    def __init__(self, name, NIRF_rank, location):
        self.name = name
        self.NIRF_rank = NIRF_rank
        self.location = location
        print("College object instantiated.")

try :
    clg = college("IIT", 2, "Bombay")
    logging.info("College object instantiated successfully. ")
except Exception as e:
    logging.error(e)