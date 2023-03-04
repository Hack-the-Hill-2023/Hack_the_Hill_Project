import math

import pandas as pd
import pyodbc

path = 'Driver={SQL Server};''Server=KAAN-HP;''Database=Python3_Test;''Trusted_Connection=yes;'


def get_data(path):
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=KAAN-HP;'
                          'Database=Python3_Test;'
                          'Trusted_Connection=yes;')
    conn = pyodbc.connect(path)

    col1 = pd.read_sql_query("SELECT columnX FROM table1", conn)  # Automatically turns the DB data into a DataFrame
    col2 = pd.read_sql_query("SELECT columnY FROM table1", conn)  # Automatically turns the DB data into a DataFrame
    table = pd.read_sql_query("SELECT * FROM table1", conn)  # Gets the entire table
    return table


def get_interestlist(purchaselist, dictionary):
    for key in purchaselist:
        if key in dictionary:
            dictionary[key] += 1
        else:
            dictionary[key] = 0
            if dictionary[key] >= 0:
                dictionary[key] += 1
    return dictionary


def get_median():
    array = []
    df = get_data(path)
    z = df.theme.mode()
    df.loc[df[df.theme] == z, df.theme] = math.nan  # may need some changing
    array.append(z)
    return array


def find_interest(dictionary):
    val = 0
    k = "default"
    array = []

    if len(dictionary) >= 4:
        for x in range(5):
            val = 0
            for key in dictionary:
                value = dictionary[key]
                if value > val:
                    k = key
                    val = value
            array.append(k)
            del dictionary[k]
    else:
        for x in range(5):
            val = 0
            if len(dictionary) != 0:
                for key in dictionary:
                    value = dictionary[key]
                    if value > val:
                        k = key
                        val = value
                array.append(k)
                del dictionary[k]
            else:
                array.append(3)
                # array.append(get_median())  # De comment when implemented

    return array


my_dict = {"a": 1, "b": 2, "c": 3}
dict = {}
my_keys = ["a", "b", "d", "a", "c", "e", "b", "b", "c", "d"]
my_keys2 = ["a", "b", "c", "a"]
my_keys3 = []

new_dict = get_interestlist(my_keys2, dict)
print(new_dict)
print(find_interest(new_dict))
