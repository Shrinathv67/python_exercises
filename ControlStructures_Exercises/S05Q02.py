"""Program to print the max and min of the numbers entered by the user until the user enters zero."""

def get_usrinput():
   num = int(input("Please enter a number:"))
   num_list = []
   while num != 0:
       num_list.append(num)
       num = int(input("Please enter a number:"))
   print("The user has entered a zero.")
   return num_list    

def do_max_min_num(num_list):
    num_list.sort()
    print(f"The Min number from the user entered numbers is :{num_list[0]}")
    print(f"The Max number from the user entered numbers is :{num_list[-1]}")
    
def do_digit_check(num_list):
    for nums in num_list:
        if nums > 0 and nums < 10:
            print("The number is a single digit number.")
        elif nums > 10 and nums < 100:
            print("The number is a two digit number.")
        elif nums > 100 and nums < 1000:
            print("The number is a three digit number.")
        else:
            print(f"The number is {nums}")

def main():
    list_of_num = []
    list_of_num = get_usrinput()
    do_max_min_num(list_of_num)
    do_digit_check(list_of_num)


if __name__ == "__main__":
    main()
    