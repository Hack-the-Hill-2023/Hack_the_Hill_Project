import random
import json

# The file path for the JSON file to be parsed
filename = 'zaman/generated.json'

def parser(name):
    # Initialize the fcc_data variable
    fcc_data = None
    
    # Open the JSON file for reading and load its contents into fcc_data
    with open(filename, 'r') as fcc_file:
        fcc_data = json.load(fcc_file)
    
    # Iterate through the fcc_data JSON object and return a randomly chosen product category for the given name
    for i in fcc_data:
        if name == i["name"]:
            rand=random.randint(0,len(i["purchase"])-1)
            return i["purchase"][rand]["product_category"]

    # Return an empty string if the name is not found in the JSON file
    return ""

# Test the parser function with a specific name
if __name__ == '__main__':
    print(parser("Lucile Roman"))
