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
        array3 = []
        for intgr in range(3):
            array3.append(i["purchase"][intgr]["product_category"])
        array2.append(array3)
        array.append(array2)

    return array

print(parser())