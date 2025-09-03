import csv


def read_csv(filename):
    """
    Read data from a CSV file and return list of rows
    Args:
        filename (str): Path to CSV file to read
    Returns:
        list: List of rows from CSV file
    """
    rows = []
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            rows.append(row)
    return rows


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
