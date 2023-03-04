import requests

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

def save_input_to_file(user_input):
    # Open a file for writing
    with open('saved_input.txt', 'w') as file:
        # Write the user input to the file
        file.write(user_input)

def load_page(url: str):
    r = requests.get(url, headers=HEADERS)
    return r.text

def get_products(search: str) -> [str]:
    pass

if __name__ == "__main__":
    print(load_page("https://apim.canadiantire.ca/v1/search/search?q=gardening;page=1;store=659;lang=en_CA;count=24"))