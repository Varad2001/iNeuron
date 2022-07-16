import logging, random
logging.basicConfig(filename='examples.log', level=logging.DEBUG, format='%(levelname)s: %(name)s: %(asctime)s: %(message)s')

class candidate:
    __name = ''
    experience = 0
    skills = []        # list of the skills the candidate possesses
    aptitude = random.randrange(4,10,1)      # aptitude can be 1 to 10
    def __init__(self,name, exp, skills):
        self.__name = name
        self.experience = exp
        self.skills = skills
    def get_name(self):
        return self.__name

    def clear_round(self):
        logging.info("Appearing for the interview round...")
        test_score = random.randrange(20,100,2)
        if test_score > 50 :
            return True
        else :
            return False
    def upskill(self, new_skill):
        logging.info("Upskilling..")
        print("Learning new skill:{}".format(new_skill))
        self.skills.append(new_skill)
        print("{} skill learned.".format(new_skill))
        logging.info("new skill learned.")




