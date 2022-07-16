import logging
from article import article
from website import website
logging.basicConfig(filename='examples.log', level=logging.DEBUG, format="%(levelname)s: %(name)s: %(asctime)s: %(message)s")

class blogpost(article,website):
    parent_blog = ''
    type = 'blogpost'       # website type attribute from website class
    article_list = 'Files/blogposts.txt'     # attribute from article class
    def __init__(self):
        pass
    def create_article(self,name):
        logging.info("\nCreating new blogpost....")
        try :
            logging.info("Calling create_article method from article class....")
            super().create_article()
            logging.info("Calling method successful.  ")
        except Exception as e:
            logging.exception(e)
        self.parent_blog = name
        self.url = "https://www.{}.blog/{}".format(self.parent_blog,self._title.lower())
        logging.info("A new blogpost named {} is created.".format(name))




