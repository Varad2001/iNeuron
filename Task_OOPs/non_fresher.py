import logging
import random

from candidate import candidate
logging.basicConfig(filename='examples.log', level=logging.DEBUG, format='%(levelname)s: %(name)s: %(asctime)s: %(message)s')

# posts and companies available in the world for a non fresher
posts = ['Data Scientist', 'Data Engineer', 'Junior software dev', 'Senior software dev', 'Manager', 'System admin', 'DB admin', 'Data analysts']
companies = ['Infosys', 'Wipro', 'Google', 'Amazon', 'Amdocs', 'Accenture', 'Walmart', 'Facebook', 'Netflix', 'TCS']
class non_fresher(candidate):
    recent_post = ''
    recent_salary = ''
    recent_company = ''
    prev_companies = []
    prev_posts = []

    def set_companies(self):
        self.prev_companies.append(companies[random.randrange(0,len(companies))])
        other_comp = companies[random.randrange(0,len(companies))]
        if other_comp not in companies:
            self.prev_companies.append(other_comp)
    def set_posts(self):
        self.prev_posts.append(posts[random.randrange(0, len(posts))])
        other_post = posts[random.randrange(0, len(posts))]
        if other_post not in posts:
            self.prev_posts.append(other_post)

    def __init__(self,name, exp , skills ,post, salary, company):
        if exp == 0:
            print("Experience cannot be zero for a non-fresher.")
        else:
            super().__init__(name,exp,skills)
            self.recent_post = post
            self.recent_salary  = salary
            self.recent_company = company
            self.set_posts()
            self.set_companies()
            logging.info("non fresher object created.")


x = non_fresher("Varad",3,['Python'],"Python dev", 50000,'Infosys')
print(x.prev_posts)
print(x.prev_companies)
