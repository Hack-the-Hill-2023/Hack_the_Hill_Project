import math
import numpy
import pandas as pd
import pyodbc
from numpy import transpose
import random
import json

def create_dataset():
    listoflists = []
    for x in range(random.randint(1, 15)):
        command_variable = "newlist" + str(x) + " = " + "[]"
        exec(command_variable)
        for y in range(random.randint(4, 28)):
            command_variable = "newlist" + str(x) + ".append( " + str(random.randint(1, 66)) + ")"
            exec(command_variable)
        command_variable = "listoflists.append(" + "newlist" + str(x) + ")"
        exec(command_variable)
    return listoflists


def get_data_from_database(filename):
    # f = open(filename)
    # data=json.load(f)
    # customer_dict = json.loads(data)
    # print(customer_dict['purchase'])


    data = pd.read_json(filename)
    df = pd.DataFrame(data)

    return df

#print(get_data_from_database('generated.json'))


#print(get_data_from_database('generated.json'))


def parse(df):
    #DataFrame=pd.DataFrame(columns=[for i in len(df),i])
    lists=df.values.tolist()
    for x in range(len(lists)):
        array=[]
        lst=lists[x]
        lst=lst[6]
        print(lst)
        for purchase in lst['purchase']:
            print(purchase)
            array.append(purchase)
            print(array)

    return DataFrame

print(parse(get_data_from_database('generated.json')))



# lst=get_data_from_database('generated.json').values.tolist()
#
#
# lst=lst[0]
# lst=lst[6]
# print(lst)
# array=[]
# for key,value in lst:
#     while key=="product_category":
#         array.append(value)
# print(array)
#
#
# lst=lst[0]
# print(lst)
#
#
#



def parsing(filename):
    with open(filename, 'r') as fcc_file:
        fcc_data = json.load(fcc_file)
        print(fcc_data)

        array=[]

        for purchase in fcc_data:
            if key=="procuct_category":
                array.append(value)
                print(array)



    total=1
    return total

print(parsing('generated.json'))



def get_median(dataset):
    array = []
    df = turn_into_dataframe(dataset)

    dictionary = []
    z = df.describe()
    a = z.values.tolist()
    b = a[2]
    c = a[3]
    index = 0
    int = 0
    counter = 0
    for x in range(len(c)):
        if c[x] >= index:
            index = c[x]
            int = x

    res = b[int]

    df = df.replace([res], None)
    return res


def find_interest(dictionary):
    val = 0
    k = "default"
    array = []
    earray = []
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
                #         earray.append(k)
                # k = cluster(earray)
                array.append(k)
                del dictionary[k]
            else:
                array.append(get_median())  # Uncomment when implemented

    return array


def find_interest2(dictionary, user):
    val = 0
    k = "default"
    array = {}
    sums = []
    elements=[]
    col = dictionary[user]
    columnlist = col.values.tolist()
    print(columnlist)
    ct = 0
    res=[]
    # for x in range(len(columnlist)-1):
    #     if columnlist[x] in elements:
    #         sums[x]+=1
    #     else:
    #         sums.append(1)
    #         elements.append(columnlist[x])
    #     print(sums)
    #     print(elements)
    #
    num=0
    for x in range(len(columnlist)):
        if columnlist[x] not in array:
            array[num] = columnlist[x]
            num+=1



    if len(columnlist) >= 4:
        for x in range(5):
            val = 0
            # for integer in range(len(columnlist)):
            #     add = columnlist.count(columnlist[integer])
            #     array[add] = columnlist[integer]
            #
            for key, value in array.items():
                if value >= val:
                    k = key
                res.append(k)
                del array[k]
    else:
        for x in range(5):
            val = 0
            if len(columnlist) != 0:
                for key, value in array:
                    if value >= val:
                        k = key
                    res.append(k)
                    del array[k]
            else:
                res.append(res(get_median(Dataset)))  # Uncomment when implemented

    return res


def combine_categories_with_indices():
    themes = ["Tires & Wheels", "Batteries, Maintenance & Accessories", "Auto Parts",
              "Oils, Fluids, Additives & Chemicals", "ATVs, Snowmobiles, Motorcycles Parts & Accessories",
              "Auto Body Repair, Paints & Accessories", "Exterior Accessories", "Interior Accessories", "Auto Tools",
              "Car Cleaning",

              "Garage Organization & Tool Storage", "Power Tools", "Hand Tools", "Air Tools & Compressors",
              "Paints & Stains", "Ladders & Scaffolding", "Sinks, Faucets & Fixtures",
              "Plumbing", "Power Tool Accessories", "Electrical",

              "Appliances", "Kitchen & Dining", "Household & Cleaning Supplies", "Pet Care", "Furniture & Décor",
              "Heating, Cooling & Air Quality", "Storage & Organization",
              "Home Electronics", "Lighting", "Baby & Toddler",

              "Games Room", "Team Sports", "Winter Sports", "Clothing, Shoes & Accessories", "Fitness & Exercise",
              "Bikes & Accessories", "Toys & Games", "Hunting", "Fishing", "Camping & Hiking",

              "Patio Furniture & Décor", "BBQs, Smokers & Accessories", "Outdoor Power Equipment",
              "Gazebos, Pergolas & Canopies", "Pools, Spas & Accessories", "Outdoor Lighting",
              "Lawn & Garden", "Outdoor Heating", "Mosquito, Insect & Pest Control", "Sheds & Outdoor Storage",

              "Balloons & Accessories", "Party Decorations", "Tableware & Serveware", "Party Favours", "Party Games",
              "Halloween", "Wrapping Paper, Bags & Acc",
              "Cards & Invitations", "Party Cleanup",

              "Snow Removal Equipment", "Winter Sports", "Snowmobile", "Heating, Cooling, & Air Quality",
              "Winter Tires", "Snow Plows & Accessories", "Winter Apparel"]
    nums = []
    for int in range(66):
        nums.append(int)

    res = {}
    for key in themes:
        for value in nums:
            res[key] = value
            nums.remove(value)
            break
    return res


def create_dictionary_transformed_dataset(dataset):
    categories = combine_categories_with_indices()
    dataset2 = []
    for lists in dataset:
        emptylist = []
        for key, value in categories.items():
            for i in lists:
                if i == value:
                    emptylist.append(key)
        dataset2.append(emptylist)

    return dataset2


def turn_into_dataframe(dataset):
    max = 0
    for lists in dataset:
        if len(lists) > max:
            max = len(lists)

    for lists in dataset:
        if len(lists) != max:
            while len(lists) != max:
                lists.append(None)

    transposed = numpy.transpose(dataset)

    for lists in dataset:
        filtered_iterator = filter(None, lists)
        lists = list(filtered_iterator)

    length = len(dataset)
    customers = []
    for i in range(length):
        customers.append(i)

    df = pd.DataFrame(transposed, columns=customers)
    df.dropna()
    return df


# def cluster(interestarray, customerindex,database):
#     col = turn_into_dataframe(database)
#     column = col.values.tolist()

my_dict = {"a": 1, "b": 2, "c": 3}
my_keys = ["a", "b", "d", "a", "c", "e", "b", "b", "c", "d"]
my_keys2 = ["a", "b", "b", "a"]
my_keys3 = []

Database = create_dataset()

Dataset = create_dictionary_transformed_dataset(Database)
# print(x)
DataFrame = turn_into_dataframe(Dataset)

col1 = DataFrame[0]

# print(y)
# pd.set_option('display.max_columns', None)
# y.head()
# print(y)
DictionarySet = combine_categories_with_indices()

#print(find_interest2(DataFrame, 0))
