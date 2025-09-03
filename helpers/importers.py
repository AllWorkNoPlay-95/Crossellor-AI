import re

import requests


def contains_digits(string):
    if not isinstance(string, str):
        return False
    pattern = r'^\d+(?:[,\.]\d+)?$'
    return bool(re.match(pattern, string))


def embed_products(products, bucket_step):
    for product in products:
        for key, value in product.items():
            if contains_digits(value):
                print(f"Found numeric values in field '{key}': {value}")

    return products


def embed_orders():
    pass


def read_csv_from_url(url):
    response = requests.get(url)
    # TODO: Decode into products
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Failed to download from {url}")
