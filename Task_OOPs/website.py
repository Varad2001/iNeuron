import logging
logging.basicConfig(filename='examples.log', level=logging.DEBUG, format="%(levelname)s: %(name)s: %(asctime)s: %(message)s")

class website:
    url = ''
    type = 'general website'   # type can be : 'general website' or 'blogpost'
    def __init__(self, url):
        self.url = url

    def show_info(self):
        print("This is a {} with url:{}".format(self.type,self.url))
