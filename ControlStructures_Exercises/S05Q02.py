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
    count_2, count_3, count_1 = 0,0,0
    for nums in num_list:
        if nums > 0 and nums < 10:
            count_1 = count_2 + 1
        elif nums > 10 and nums < 100:
            count_2 += 1
        elif nums > 100 and nums < 1000:
            count_3 += 1
        else:
            print(f"The user has entered a number with more than three digits and the number is {nums}")
    print(f"The number of single digit number is {count_1}")
    print(f"The number of two digit number is : {count_2}")
    print(f"The number of three digit number is: {count_3}")
def main():
    list_of_num = []
    list_of_num = get_usrinput()
    do_max_min_num(list_of_num)
    do_digit_check(list_of_num)


if __name__ == "__main__":
    main()
    