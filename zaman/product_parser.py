import requests
import json

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

class Project:
    def __init__(self, name, rating, price):
        self.name = name
        self.rating = rating
        self.price = price
    
    def __repr__(self):
        return f"Project(name='{self.name}', rating={self.rating}, price={self.price})"

def get_url(topic: str, page: int, count: int = 100) -> str:
    return "https://apim.canadiantire.ca/v1/search/search?q={0};page={1};store=659;lang=en_CA;count={2}".format(topic, page, count)

def get_data(url: str):
    r = requests.get(url, headers=HEADERS)
    return r.text

def parse_json(raw: str):
    return json.loads(raw)

def extract_products(products) -> [Project]:
    data = []

    for product in products:
        if product["type"] == "PRODUCT":
            name = product["title"]
            rating = product["rating"]
            price = product["currentPrice"]["value"]

            data.append(Project(name, rating, price))
    
    return data

if __name__ == "__main__":

    url = get_url("gardening",2)
    raw_data = get_data(url)
    products = parse_json(raw_data)["products"]

    print(len(products))

    products = extract_products(products)
    
    for p in products:
        print(p)

