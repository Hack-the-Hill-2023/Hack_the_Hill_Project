import json

filename = 'zaman\generated.json'

def parser(name):
    fcc_data = None

    array = []
    array2 = []
    with open(filename, 'r') as fcc_file:
        fcc_data = json.load(fcc_file)

    for i in fcc_data:
        if name == i["name"]:
            for intgr in range(len(i["purchase"])):
                array2 = [intgr, i["purchase"][intgr]["product_category"]]
                array.append(array2)

    return array


if __name__ == '__main__':
    print(parser("Lucile Roman"))