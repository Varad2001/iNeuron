import logging
from candidate import candidate
from fresher import fresher
from Job import Job
logging.basicConfig(filename='examples.log', level=logging.DEBUG, format='%(levelname)s: %(name)s: %(asctime)s: %(message)s')

# There is a specific interview for each specific candidate.
class interview:
    __company = ''
    job_title = ''
    no_of_rounds = 0
    __rounds_cleared = 0
    __candidate = None
    __interview_panel = ()

    def show_info(self):
        print("Interview details:")
        print("Company:", self.__company)
        print("Job title:", self.job_title)
        print("No of rounds:{} ".format(self.no_of_rounds))
        print("Candidate:", self.__candidate.get_name())
        print("Interview panel:",end='')
        for i in self.__interview_panel:
            print(i,end='    ')
        print("\n")
    def __init__(self, company,title, rounds, candidate, panel):
        self.__company =company
        self.job_title = title
        self.no_of_rounds = rounds
        self.__candidate = candidate
        self.__interview_panel = panel
        self.show_info()
        logging.info("Interview scheduled.")
        self.appear_for_round()

    def appear_for_round(self):
        if self.__rounds_cleared == self.no_of_rounds :
            print("Congratulations! You have cleared the interview!")
            self.offer_job()
            return
        print("Appearing for round {}..".format(self.__rounds_cleared + 1))
        if self.__candidate.clear_round():
            self.__rounds_cleared = self.__rounds_cleared + 1
            print("Congrats! You've cleared round no. {}.".format(self.__rounds_cleared))
            self.appear_for_round()
        else :
            print("Sorry! You have failed in the round {}. Better luck next time.".format(self.__rounds_cleared+1))

    def offer_job(self):
        logging.info("Offerring the job..")
        new_job = Job(self.job_title,self.__candidate.aptitude * 10000, 'Pune')


"""varad = candidate("Varad Khonde", 0, ['Pandas'])
varad.upskill('Data Science')
amazon_int = interview('Amazon','Data Scientist',3,varad,("John","Ram"))"""
varad = fresher("Varad Khonde", ['Software dev.'], {'college': 'GECA', 'degree':'BE', 'branch':'CSE', 'cgpa':9})
varad.study_further('IIT B','MTech','CSE')
amazon_int = interview('Amazon','Data Scientist',3,varad,("John","Ram"))