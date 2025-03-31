"""
Print all the squares of the numbers that are less than the number entered as input by the user.
"""
from math import pow

def get_usr_input():
    num = int(input('Please enter a numnber:'))
    return num

def num_square(usr_num):
    square_nums = []
    for nums in range(1, usr_num+1):
        if int(pow(nums,2)) <= usr_num:
            square_nums.append(int(pow(nums,2)))
    print(f"The number of square numbers which are less than the user input number are: {square_nums}")

def main():
    usr_num = get_usr_input()
    num_square(usr_num)

if __name__ == "__main__":
    main()