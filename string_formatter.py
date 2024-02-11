import json
import random

def roll_template_json(path):
    template_json_dict = json.load(open(path))
        
    param_dict = roll_parameters(template_json_dict)
    return format_string(template_json_dict["StringFormat"], param_dict)

def format_string(string_format:str, parameter_dict):
    return string_format.format_map(parameter_dict)

def roll_parameters(data):
    rolled_dict = {}
    for key, value in data["Parameters"].items():
        rolled_dict[key] = roll_on_table(value)
    return rolled_dict

def roll_on_table(table):
    return table[random.randint(0, len(table)-1)]

print(roll_template_json("templates/settlement.json"))