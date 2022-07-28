import mysql.connector as connection
import logging
logging.basicConfig(filename="sql_crud.log", level=logging.DEBUG, format="%(levelname)s:%(name)s:%(asctime)s:%(message)s")
logging.info("\nReading a table...")

try:
    mydb = connection.connect(host='localhost', user='root', passwd='Varad@2001', database='ineuron_task')
    logging.info("Database connected successfully.")
except Exception as e:
    logging.exception(e)

cursor = mydb.cursor(buffered=True)
q1 = "select * from attribute"
q2 = "select * from dress_sales"
try:
    cursor.execute(q3)
except Exception as e:
    logging.exception(e)

results = cursor.fetchall()
print(len(results))
