"""
Program to find whether a user input number is part of a fibonacci sequence. 
If not, print the closest fibonacci sequence number.

"""

def fibonacci_num(number):
    fibonacci_seq = [0]
    list_adder = 1
    while fibonacci_seq[-1] < number:
        if fibonacci_seq[-1] ==0:
            list_adder = fibonacci_seq[-1] + list_adder
            fibonacci_seq.append(list_adder)
            
        else:
# This logic will create a sequence with one number in the sequence greater than the user provided number. This was allowed to 
# find the nearest number in the fibonacci sequence. 
            list_adder = fibonacci_seq[-2]+ fibonacci_seq[-1]
            fibonacci_seq.append(list_adder)
    print(f"The fibonacci sequence is: {fibonacci_seq}")
    return fibonacci_seq

#Added this logic to consider sequence with numbers only less than the user provided number.  This will create a sequence always
#less than the user provided number.
#           if list_adder > number:
#               break
#            else:
#                fibonacci_seq.append(list_adder)
#                print(fibonacci_seq)
        
def find_nearest_fibonacci_num(sequence,usr_num):
    if usr_num in sequence:
        print("The user input number is present in the Fibonacci Sequence.")
    elif abs(usr_num-sequence[-1]) > abs(usr_num-sequence[-2]):
        print(f"The nearest fibonacci sequence number to the user input number is: {sequence[-2]}")
    else:
        print(f"The nearest fibonacci sequence number to the user input number is: {sequence[-1]}")

def get_usr_input():
    num = int(input("Please enter a number:"))
    return num


def main():
    number = get_usr_input()
    fibonacci_seq = fibonacci_num(number)
    find_nearest_fibonacci_num(fibonacci_seq,number)

if __name__ == "__main__":
    main()