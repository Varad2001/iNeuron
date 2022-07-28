import datetime

import pymongo
import pandas as pd
import numpy as np
import json
import logging
logging.basicConfig(filename='mongodb.log', level=logging.DEBUG, format="%(levelname)s:%(name)s:%(asctime)s:%(message)s")
logging.info("\nInserting data into mongodb...")

try:
    client = pymongo.MongoClient("mongodb+srv://varadkhonde:yadneshkhonde@cluster0.zeesz.mongodb.net/?retryWrites=true&w=majority")
    db = client.test
except Exception as e:
    logging.info(e)

mydb = client["Ineuron_task"]
attribute_table= mydb["attribute"]
dress_sales_table = mydb["dress_sales"]

"""# import the dataset
df1 = pd.read_excel("../Data/Attribute DataSet.xlsx")

data_list = []              # stores list of dictionaries

for i in range(df1.shape[0]):           # for every row in the dataframe
    row = df1.loc[i,:]
    indexes = list(row.index)           # contains columns names
    values = list(row.values)           # contains values
    data = {}
    for j in range(len(indexes)):            # for every index, value of the row
        if type(values[j]) == np.int64:      # convert np.int64 into int
            values[j] = int(str(values[j]))
        data[indexes[j]] = values[j]        # add the record to the dict, {'index':'value'}

    data_list.append(data)                  # append the dict to the list

attribute_table.insert_many(data_list)"""


df2 = pd.read_excel("../Data/Dress Sales.xlsx")
# dress_sales columns contains string which represent datetime, hence taken as datetime object by dataframe
# convert those objects to normal strings
for col in df2.columns:
    old_col_name = col
    new_name = col
    if type(col) == datetime.datetime:          # if the column_name is of datetime object
        col = str(col)                          # convert to string
        col=col.split(' ')                      # returns list of date and time
        col=col[0]                              # select date
        new_name = col
    df2.rename(columns={old_col_name:new_name},inplace=True)      # update the column names
print(df2.columns)


data_list = []              # stores list of dictionaries

for i in range(df2.shape[0]):           # for every row in the dataframe
    row = df2.loc[i,:]
    indexes = list(row.index)           # contains columns names
    values = list(row.values)           # contains values
    data = {}
    for j in range(len(indexes)):            # for every index, value of the row
        if type(values[j]) == np.int64:      # convert np.int64 into int
            values[j] = int(str(values[j]))
        elif type(values[j]) == str:           # all values in this excel file are int, so remove str
            values[j] = 0
        data[indexes[j]] = values[j]        # add the record to the dict, {'index':'value'}

    data_list.append(data)                  # append the dict to the list

dress_sales_table.insert_many(data_list)



