import pandas
import random


def roll_on_table(table: pandas.DataFrame):
    return table["value"][random.randint(0, len(table))]
