import sys
from .roll import roll_

def main():
    print(sys.argv)
    
    for dice in sys.argv[1:]:
        print(dice)
        roll_(dice)

if __name__ == "__main__":
    main()