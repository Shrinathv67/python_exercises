"""
Script to calculate mileage by using functions.

"""
# This function definition gets inputs from the user about the starting, ending odometer reading
def usr_input():
    start_mileage = int(input("Please enter the starting odometer mileage: "))
    end_mileage = int(input("Please enter the ending odometer mileage: "))
    fuel_consumed = int(input("Please enter the amount of fuel used: "))
    tank_capacity = int(input("Enter the capacity of tank: "))
    return start_mileage,end_mileage,fuel_consumed,tank_capacity

#This function takes the input from the previous function and calculates the mileage using the formula in line 15.
def mileage_calc(start_mileage, end_mileage, gas_used):
    distance_travelled = end_mileage - start_mileage
    mileage = distance_travelled/gas_used
    print("Mileage of the car: ", mileage, "km/lts")
    return mileage

#This function calculates the number of stops that the car has to make to refuel to cover the distance of 560 KM assuming that the car starts with full fuel tank.
def number_of_stops(mileage,capacity_of_fuel_tank):
    num_of_stops = 560//(mileage*capacity_of_fuel_tank)
    print("The number of stops that the car has to make refuel to cover the distance of 560 KMs is:",num_of_stops)


#This function calls the other two functions to get user inputs and to calculate the mileage.
def main():
    start_mil, end_mil, gas_used,tank_capacity = usr_input()
    mil = mileage_calc(start_mil,end_mil,gas_used)
    number_of_stops(mil,tank_capacity)
50


#Main program starts here
main()

