import argparse
import csv_reader
import simple_table_service

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-f', '--file-list', default=[], nargs='+')

    args = parser.parse_args()

    for file in args.file_list:
        df = csv_reader.read_csv(file)
        result = simple_table_service.roll_on_table(df)
        print(file.replace(".csv", "") + " result: " + result)
