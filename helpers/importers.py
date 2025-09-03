import requests

from helpers.cli import print_ok


def embed_products(products):
    for product in products:
        print_ok(product)
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
