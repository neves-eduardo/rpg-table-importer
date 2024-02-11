import random
    
def roll_dice(number_of_rolls, dice_value):
    sum = 0
    for roll in range(number_of_rolls):
        sum += random.randint(1, dice_value)
    return sum