"""
This program is for printing the multiplication table of a number using For Loop and While Loop
"""


def get_userinput():
    num = int(input("Please enter a number for printing the multiplication table:"))
    multiplier_limit = int(input("Please enter the number till when the multiplication has be be performed: "))
    return num, multiplier_limit


def loop_print(num,mult_limit):
    print("Print using For Loop.")
    print("_____________________")
    for i in range(1,(mult_limit+1)):
        print(num,"X",i,"=",num*i)

    print("----------------------")

    print("Print using While Loop.")
    print("_____________________")
    j = 1
    while (j<(mult_limit+1)):
        print(num,"X",j,"=",num*j)
        j += 1


def main():
    num, multiplier_limit = get_userinput()
    loop_print(num,multiplier_limit)


if __name__ == "__main__":
    main()