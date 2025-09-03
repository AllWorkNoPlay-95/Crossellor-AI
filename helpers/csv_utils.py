import csv
import sys

from config import DELIMITER, QUOTE_CHAR
from helpers.cli import print_err, print_ok, print_info


def read_csv(file_path):
    """
    Read data from a CSV file and return list of rows
    Args:
        file_path (Path): Path to CSV file to read
    Returns:
        list: List of dictionaries with header keys
    """
    rows = []
    try:
        with open(file_path, 'r', newline='\n') as csvfile:
            reader = csv.reader(csvfile, delimiter=DELIMITER, quotechar=QUOTE_CHAR)
            headers = next(reader)
            print_info(f"({len(headers)}) Product attributes: {headers}")

            for row in reader:
                rows.append(dict(zip(headers, row)))

            print_ok(f"Loaded {len(rows)} rows from {file_path}")
        return rows
    except FileNotFoundError:
        print_err(f"File not found: {file_path}")
        sys.exit(1)


def write_csv(filename, data):
    """
    Write data to a CSV file
    Args:
        filename (str): Path to CSV file to write
        data (list): List of rows to write to CSV
    """
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
