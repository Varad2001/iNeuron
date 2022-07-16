import logging
logging.basicConfig(filename='examples.log', level=logging.DEBUG, format='%(levelname)s: %(name)s: %(asctime)s: %(message)s')

class Job:
    title = ''
    __salary = 0
    location = ''
    type = 'Full time'
    def __init__(self,title, salary,location):
        self.title = title
        self.__salary = salary
        self.location = location
        print("Job title:{}\tSalary:Rs.{}/month\tLocation:{}".format(self.title,self.__salary,self.location))
        logging.info("Job object created.")
    def set_salary(self, salary):
        logging.info("Current salary for my {} job is {}.".format(self.title,self.__salary))
        self.__salary = salary
        logging.info("Salary changed to {}.".format(self.__salary))
    def promote(self, salary, title):
        logging.info("Promotion request...")
        self.set_salary(salary)
        self.title = title
        print("Promotion approved. {} : Rs. {}/month".format(self.title,self.__salary))
        logging.info("Promotion approved. {} : Rs. {}".format(self.title,self.__salary))

if (__name__ == '_main_'):
    myjob = Job('Data Engineer', 100000, 'Pune')
    myjob.promote(200000,'Data scientist')
