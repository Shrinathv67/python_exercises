"""Program to print the max and min of the numbers entered by the user until the user enters zero."""

def get_usrinput():
   num = 0
   while num!=0:
       num = input("Please enter the number")
   else:
       return "The user has input 0."
 
def main():
    usr_num = get_usrinput()


if __name__ == "__main__":
    main()
    