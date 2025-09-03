import argparse
import sys
from pathlib import Path

from helpers.cli import print_err
from helpers.csv_utils import read_csv
from helpers.importers import read_csv_from_url
from helpers.ollama import assert_model

# region Defaults
OLLAMA_URL = 'http://localhost:11434'
EMBEDDING_MODEL = 'mxbai-embed-large'
DELIMITER = ','
QUOTECHAR = '"'


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
    # endregion
    # region Embed Products

    # endregion


if __name__ == "__main__":
    main()
