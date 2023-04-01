import random
import openai

from product_parser import Product, get_products

class DiscountedProduct(Product):
    """
    Discounted Product stores state of a discounted product
    """
    def __init__(self, name, rating, price, image, url, discount):
        """
        :param name: Canadian tire product name
        :param rating: Rating of product
        :param price: intial price of product
        :param image: url of product image
        :param url: url of canadian tire product
        :param discount: floating point in the range[0,1] that represents the discount on the initial price
        """
        super().__init__(name, rating, price, image, url)
        self.discount = discount
        
    def discounted_price(self):
        """
        discounted_price calculates the discounted price of product
        """
        return self.price * (1 - self.discount)
    
    def __repr__(self):
        return f"DiscountedProduct(name='{self.name}', rating={self.rating}, price={self.price}, image='{self.image}', url='{self.url}', discount={self.discount})"

class Bundle:
    """
    Bundle is a clsss that stores list of discounted product & associated methods
    """
    def __init__(self, product_list: [Product], discount_calc):
        """
        :param product_list: List of products
        :param discount_calc: discount function used to convert Product -> DiscountedProduct. discount_calc: (product, product_list) -> DiscountedProduct, where product ϵ product_list And product is an instance of Product 
        """
        self.products = [discount_calc(product, product_list) for product in product_list]
    
    def __repr__(self):
        products_str = ', '.join([f'{p.name} ({p.price}) => ({p.discounted_price()})' for p in self.products])

        #print(products_str)
        return f"Bundle(products=[{products_str}])"


def create_bundle_raw(product: str, response_size: int = 50) -> [str] :
    """
    create_bundle_raw function returns a list of names of products someone would purchase with the intial product seed
    
    :param product: Intial product to seed the response
    :param response_size: maximum character response from openAI
    """
    openai.api_key = "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" #API key needs to be replaced with env variable & current API key doesn't work

    prompt = "name {0} products someone would buy with this:{1}".format(5, product)

    response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0, max_tokens=50)

    text = response["choices"][0]["text"].strip()

    stripped_text = [val.split(".") for val in text.split("\n")]

    filtered_text = list(filter(lambda split_list: len(split_list) == 2, stripped_text))

    filtered_text = list(filter(lambda elem: len(elem[1]) > 1, filtered_text))

    return [val[1][1:] for val in filtered_text]

def project_to_bundle(products: [str]) -> [Product]:
    """
    project_to_bundle converts a list of strings into a list of products using the Canadian Tire search REST API
    
    :param products: list of string that repersents the name of product
    """
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
    """
    percent_off is an higher order function that returns a function that calculates a flat discount on all product
    
    THis is to ensure the algorithm can be easily swaped out with a more intuitive model in the future
    """
    def func(val: Product, og: [Product]):
        return DiscountedProduct(val.name, val.rating, val.price, val.image, val.url, percent)

    return func


if __name__ == "__main__":

    ten_off = percent_off(0.1)
    print(Bundle(project_to_bundle(create_bundle_raw("bike")), ten_off))
