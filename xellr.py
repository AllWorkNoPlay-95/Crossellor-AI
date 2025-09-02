import argparse
import sys


def assert_args(args):
    if args.url is None and args.file is None:
        print("Error: Either URL or file path must be specified", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', '-u', help='Remote download URL', type=str)
    parser.add_argument('--file', '-f', help='Local file path', type=str)
    args = parser.parse_args()
    assert_args(args)


if __name__ == "__main__":
    main()
