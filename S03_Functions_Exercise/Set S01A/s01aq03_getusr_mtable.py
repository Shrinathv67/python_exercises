
""" 
    Mention what this program does
"""

def get_number():
    """ 
        This function should fetch a number from user
        Input : None
        Return : an integer
    """
    number = input("Please enter the number for multiplcation: ")
    # Check out your code behaviour by commenting the line below
    number = int(number) # What happens if you dont perform this operation ? Answer: The number from previous step in in string format. Hence this step is necessary to
    #convert string into int format to perform the operatiob in the below function. If not converted, it results in string multiplication.
    return number


def print_mtable(num):
    """ 
        This function prints the multiplication table of num
        Input : an integer
        Output : Display multiplication table of input integer
        Return : None
    """
    for multiply in range(1,11):
        print(num,"X",multiply,"=",num*multiply)
    # Your solution code goes in here

def main():
    '''
        Main program
    '''
    inp = get_number()
    print_mtable(inp)

# Main starts from here
main()