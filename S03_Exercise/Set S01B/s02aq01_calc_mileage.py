"""
Script to calculate mileage by using functions.

"""
# This function definition gets inputs from the user about the starting, ending odometer reading
def usr_input():
    start_mileage = int(input("Please enter the starting odometer mileage: "))
    end_mileage = int(input("Please enter the ending odometer mileage: "))
    fuel_consumed = int(input("Please enter the amount of fuel used: "))
    return start_mileage,end_mileage,fuel_consumed

#This function takes the input from the previous function and calculates the mileage using the formula in line 15.
def mileage_calc(start_mileage, end_mileage, gas_used):
    distance_travelled = end_mileage - start_mileage
    mileage = distance_travelled/gas_used
    print("Mileage of the car: ", mileage, "km/lts")

#This function calls the other two functions to get user inputs and to calculate the mileage.
def main():
    start_mil, end_mil, gas_used = usr_input()
    mileage_calc(start_mil,end_mil,gas_used)
50


#Main program starts here
main()

