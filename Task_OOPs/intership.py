import logging, random
from Job import Job
logging.basicConfig(filename='examples.log', level=logging.DEBUG, format='%(levelname)s: %(name)s: %(asctime)s: %(message)s')

class internship (Job):
    duration = 0    # in months
    type = 'Part time'
    def __init__(self,title, salary,location,duration):
        super().__init__(title, salary, location)
        self.duration =duration
        print("Internship as a {} for {} months at {} with stipend of Rs. {}".format(self.title, self.duration,self.location,self._Job__salary))
        logging.info("Intership object created.")

    # promotion in intership means being picked for a full time job for the same title
    # thus job object is created from intership object and the corresponding internship obj is deleted
    def promote(self, salary):
        logging.info("Intership is being promoted to a job...")
        try :
            print("Congratulations for the new job!")
            new_job = Job(self.title,salary,self.location)
            logging.info("New job object created from internship object.")
            del self
            logging.info("Current internship object deleted.")
            return new_job
        except Exception as e:
            logging.exception(e)

   # assess the candidate
    def is_employable(self):
        assessment = random.randrange(1,10,1)
        if assessment > 5:
            return True
        else :
            return False

   # after completion, the candidate may or may not receive job offer based on the assessment
    def complete(self):
        print("Internship is complete. ")
        logging.info("Internship is complete.")
        if self.is_employable():
            self.promote(random.randrange(50000,80000,500))
        else :
            print("The internship is complete and a certificate has been provided. Sorry, no offer letter has been offered.")


myintern = internship('Junior Data Scientist',50000,'Pune',6)
myintern.complete()

