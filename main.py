import csv_reader
import simple_table_service

if __name__ == '__main__':
    df = csv_reader.read_csv("./files/trigger.csv")
    print(df)
    print(simple_table_service.roll_on_table(df))
