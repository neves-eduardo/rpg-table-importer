import json
import random
import dice_string_interpreter

STRING_FORMAT_PARAM_NAME = "StringFormat"
PARAM_NAME = "Parameters"
VARIABLES_NAME = "Rolls"

def roll_template_json(path):
    template_json_dict = json.load(open(path))
        
    param_dict = roll_parameters(template_json_dict)
    variable_dict = roll_variables(template_json_dict)
    
    param_dict.update(variable_dict)
    
    return format_string(template_json_dict[STRING_FORMAT_PARAM_NAME], param_dict)

def roll_parameters(data):
    parameters_dict:dict = data[PARAM_NAME].items()
    rolled_dict = {}
    if parameters_dict:
        for key, value in parameters_dict:
            rolled_dict[key] = roll_on_table(value)

    return rolled_dict

def roll_variables(data):
    variables_dict:dict = data[VARIABLES_NAME].items()
    rolled_dict = {}
    if variables_dict:
        for key, value in variables_dict :
            rolled_dict[key] = dice_string_interpreter.interpret_dice_string(value)
    return rolled_dict

def roll_on_table(table):
    return table[random.randint(0, len(table)-1)]

def format_string(string_format:str, parameter_dict):
    return string_format.format_map(parameter_dict)

print(roll_template_json("templates/settlement.json"))
