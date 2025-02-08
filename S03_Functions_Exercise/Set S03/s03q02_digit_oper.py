""" This program requests for a number from the user. It then determines whether the number is a single, double or triple digit number. Based on the inference operations are carried out and the 
One's place of the final resultant number is displayed.
"""

# Implement the helper functions here
# This function performs operations if the user input number is a 1 digit number. It adds 7 to the number and displays the one's place of the resultant number.

def do_1digit_oper(num_1digit):
    num_1digit +=7
    num_1digit = str(num_1digit)
    print(num_1digit[-1])

# This function performs operations if the user input number is a 2 digit number. It raises the number to the power of 5 and displays the one's place of the resultant number.

def do_2digit_oper(num_2digit):
    num_2digit **= 5
    num_2digit = str(num_2digit)
    print(num_2digit[-1])


# This function performs operations if the user input number is a 3 digit number. It requests for another number from the user and adds it to the original 3 digit number 
# and displays the one's place of the resultant number.

def do_3digit_oper(num_3digit):
     num2 = int(input("Please enter a number to add to the three digit number: "))
     num_3digit = num_3digit + num2
     num_3digit = str(num_3digit)
     print(num_3digit[-1])

def perform_check(number):
    """ This function uses helper functions
        check_if_2digit
        check_if_3digit
        to perform the required operations
    """
    #This control statement logic determines whether the user input number is a one digit, two digit or three digit number. Depending upon the number of digits, it will call the corresponding 
    #functions to perform operations.
    if number > 0 and number < 10:       
        do_1digit_oper(number)
    elif number > 9 and number < 100:
        do_2digit_oper(number)
    elif number > 99 and number < 1000:     
        do_3digit_oper(number)

#This function definition is to request for user input for a number.
def get_number():
    """ This function prompts the user for a number
        It returns an integer [ and not a string ]
    """
    number = int(input("Please enter the number: "))
    return number

# Main starts from here
num = get_number()
perform_check(num)


