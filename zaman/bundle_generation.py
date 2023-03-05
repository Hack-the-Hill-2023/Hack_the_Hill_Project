import random
import openai

from product_parser import Product, get_products
class DiscountedProduct(Product):
    def __init__(self, name, rating, price, image, url, discount):
        super().__init__(name, rating, price, image, url)
        self.discount = discount
        
    def discounted_price(self):
        return self.price * (1 - self.discount)
    
    def __repr__(self):
        return f"DiscountedProduct(name='{self.name}', rating={self.rating}, price={self.price}, image='{self.image}', url='{self.url}', discount={self.discount})"

class Bundle:
    def __init__(self, project_list: [Product], discount_calc):
        self.products = [discount_calc(project, project_list) for project in project_list]
    
    def __repr__(self):
        products_str = ', '.join([f'{p.name} ({p.price}) => ({p.discounted_price()})' for p in self.products])

        print(products_str)
        return f"Bundle(products=[{products_str}])"


def create_bundle_raw(product: str, response_size: int = 50) -> str :
    openai.api_key = "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"

    prompt = "name {0} products someone would buy with this:{1}".format(5, product)

    response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0, max_tokens=50)

    text = response["choices"][0]["text"].strip()

    stripped_text = [val.split(".") for val in text.split("\n")]

    filtered_text = list(filter(lambda split_list: len(split_list) == 2, stripped_text))

    filtered_text = list(filter(lambda elem: len(elem[1]) > 1, filtered_text))

    return [val[1][1:] for val in filtered_text]

def project_to_bundle(products: [str]) -> [Product]:
    data = []

    for product in products:
        tmp = get_products(product)
        while len(tmp) > 0 :
            val = random.choice(tmp);

            if val.price == None:
                tmp.remove(val)
            else:
                data.append(val)
                break

        
    return data

def percent_off(percent: float):
    def func(val: Product, og: [Product]):
        return DiscountedProduct(val.name, val.rating, val.price, val.image, val.url, percent)

    return func


if __name__ == "__main__":

    ten_off = percent_off(0.1)
    print(Bundle(project_to_bundle(create_bundle_raw("bike")), ten_off))
