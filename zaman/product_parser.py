import requests
import json

# constant used to spoof HTTP request inorder get valid json data from Canadian Tire Search API
HEADERS = (
    {
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'bannerid': 'CTR',
        'basesiteid': 'CTR',
        'dnt': '1',
        'ocp-apim-subscription-key': 'c01ef3612328420c9f5cd9277e815a0e',
        'origin': 'https://www.canadiantire.ca',
        'referer': 'https://www.canadiantire.ca/',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'service-client': 'ctr/web',
        'service-version': 'ctc-dev2',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57',
        'x-br-uid': 'uid%3D235052509575%3Av%3D12.0%3Ats%3D1677923933334%3Ahc%3D11',
        'x-web-host': 'www.canadiantire.ca',
    }
)

class Product:
    """
    Product class stores state and method related with a Canadian Tire Product
    """
    def __init__(self, name, rating, price, image, url):
        """
        :param name: Canadian tire product name
        :param rating: Rating of product
        :param price: intial price of product
        :param image: url of product image
        :param url: url of canadian tire product
        """
        self.name = name
        self.rating = rating
        self.price = price
        self.image = image
        self.url = url
    
    def __repr__(self):
        return f"Product(name='{self.name}', rating={self.rating}, price={self.price}, image='{self.image}', url='{self.url}')"

    # def __str__(self):
    #     return f"{self.name[:10]}..." if len(self.name) > 10 else self.name
    
def get_url(topic: str, page: int, count: int = 10) -> str:
    """
    get_url function creates the required url inorder to search using the Canadian Tire Serach API
    
    :param topic: String of topic that is being searched
    :param page: I don't know what this does after a couple minutes of testing
    :param count: Max number of products that can be returned in a search
    """
    return "https://apim.canadiantire.ca/v1/search/search?q={0};page={1};store=659;lang=en_CA;count={2}".format(topic, page, count)

def get_data(url: str):
    """
    get_data returns data from request
    
    :param url:
    """
    r = requests.get(url, headers=HEADERS)
    return r.text

def parse_json(raw: str):
    """
    parse_json returns json of data
    
    :param raw: unparsed response http body
    """
    return json.loads(raw)

def extract_products(products) -> [Product]:
    """
    extract_products function converts a json object into a list of Products 
    
    :param products: Json repersetnation of a product
    """
    data = []

    if products != None:
        for product in products:
            
            if product["type"] == "PRODUCT":
                name = product["title"]
                rating = product["rating"]
                price = product["currentPrice"]["value"]
                image = product["images"][0]["url"] if len(product["images"]) > 0 else ""
                url = "https://www.canadiantire.ca"+product["url"]

                data.append(Product(name, rating, price, image, url))
        
    return data

def get_products(item: str) -> [Product]:
    """
    get_products function gets a list of products from an item prompt
    
    :param item: iitial prompt used to get a list of products
    """
    url = get_url(item, 1)

    raw_data = get_data(url)
    
    products = parse_json(raw_data)["products"]

    return extract_products(products)

if __name__ == "__main__":
    products = get_products("gardening")
    
    for p in products:
        print(p)

