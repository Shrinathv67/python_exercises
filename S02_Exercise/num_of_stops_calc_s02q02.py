#Script to calculate the mileage of the aar

start_mileage = int(input("Please enter the starting odometer mileage: "))
end_mileage = int(input("Please enter the ending odometer mileage: "))
distance_travelled = end_mileage - start_mileage
print('Distance Travelled: ', distance_travelled, 'Kilometers')
gas_used = int(input("Please enter the amount of fuel used: "))
mileage = distance_travelled/gas_used
print("Mileage of the car: ", mileage, "km/lts")
capacity_of_fuel_tank = int(input("Enter the capacity of tank: "))
num_of_stops = int(560 /(mileage*capacity_of_fuel_tank))
print("The number of stops that the car has to make to refuel is: ",num_of_stops)