import mysql.connector as connection
import logging
logging.basicConfig(filename="sql_crud.log", level=logging.DEBUG, format="%(levelname)s:%(name)s:%(asctime)s:%(message)s")
logging.info("\nCreating a table...")

mydb = connection.connect(host='localhost', user='root', passwd='Varad@2001',database='ineuron_task')
cursor = mydb.cursor()

query1 = "create table Attribute (" \
        "dress_id int," \
        "style varchar(30)," \
        "price varchar(10)," \
        "rating float," \
        "size varchar(15)," \
        "season varchar(33)," \
        "neckline varchar(33)," \
        "sleevelength varchar(33)," \
        "waiseline varchar(33)," \
        "material varchar(33)," \
        "fabrictype varchar(33)," \
        "decoration varchar(33)," \
        "patterntype varchar(33)," \
        "recommendation int" \
        ")"

query2 = "create table dress_sales(" \
         "dress_id int," \
         "29_8_2013 int," \
         "31_8_2013 int," \
         "09_02_2013 int," \
         "09_04_2013 int," \
         "09_06_2013 int," \
         "09_08_2013 int," \
         "09_10_2013 int," \
         "09_12_2013 int," \
         "14_9_2013 int," \
         "16_9_2013 int," \
         "18_9_2013 int," \
         "20_9_2013 int," \
         "22_9_2013 int," \
         "24_9_2013 int," \
         "26_9_2013 int," \
         "28_9_2013 int," \
         "30_9_2013 int," \
         "10_02_2013 int," \
         "10_04_2013 int," \
         "10_06_2013 int," \
         "10_08_2010 int," \
         "10_10_2013 int," \
         "10_12_2013 int" \
         ")"



cursor.execute(query1)
#cursor.execute(query2)

