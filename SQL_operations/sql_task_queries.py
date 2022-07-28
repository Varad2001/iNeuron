import mysql.connector as connection
import logging
import pandas as pd
import numpy as np
logging.basicConfig(filename="sql_crud.log", level=logging.DEBUG, format="%(levelname)s:%(name)s:%(asctime)s:%(message)s")
logging.info("\nPerforming sql queries...")

try:
    mydb = connection.connect(host='localhost', user='root', passwd='Varad@2001', database='ineuron_task')
    logging.info("Database connected successfully.")
except Exception as e:
    logging.exception(e)

cursor = mydb.cursor(buffered=True)

def exec_query(q,get_results):
    try :
        cursor.execute(q)
        logging.info("Query successful.")
    except Exception as e:
        logging.exception(e)

    if get_results==True:
        results = cursor.fetchall()
        for i in results:
            print(i)
        print(len(results))

# q1:perform left join operation with attrubute dataset and dress dataset on column Dress_ID
q1 = "select * from attribute " \
     "left join dress_sales " \
     "on attribute.dress_id = dress_sales.dress_id"
#exec_query(q1)


#q2: Write a sql query to find out how many unique dress that we have based on dress id
q2 = "select count(distinct dress_id) from attribute"
#exec_query(q2)


#q3:find out how many dress is having recommendation 0
#q3_1 = "select recommendation,count(*) from attribute group by recommendation"
#q3_2 = "select count(*) from attribute group by recommendation having recommendation = 0"
q3 = "select count(*) from attribute where recommendation = 0"
#exec_query(q3)


#q4: find out total dress sell for individual dress id

q41="create view dress_sales_total as " \
    "select dress_id,(29_8_2013 + 31_8_2013 + 09_02_2013 + 09_04_2013 + 09_06_2013 + 09_08_2013 + 09_10_2013 + 09_12_2013 + 14_9_2013 + 16_9_2013 + 18_9_2013 + 20_9_2013 + 22_9_2013 + 24_9_2013 + 26_9_2013 + 28_9_2013 + 30_9_2013 + 10_02_2013 + 10_04_2013 + 10_06_2013 + 10_08_2010 + 10_10_2013 + 10_12_2013) as total_sale " \
    "from dress_sales"
q42="create view dress_sales2 as " \
    "select dress_id,sum(total_sale) as total_sale " \
    "from dress_sales_total group by dress_id"
q43="create view attribute2 as select * from attribute group by dress_id"
q4 = "select attribute2.dress_id,dress_sales2.total_sale " \
     "from attribute2 inner join dress_sales2 " \
     "on attribute2.dress_id = dress_sales2.dress_id"
#exec_query(q41,False)
#exec_query(q42,False)
#exec_query(q43,False)
#exec_query(q4,True)

#q5:find out a third highest most selling dress id
q5="select attribute2.dress_id,dress_sales2.total_sale " \
   "from attribute2 inner join dress_sales2 " \
   "on attribute2.dress_id = dress_sales2.dress_id " \
   "order by dress_sales2.total_sale desc " \
   "limit 1 offset 2"
exec_query(q5,True)

