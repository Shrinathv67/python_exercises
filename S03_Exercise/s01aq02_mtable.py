
""" 
Describe what this program does
"""

def print_mtable(multi_num):
    """ 
        Describe what this function does
        The purpose of the function is to print mulplication table of 17 from 1 to 10.
    """
    
    for num in range(1,11):
        print(multi_num,"X",num,"=",multi_num*num)

# Main starts from here
def main():
    print_mtable(17)
      
main()