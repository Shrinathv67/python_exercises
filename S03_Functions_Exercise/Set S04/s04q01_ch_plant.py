""" What does this program do ?
"""

def do_action(present, redmark, bluemark):
    if present > redmark:
        print("Please close the valve.")
    elif present < bluemark:
        print("Please buy more ethanol.")
    else:
        print("The current level of the liquid is at a safe range.")

def get_current_level():
    capacity = int(input("Please enter the capacity of the tank: "))
    current_level = int(input("Please enter the current level of the ethanol: "))
    return capacity,current_level

# Main starts from here
def main():
    capacity,level = get_current_level()
    high =  (0.8 * capacity)
    low =  (0.2 * capacity)
    do_action(level, high, low)

if __name__ == "__main__":
    main()