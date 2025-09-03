import argparse
import sys
from pathlib import Path

from helpers.cli import print_ok, print_err
from helpers.importers import download_csv_from_url, import_products
from helpers.ollama import assert_model

OLLAMA_URL = 'http://localhost:11434'
EMBEDDING_MODEL = 'mxbai-embed-large'


def assert_args(args):
    if args.url is None and args.file is None:
        print_err("Either URL or file path must be specified")
        sys.exit(1)


def init_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', '-u', help='Remote download URL', type=str)
    parser.add_argument('--file', '-f', help='Local file path', type=str)
    parser.add_argument('--delimiter', '-d', help='Delimiter character', type=str, default=',')
    parser.add_argument('--quotechar', '-q', help='Quote character', type=str, default='"')
    parser.add_argument('--embedding-model', help='Embedding model name (Ollama)', type=str, default=EMBEDDING_MODEL)
    parser.add_argument('--ollama-url', help='Ollama server URL', type=str, default=OLLAMA_URL)

    args = parser.parse_args()
    assert_args(args)  # Die if args are invalid
    return args


def main():
    products = []
    args = init_args()
    assert_model(args.ollama_url, args.embedding_model)

    # region Load CSV
    if args.url:
        csv = download_csv_from_url(args.url)
    else:
        file_path = Path(args.file).expanduser().resolve()
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                csv = f.read()
            path = str(file_path)
            print_ok(f"Loaded {len(csv.splitlines())} rows from {path}")
        except FileNotFoundError:
            print_err(f"File not found: {file_path}")
            sys.exit(1)
    # endregion
    # region Load Products
    products = import_products(csv)
    # endregion


if __name__ == "__main__":
    main()
