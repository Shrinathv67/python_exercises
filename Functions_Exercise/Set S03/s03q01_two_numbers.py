""" What does this program do ?
"""

# Implement the helper functions here

def perform_check(number):
    """ This function uses helper functions
        check_if_2digit
        check_if_3digit
        to perform the required operations
    """
    # Your solution code goes here
    # Invoke check_if_2digit and
    # check_if_3digit to check if the number
    # matches the criteria and print accordingly
    if number > 10 and number < 100:
        print(number, "is a two digit number.")
    elif number > 99 and number < 1000:
        print(number, "is a three digit number.")
    else:
        print("The number is", number)

def get_number():
    """ This function prompts the user for a number
        It returns an integer [ and not a string ]
    """
    number = int(input("Please enter the number: "))
    return number

# Main starts from here
def main():
    num1 = get_number()
    num2 = get_number()
    perform_check(num1)
    perform_check(num2) 

if __name__ == "__main__":
    main()
