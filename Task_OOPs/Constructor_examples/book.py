import logging
logging.basicConfig(filename='constructor_examples.log', level=logging.DEBUG, format="%(levelname)s: %(name)s: %(asctime)s: %(message)s")

class book :
    title = ''
    author = ''
    price = 0
    pages = 0
    def __init__(self, title, author, price, pages):
        self.title = title
        self.author = author
        self.price = price
        self.pages = pages
        print("book object instantiated.")

try :
    book = book("Deep work",  "Cal Newport", 500, 300)
    logging.info("Book object instantiated successfully. ")
except Exception as e:
    logging.error(e)