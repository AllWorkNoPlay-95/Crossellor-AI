import requests


def import_products():
    pass


def import_orders():
    pass


def download_csv_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Failed to download from {url}")
