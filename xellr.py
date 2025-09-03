import argparse
import sys
from pathlib import Path

from rich.pretty import pprint

from helpers.cli import print_err
from helpers.csv_utils import read_csv
from helpers.importers import read_csv_from_url, embed_products
from helpers.ollama import assert_model

# region Defaults
OLLAMA_URL = 'http://localhost:11434'
EMBEDDING_MODEL = 'mxbai-embed-large'
DELIMITER = ','
QUOTECHAR = '"'
BUCKET_STEP = 5


# endregion

def assert_args(args):
    if args.url is None and args.file is None:
        print_err("Either URL or file path must be specified")
        sys.exit(1)


def init_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', '-u', help='Remote download URL', type=str)
    parser.add_argument('--file', '-f', help='Local file path', type=str)
    parser.add_argument('--delimiter', '-d', help='Delimiter character', type=str, default=DELIMITER)
    parser.add_argument('--quotechar', '-q', help='Quote character', type=str, default=QUOTECHAR)
    parser.add_argument('--embedding-model', help='Embedding model name (Ollama)', type=str, default=EMBEDDING_MODEL)
    parser.add_argument('--ollama-url', help='Ollama server URL', type=str, default=OLLAMA_URL)
    parser.add_argument('--id-field', '-i', help='ID field name', type=str, default='id')
    parser.add_argument('--bucket-step', '-b', help='Bucket step size', type=int, default=BUCKET_STEP)
    args = parser.parse_args()
    assert_args(args)  # Die if args are invalid
    return args


def main():
    products = []
    args = init_args()
    assert_model(args.ollama_url, args.embedding_model)

    # region Load CSV
    if args.url:
        products = read_csv_from_url(args.url)
    else:
        file_path = Path(args.file).expanduser().resolve()
        products = read_csv(file_path, args.delimiter, args.quotechar)

    # Validate
    if len(products) == 0:
        print_err("No products found in CSV data")
        sys.exit(1)

    if args.id_field not in products[0]:
        print_err(f"ID field '{args.id_field}' not found in CSV data")
        sys.exit(1)
    # endregion

    # region Embed Products
    pprint(products)
    embed_products(products, args.bucket_step)
    # endregion


if __name__ == "__main__":
    main()
