import logging,random
from candidate import candidate
logging.basicConfig(filename='examples.log', level=logging.DEBUG, format='%(levelname)s: %(name)s: %(asctime)s: %(message)s')

class fresher(candidate):
    experience = 0
    # academic record: college, cgpa, branch
    academic_record = {'college' : '','degree':'',  'branch' : '', 'cgpa' : 0}
    def __init__(self, name, skills, academic_record):
        super().__init__(name, 0, skills)
        self.academic_record = academic_record
        logging.info("fresher object created.")

    def study_further(self, college,degree, branch):
        self.academic_record['college'] = college
        self.academic_record['degree'] = degree
        self.academic_record['branch'] = branch
        # the fresher now is enrolled in another degree; so the cgpa would also change
        cgpa = random.randrange(5,9,1)
        self.academic_record['cgpa'] = cgpa
        print("{} studied {} {} at {} and has cgpa of {}.".format(self.get_name(),degree,branch, college,cgpa))

