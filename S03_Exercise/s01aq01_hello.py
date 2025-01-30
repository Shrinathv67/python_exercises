def get_username():
    """ 
    Prompt the user to enter his name
    Input : None
    Output : Return the user input as a string
    """
    # Your solution code should go in here
    usr_name = input("Please enter your name: ")
    return usr_name
    

def say_hello(user):
    '''
    Greet the user by saying Hello followed by his name
    Input : user name
    Output : Greeting statement on the screen. No return value
    Example : If input string is Sam
        Then the expected output is
        Hello Sam !!!
    '''
    print("Hello", user, "!!!")

def main():
    '''
    Main function of the program
    '''
    name = get_username()
    say_hello(name)
    
# Main starts from below
main()