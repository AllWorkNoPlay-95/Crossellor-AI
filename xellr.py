import argparse
import sys
from pathlib import Path

from rich.pretty import pprint

from config import ID_FIELD, BUCKET_STEP, OLLAMA_URL, EMBEDDING_MODEL
from helpers.cli import print_err
from helpers.csv_utils import read_csv
from helpers.importers import read_csv_from_url, embed_products
from helpers.ollama import assert_model


def assert_args(args):
    if args.url is None and args.file is None:
        print_err("Either URL or file path must be specified")
        sys.exit(1)


def init_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', '-u', help='Remote download URL', type=str)
    parser.add_argument('--file', '-f', help='Local file path', type=str)
    parser.add_argument('--output', '-o', help='Output file path', type=str, default="./xellr_output")
    args = parser.parse_args()
    assert_args(args)  # Die if args are invalid
    return args


def main():
    products = []
    args = init_args()
    assert_model(OLLAMA_URL, EMBEDDING_MODEL)

    # region Load CSV
    if args.url:
        products = read_csv_from_url(args.url)
    else:
        file_path = Path(args.file).expanduser().resolve()
        products = read_csv(file_path)

    # Validate
    if len(products) == 0:
        print_err("No products found in CSV data")
        sys.exit(1)

    if ID_FIELD not in products[0]:
        print_err(f"ID field '{ID_FIELD}' not found in CSV data")
        sys.exit(1)
    # endregion

    # region Embed Products
    pprint(products)
    embed_products(products, BUCKET_STEP)
    # endregion


if __name__ == "__main__":
    main()
