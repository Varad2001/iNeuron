import logging
logging.basicConfig(filename='constructor_examples.log', level=logging.DEBUG, format="%(levelname)s: %(name)s: %(asctime)s: %(message)s")

class internship:
    domain = ''
    stipend = 0
    duration = 0        # in days
    def __init__(self, domain, stipend, duration):
        self.domain = domain
        self.stipend = stipend
        self.duration = duration
        print("Internship object instantiated.")

try :
    intrn = internship("Machine learning",20000, 180)
    logging.info("Internship object instantiated successfully. ")
except Exception as e:
    logging.error(e)
