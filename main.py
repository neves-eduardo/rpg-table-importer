import argparse
import csv_reader
import simple_table_service

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-f', '--file-list', default=[], nargs='+')

    args = parser.parse_args()

    print(args.file_list)
