import json

filename = 'zaman\generated.json'


def parser():
    fcc_data = None
    array= []

    with open(filename, 'r') as fcc_file:
        fcc_data = json.load(fcc_file)

    for i in fcc_data:
        array2 = []
        array2.append(i["index"])
        array2.append(i["name"])
        string1 = ""
        for intgr in range(3):
            string1 = string1 + ", " + i["purchase"][intgr]["product_category"]
        array2.append(string1)
        array.append(array2)

    return array

if __name__ == '__main__':
    print(parser())