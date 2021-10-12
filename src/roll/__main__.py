import sys
from .roll_dice import roll_dice

def main():
    
    for dice in sys.argv[1:]:
        print(dice)
        roll_dice(dice)

if __name__ == "__main__":
    main()