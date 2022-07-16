import logging
from blogpost import blogpost
logging.basicConfig(filename='examples.log', level=logging.DEBUG, format="%(levelname)s: %(name)s: %(asctime)s: %(message)s")

class blog:
    _no_of_posts = 0
    _name = ''
    _blogposts = blogpost.article_list
    def __init__(self,name):
        self._name = name
        logging.info("\n A blog with name {} is created.".format(self._name))
    def create_blogpost(self):
        logging.info("\nCreate blogpost request from {}...".format(self._name))
        new_post = blogpost()
        try :
            new_post.create_article(self._name)
            logging.info("New blogpost ({}) created successfully. ".format(new_post._title))
        except Exception as e:
            logging.exception(e)
        self._no_of_posts = self._no_of_posts + 1

    def show_post(self,title):
        print("******* {} blog *******".format(self._name))
        print()
        blogpost.show_article(title)






logging.info("\nEXECUTING BLOG.PY FILE.....")
# create a blog
myblog = blog("Data Science")
myblog.create_blogpost()
myblog.create_blogpost()
myblog.show_post('seaborn')
myblog.show_post('ss')
