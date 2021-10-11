import random

def roll_dice(roll_str):

    num_dice, dice = roll_str.lower().split("d")
    num_dice = int(num_dice) if len(num_dice) > 0 else 1
    dice = int(dice)

    result_str = ""
    result = 0
    for _ in range(num_dice):
        dice_result = random.randint(1, dice)
        result += dice_result
        result_str += str(dice_result)
    
    print(" + ".join(result_str))
    print(f"= {result}")
    print("\n")



