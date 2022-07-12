import logging
logging.basicConfig(filename='constructor_examples.log', level=logging.DEBUG, format="%(levelname)s: %(name)s: %(asctime)s: %(message)s")


class course:
    course_name = ''
    course_price = 0
    duration = 0  # in days

    def __init__(self, name, price, duration):
        self.course_name = name
        self.course_price = price
        self.duration = duration
        print("Course object instantiated.")

try:
        course = course("Full stack data science",10000,365)
        logging.info("course object instantiated successfully. ")
except Exception as e:
        logging.error(e)