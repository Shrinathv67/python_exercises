""" What does this program do ?
A program to get user input regarding the capacity and current_level of the tank.
and a function to raise an alarm to close the valve if the tank is more than 80% full,
or send an sms to buy more liquid if the tank is less than 20% full.

"""

def do_action(present, redmark, bluemark):
    if present > redmark:
        print("Please close the valve.")
    elif present < bluemark:
        print("Please buy more ethanol.")
    else:
        print("The current level of the liquid is at a safe range.")

def get_current_level():
    capacity = int(float(input("Please enter the capacity of the tank: ")))
    current_level = int(float(input("Please enter the current level of the ethanol: ")))
    print(capacity,current_level)
    return capacity,current_level

# Main starts from here
def main():
    capacity,level = get_current_level()
    high =  (0.8 * capacity)
    low =  (0.2 * capacity)
    do_action(level, high, low)

if __name__ == "__main__":
    main()