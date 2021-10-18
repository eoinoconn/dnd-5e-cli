import random

from termcolor import colored

def get_dice(roll_str):
    num_dice, dice_type = roll_str.lower().split("d")
    num_dice = int(num_dice) if len(num_dice) > 0 else 1
    dice_type = int(dice_type)

    return num_dice, dice_type


def throw_dice(num_dice, dice_type):
    results = []
    total = 0
    
    for _ in range(num_dice):
        dice_result = random.randint(1, dice_type)
        total += dice_result
        results.append(dice_result)

    return total, results


def roll(roll_str):
    num_dice, dice_type = get_dice(roll_str)

    total, results = throw_dice(num_dice, dice_type)

    result_str = " + ".join([str(x) for x in results]) + "\n"
    result_str += colored(f"= {total}", 'green') + "\n"
    return result_str
