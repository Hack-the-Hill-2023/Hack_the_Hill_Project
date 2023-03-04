import random
import openai
import json

from product_parser import Product, get_products

def create_bundle_raw(product: str, response_size: int = 50) -> str :
    openai.api_key = "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"

    prompt = "name {0} products someone would buy with this:{1}".format(response_size, product)

    response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0, max_tokens=50)

    text = response["choices"][0]["text"].strip()

    stripped_text = [val.split(".") for val in text.split("\n")]

    filtered_text = list(filter(lambda split_list: len(split_list) == 2, stripped_text))

    filtered_text = list(filter(lambda elem: len(elem[1]) > 1, filtered_text))

    return [val[1][1:] for val in filtered_text]

def project_to_bundle(products: [str]) -> [Product]:
    data = []

    for product in products:
        print(product)
        tmp = get_products(product)

        if len(tmp) > 0:
            data.append(random.choice(tmp))
        
    return data

if __name__ == "__main__":
    print(project_to_bundle(create_bundle_raw("bike")))
    print(project_to_bundle(create_bundle_raw("seeds")))
