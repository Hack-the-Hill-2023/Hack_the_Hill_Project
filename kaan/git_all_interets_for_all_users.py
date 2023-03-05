import json

filename = './generated.json'


def parser():
    fcc_data = None
    array= []

    with open(filename, 'r') as fcc_file:
        fcc_data = json.load(fcc_file)

    for i in fcc_data:
        array2 = []
        array2.append(i["index"])
        array2.append(i["name"])
        strıng1 = ""
        for intgr in range(3):

            strıng1 = strıng1 + ", " + i["purchase"][intgr]["product_category"]
        array2.append(strıng1)
        array.append(array2)

    return array

print(parser())