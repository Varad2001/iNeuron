import mysql.connector as connection
import logging
import pandas as pd
import numpy as np
logging.basicConfig(filename="sql_crud.log", level=logging.DEBUG, format="%(levelname)s:%(name)s:%(asctime)s:%(message)s")
logging.info("\nInserting values...")

try:
    mydb = connection.connect(host='localhost', user='root', passwd='Varad@2001', database='ineuron_task')
    logging.info("Database connected successfully.")
except Exception as e:
    logging.exception(e)

cursor = mydb.cursor()

def insert_excel_data(file_path,table_name):
    # read attribute dataset values from the respective excel file
    try :
        df = pd.read_excel(file_path, keep_default_na=False)
        logging.info("Excel file found successfully.")
    except Exception as e:
        logging.info(e)

    s = ''
    for i in range(df.shape[1]):
        s=s+'%s,'
    s=s[0:-1:1]
    #print(s)  ==> %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s

    query = ("insert into {} values ({})".format(table_name,s))


    for i in range(df.shape[0]):
        row=df.loc[i,:]
        l = []                               # list to append the values of columns

        for value in row:
            if type(value)==np.int64:       # attribue dataset contains numpy.int64 values
                value=int(str(value))
            elif type(value)==str:
                # dress_sales dataset should not contain any string;
                # after printing data which could not be inserted, following string values were present
                # thus, convert those values to 0
                if value.lower() in ('removed','orders') or value == '':
                    value = 0
            else :
                pass

            l.append(value)

        data=tuple(l)
        # data is ready to be inserted

        try:
            cursor.execute(query, data)
            logging.info("Insert query successful.")
        except Exception as e:
            logging.info("Following record could not be inserted:",data)
            logging.exception(e)

    mydb.commit()


file1 = "../Data/Attribute DataSet.xlsx"
file2 = "../Data/Dress Sales.xlsx"

#insert_excel_data(file1,'attribute')
insert_excel_data(file2,'dress_sales')

