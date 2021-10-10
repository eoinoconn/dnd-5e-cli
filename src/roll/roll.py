import random
import sys

def roll_(roll_str):

    num_dice, dice = [int(x) for x in roll_str.lower().split("d")]

    result_str = ""
    result = 0
    for _ in range(num_dice):
        dice_result = random.randint(1, dice)
        result += dice_result
        result_str += f" + {dice_result}"
    
    print(result_str)
    print(f"= {result}")
    print("\n")



