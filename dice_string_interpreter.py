import re
import dice_roller

def interpret_dice_string(dice):
    dice_remove_brackets = re.sub("[\\[\\](){}<>]", "", dice)
    spl = dice_remove_brackets.split("d")
    number_of_dice = int(spl[0])
    splited_second_half = re.split("[+\\-*/]", spl[1])
    
    dice_value = int(splited_second_half[0])
    
    dice_result = dice_roller.roll_dice(number_of_dice, dice_value)
    
    result = re.sub('\\[(.*?)\\]', str(dice_result), dice)
    
    return eval(result)