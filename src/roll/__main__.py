import sys
from .roll_dice import roll

def main():
    
    for dice in sys.argv[1:]:
        print(dice)
        print(roll(dice))

if __name__ == "__main__":
    main()