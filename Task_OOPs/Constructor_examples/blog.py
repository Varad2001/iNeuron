import logging
logging.basicConfig(filename='constructor_examples.log', level=logging.DEBUG, format="%(levelname)s: %(name)s: %(asctime)s: %(message)s")

class blog:
    author = ''
    no_of_posts = 0
    followers = 0
    title = ''
    def __init__(self, author, posts, foll, title):
        self.author = author
        self.no_of_posts = posts
        self.followers = foll
        self.title = title
        print("Blog object instantiated.")

try:
        blog = blog("Varad",20,2000,"Research in data science")
        logging.info("Blog object instantiated successfully. ")
except Exception as e:
        logging.error(e)