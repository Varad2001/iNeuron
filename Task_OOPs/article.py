import logging, datetime, sys
logging.basicConfig(filename='examples.log', level=logging.DEBUG, format="%(levelname)s: %(name)s: %(asctime)s: %(message)s")

def input_paragraph():
    print("Enter your article paragraphs below.Enter exit when done.")
    para = ''
    for line in sys.stdin:
        if line.lower().rstrip() == 'exit':
            break
        else:
            para = para + line
    return para

class article:
    _title = ''
    _author = ''
    _write_date = datetime.datetime(2001,1,1)
    _filename = ''
    article_list = 'Files/articles.txt'   # file storing the title and the corresponding filename

    @classmethod
    def update_articles_list(self,title, filename):
        logging.info("\nUpdating article list to the file {}...".format(self.article_list))
        info = title.lower()+":"+filename+".txt" +"\n"
        try:
            f = open(self.article_list,"a")
            f.write(info)
            f.close()
            logging.info("Operation successful.")
        except FileNotFoundError as e:
            f = open(self.article_list, "x")
            f.write(info)
            f.close()
            logging.info("Operation successful.")
        except Exception as e:
            logging.exception(e)


    # create an article : anybody can create an article; hence public method
    @classmethod
    def create_article(self):
        logging.info("\nPerforming create_article function...")
        title = input("Enter the title of the article:")
        author = input("Enter the author name:")
        fname = input("Enter the filename:")
        self._title = title
        self._author = author
        self._write_date = datetime.datetime.now()
        self._filename = fname
        try :
            fn = "Files/{}.txt".format(self._filename)
            logging.info("Opening file {} ...".format(fn))
            f = open(fn, "x")
        except FileExistsError as e:
            logging.exception(e)
            print("File already exists.")
            return
        content = self._title.upper() + "\n" + "Author:" + self._author + "\n" + str((self._write_date).strftime("%d %B %Y")) + "\n"
        tmp = input_paragraph()
        content = content + "\n" + tmp
        try :
            logging.info("Performing operations on {}...".format(fn))
            f.write(content)
            f.close()
            logging.info("File operation successful.")
            self.update_articles_list(self._title,self._filename)
        except Exception as e:
            logging.exception(e)

    # showing an article does not need any object of article class; hence it must be declared as static
    @classmethod
    def show_article(self,title):
        logging.info("\nPerforming show_article function..")
        title = title.lower()
        try :
            logging.info("Opening file {}....".format(article.article_list))
            f = open(self.article_list, "r")
            logging.info("{} opened successfully.".format(article.article_list))
        except Exception as e:
            logging.exception(e)
        for line in f:
            try :
                a_name = (line.split(':'))[0].strip()
                fname = (line.split(':'))[1].strip()
                fname = "Files/" + fname
            except IndexError as i:
                print("There are no articles published.")

            if a_name == title:
                logging.info("Title found in the article list file.")
                try :
                    f2 = open(fname, "r")
                    print(f2.read())
                    f2.close()
                    logging.info('Operation completed successfully!')
                    return
                except Exception as e:
                    logging.exception(e)
        print("Article with such title does not exist.")
        logging.info('Article with such title does not exist.')










